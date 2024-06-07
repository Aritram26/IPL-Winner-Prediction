# IPL Winner Prediction

This project aims to predict the winner of an IPL match based on various inputs such as teams, toss winner, toss decision, venue, and win percentages. The prediction is made using a machine learning model.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Project Description

The IPL Winner Prediction project uses historical IPL match data to train a machine learning model that can predict the outcome of an IPL match. Users can input details about an upcoming match, and the model will predict the likely winner.

## Installation

To run this project locally, follow these steps:

1. **Install the required packages:**

    Make sure you have Python installed. Then, install the required packages using pip:

    ```sh
    pip install -r requirements.txt
    ```

2. **Prepare the dataset:**

    Place your datasets (`deliveries.csv`, `matches.csv`, `most_runs_average_strikerate.csv`, `Players.xlsx`, `teams.csv`, `teamwise_home_and_away.csv`) in the appropriate directory.

## Usage

1. **Run the Flask application:**

    Start the Flask server to run the web application:

    ```sh
    python app.py
    ```

2. **Open the application in your web browser:**

    Navigate to `http://127.0.0.1:5000` in your web browser.

3. **Input match details:**

    Enter the details of the IPL match you want to predict, including the teams, toss winner, toss decision, venue, and win percentages.

4. **Get the prediction:**

    Click on the "Predict Winner" button to see the predicted winner of the match.

## Files

- `app.py`: The main Flask application file.
- `ipl_winner_prediction.py`: The machine learning model training and prediction script.
- `templates/index.html`: The HTML template for the web interface.
- `static/style.css`: The CSS file for styling the web interface.
- `requirements.txt`: The list of required Python packages.

## Technologies

- Python
- Flask
- Pandas
- Scikit-learn
- XGBoost
- HTML/CSS

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
