from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

app = Flask(__name__)

# Load datasets
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')
most_runs = pd.read_csv('most_runs_average_strikerate.csv')
teams = pd.read_csv('teams.csv')
teamwise = pd.read_csv('teamwise_home_and_away.csv')

# Data preprocessing
matches = matches[matches['result'] != 'no result']  # Remove matches with no result

# Feature Engineering
# Extract the year from the date column
matches['year'] = pd.to_datetime(matches['date'], dayfirst=True).dt.year

# Encode the winner as binary (0 or 1)
matches['winner'] = matches['winner'].apply(lambda x: 1 if x == 'winner' else 0)

# Merge teamwise home and away stats
teamwise = teamwise.rename(columns={'team': 'team1'})
matches = matches.merge(teamwise, how='left', on='team1')

# Extract features
features = matches[['team1', 'team2', 'toss_winner', 'toss_decision', 'venue', 'home_win_percentage', 'away_win_percentage']]
target = matches['winner']

# Encode categorical variables
features = pd.get_dummies(features, columns=['team1', 'team2', 'toss_winner', 'toss_decision', 'venue'])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train model
model = XGBClassifier()
model.fit(X_train, y_train)

def predict_winner(team1, team2, toss_winner, toss_decision, venue, home_win_percentage, away_win_percentage):
    match_data = pd.DataFrame([[team1, team2, toss_winner, toss_decision, venue, home_win_percentage, away_win_percentage]], 
                               columns=['team1', 'team2', 'toss_winner', 'toss_decision', 'venue', 'home_win_percentage', 'away_win_percentage'])
    match_data = pd.get_dummies(match_data, columns=['team1', 'team2', 'toss_winner', 'toss_decision', 'venue'])
    missing_cols = set(features.columns) - set(match_data.columns)
    for c in missing_cols:
        match_data[c] = 0
    match_data = match_data[features.columns]  # Ensure the order of columns is same as training data
    prediction = model.predict(match_data)
    return prediction[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        team1 = request.form['team1']
        team2 = request.form['team2']
        toss_winner = request.form['toss_winner']
        toss_decision = request.form['toss_decision']
        venue = request.form['venue']
        home_win_percentage = float(request.form['home_win_percentage'])
        away_win_percentage = float(request.form['away_win_percentage'])
        
        prediction = predict_winner(team1, team2, toss_winner, toss_decision, venue, home_win_percentage, away_win_percentage)
        prediction = team1 if prediction == 1 else team2

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
