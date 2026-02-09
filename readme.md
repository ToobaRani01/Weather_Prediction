# 🌦️ Weather Prediction & Probability System

An interactive machine learning web application that predicts weather types (Rainy, Cloudy, Sunny, Snowy) based on various atmospheric parameters with high confidence and probability distribution visualization.

## 🚀 Features

- **Real-time Prediction**: Instantly predict the weather type based on numeric and categorical inputs.
- **Confidence Scoring**: View the model's confidence percentage for the predicted weather.
- **Probability Distribution**: Interactive bar charts showing the likelihood of all possible weather conditions using Plotly.
- **Sleek UI/UX**: Modern, responsive dashboard built with Streamlit, featuring custom CSS, glassmorphism effects, and a user-friendly layout.
- **Data-Driven Model**: Built using a Random Forest Classifier trained on a comprehensive weather dataset.

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Data Handling**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Machine Learning**: [Scikit-Learn](https://scikit-learn.org/) (Random Forest Classifier)
- **Visualization**: [Plotly Express](https://plotly.com/python/plotly-express/)
- **Model Serialization**: [Joblib](https://joblib.readthedocs.io/)

## 📋 Project Structure

```text
WEATHER_PREDICTION/
├── app.py                # Main Streamlit application
├── dataset.csv           # Raw weather data
├── model_build.ipynb     # Jupyter notebook for EDA and model training
├── weather_rf_model.pkl  # Trained Random Forest model
├── scaler.pkl            # Standardized scaler for feature normalization
├── label_encoders.pkl    # Encoders for categorical variables
├── selected_features.pkl # Features selected for prediction
└── requirements.txt      # Project dependencies
```

## ⚙️ How to Run the Project

Follow these steps to set up and run the application locally:

### 1. Clone the Repository
```bash
git clone <https://github.com/ToobaRani01/Weather_Prediction>
cd WEATHER_PREDICTION
```

### 2. Install Dependencies
It is recommended to use a virtual environment:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Streamlit server to view the app in your browser:
```bash
streamlit run app.py
```
The app will typically be available at `http://localhost:8501`.

## 📊 Features & Dataset Columns
The project utilizes 11 key features/columns from the weather dataset:
- **Temperature**: Input range from -10°C to 50°C
- **Humidity**: 0% to 100%
- **Wind Speed**: 0 to 100 km/h
- **Precipitation (%)**: 0% to 100%
- **Cloud Cover**: Categorical (Clear, Cloudy, Overcast, Partly Cloudy)
- **Atmospheric Pressure**: 950 to 1050 hPa
- **UV Index**: UV intensity level (0 to 14+)
- **Season**: Categorical (Winter, Spring, Summer, Autumn)
- **Visibility (km)**: Distance in kilometers
- **Location**: Specific region category (Inland, Mountain, Coastal)
- **Weather Type**: Target variable for prediction (Rainy, Cloudy, Sunny, Snowy)

## 👤 Credits
Created by **Tooba Rani** — AI Engineer
