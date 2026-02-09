import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="Weather Prediction",
    page_icon="🌦️",
    layout="wide"
)

# Custom CSS (UI + Green Button)
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3 {
        text-align: center;
    }
    .prediction-card {
        background: linear-gradient(135deg, #00c6ff, #0072ff);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.35);
        color: white;
    }
    div.stButton > button {
        background-color: #2ecc71;
        color: white;
        border-radius: 10px;
        padding: 0.6em 1.5em;
        font-size: 16px;
        font-weight: 600;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #27ae60;
    }
</style>
""", unsafe_allow_html=True)

# Load Model Assets
model = joblib.load("weather_rf_model.pkl")
scaler = joblib.load("scaler.pkl")
selected_features = joblib.load("selected_features.pkl")
encoders = joblib.load("label_encoders.pkl")

# Title
st.title("🌦️ Weather Type Prediction & Probability")

# Inputs Section
st.markdown("### 🧮 Weather Input Parameters")

input_data = {}

# Label ranges (ONLY text)
label_ranges = {
    "Temperature": "Temperature (°C) (-10 — 50)",
    "Humidity": "Humidity (%) (0 — 100)",
    "Wind Speed": "Wind Speed (km/h) (0 — 100)",
    "Pressure": "Pressure (hPa) (950 — 1050)",
}

for i in range(0, len(selected_features), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(selected_features):
            feature = selected_features[i + j]

            label = label_ranges.get(feature, feature)

            if feature in encoders:
                input_data[feature] = cols[j].selectbox(
                    label,
                    encoders[feature].classes_
                )
            else:
                input_data[feature] = cols[j].number_input(
                    label,
                    value=0.0,
                    step=0.1
                )

# Predict Button
st.markdown("<br>", unsafe_allow_html=True)
col_b1, col_b2, col_b3 = st.columns([2, 1, 2])
with col_b2:
    predict_btn = st.button("🚀 Predict Weather")

# Prediction Logic
if predict_btn:

    df_input = pd.DataFrame([input_data])

    for col, le in encoders.items():
        if col in df_input:
            df_input[col] = le.transform(df_input[col])

    df_input = df_input[selected_features]
    input_scaled = scaler.transform(df_input)

    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]

    predicted_label = encoders["Weather Type"].inverse_transform([prediction])[0]
    weather_types_raw = encoders["Weather Type"].classes_

    confidence = probabilities[prediction] * 100

    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        st.markdown(f"""
        <div class="prediction-card">
            <h2>{predicted_label}</h2>
            <h4>Confidence: {confidence:.2f}%</h4>
        </div>
        """, unsafe_allow_html=True)

    prob_df = pd.DataFrame({
        "Weather Type": weather_types_raw,
        "Probability": probabilities
    })

    fig = px.bar(
        prob_df,
        x="Probability",
        y="Weather Type",
        orientation="h",
        text=prob_df["Probability"].apply(lambda x: f"{x*100:.2f}%"),
        color="Probability",
        color_continuous_scale="Turbo"
    )

    fig.update_layout(
        title=dict(
            text="🌈 Weather Prediction<br>Probability Distribution",
            x=0.5
        ),
        template="plotly_dark",
        xaxis=dict(range=[0, 1]),
        height=420
    )

    col_l2, col_c2, col_r2 = st.columns([1, 2, 1])
    with col_c2:
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.write("---")
st.markdown("""
<div style="text-align:center;font-size:15px;color:#b3b3b3;">
🚀 Created by <b>Tooba Rani</b> — AI Engineer  
<br>
Weather Prediction System | Machine Learning Project
</div>
""", unsafe_allow_html=True)
