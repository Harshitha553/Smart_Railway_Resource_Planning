# app.py

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from scheduler import load_data, allocate_platforms
from conflict_detector import detect_conflicts
from optimizer import calculate_platform_utilization, delay_statistics

st.title("🚆 Smart Railway Resource Planning System")

uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Original Dataset")
    st.dataframe(df.head())

    # Platform Optimization
    df = allocate_platforms(df)

    st.subheader("Optimized Platform Allocation")
    st.dataframe(df[["Train_ID", "Arrival_Time_Min",
                     "Departure_Time_Min", "Optimized_Platform"]].head())

    # Conflict Detection
    conflicts = detect_conflicts(df)

    st.subheader("Conflict Detection")
    if conflicts:
        st.error(f"{len(conflicts)} Conflicts Detected")
    else:
        st.success("No Conflicts Found")

    # Platform Utilization
    utilization = calculate_platform_utilization(df)

    st.subheader("Platform Utilization (%)")
    st.write(utilization)

    # Plot Utilization
    fig = plt.figure()
    plt.bar(utilization.keys(), utilization.values())
    plt.xlabel("Platform")
    plt.ylabel("Utilization %")
    st.pyplot(fig)

    # Delay Statistics
    stats = delay_statistics(df)
    st.subheader("Delay Statistics")
    st.write(stats)

    # Delay Prediction (Optional)
    try:
        model = joblib.load("models/delay_model.pkl")

        st.subheader("Predict Delay")

        prev_delay = st.number_input("Previous Delay", 0, 60, 5)
        peak = st.selectbox("Peak Hour", [0, 1])
        weather = st.selectbox("Weather", ["Clear", "Rain", "Fog"])

        weather_map = {"Clear": 0, "Rain": 1, "Fog": 2}

        input_data = pd.DataFrame(
            [[prev_delay, peak, weather_map[weather]]],
            columns=["Previous_Delay_Min", "Peak_Hour", "Weather"]
        )

        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Delay: {round(prediction, 2)} minutes")

    except:
        st.info("ML Model not found. Add delay_model.pkl inside models/")