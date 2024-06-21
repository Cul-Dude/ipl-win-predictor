# IPL-WIN-PREDICTOR

# Introduction
The IPL Win Predictor is a machine learning project that predicts the winning probability of an ongoing IPL cricket match based on the current match situation. This project utilizes historical IPL data to train a model that can provide real-time predictions, helping fans and analysts gauge the likely outcome of a match.

# Features
1) **Real-time Prediction**: Get win probabilities for both teams based on the current score, overs bowled, and wickets fallen.
2) **User-friendly Interface**: A Streamlit web app providing an interactive and easy-to-use interface.
3) **Comprehensive Data**: Utilizes extensive IPL historical data for accurate predictions.

   
# Demo
Live App

Check out the live app here: [IPL Win Predictor](https://ipl-win-predictor-aditya.streamlit.app/).

# How to Use the App
1) **Select Teams**: Choose the chasing team and defending teams from the dropdowns.
2) **Enter The Equation**: Provide current match details like the target to chase, score of chasing team, overs bowled by bowling team, and wickets of batting team fallen.
3) **Predict:** Click the "Predict" button to get the live winning probabilities.

# Datasets Used
1) **MATCHES.csv**
2) **DELIVERIES.csv**
   Details about these datasets and how I proceeded further in the project is given in *ipl-prediction.ipynb* 

# How It Works
The project uses a machine learning pipeline built with scikit-learn, which includes:

1) **Data Preprocessing**: Cleans and prepares the data for training.
2) **Feature Engineering**: Creates meaningful features such as current run rate and required run rate.
3) **Model Training**: Uses historical IPL match data to train a classification model.
4) **Prediction**: The model predicts the win probabilities based on the provided match situation.


# Model Performance
The model has been evaluated using various metrics and has shown promising results in predicting match outcomes. Accuracy of 80% is achieved. Detailed performance metrics and validation results can be found in the jupyter notebook attached.

# Contributions
I welcome contributions to improve the IPL Win Predictor. If you have ideas or find bugs, feel free to open an issue or submit a pull request.



# Acknowledgements
Thanks to the creators of the datasets used in this project. The same dataset can be found in this [kaggle notebook](https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set)
Special thanks to the Streamlit team for their amazing visualization library.

