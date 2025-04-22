import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Load the updated dataset
data = pd.read_csv("pitchease_20_pitchers_dataset.csv")

# Set up Streamlit app
st.set_page_config(page_title="PITCHEASE Dashboard", layout="wide")
st.title("PITCHEASE Dashboard")
st.markdown("Monitor pitcher fatigue and recovery trends in real time.")

# Pitcher selection
selected_pitcher = st.selectbox("Select Pitcher:", data["Pitcher"].unique())
pitcher_data = data[data["Pitcher"] == selected_pitcher].iloc[0]

# Display Key Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("RPE", f"{pitcher_data['RPE']}")
col2.metric("Torque (Nm)", f"{pitcher_data['Torque']}")
col3.metric("HRV (ms)", f"{pitcher_data['HRV']}")
col4.metric("Pitches Thrown", f"{pitcher_data['Pitches_Thrown']}")

# Fatigue Flag
st.subheader("Fatigue Flag")
flag_color = "green" if pitcher_data["Fatigue_Flag"] == "Low" else "orange"
st.markdown(
    f"<div style='font-size:16px; color:{flag_color};'><strong>Status:</strong> {pitcher_data['Fatigue_Flag']}</div>",
    unsafe_allow_html=True
)

# Simulated 7-Day HRV Trend
st.subheader("HRV Trend (Simulated)")
np.random.seed(abs(hash(selected_pitcher)) % 10000)  # Ensure unique trend per pitcher
hrv_trend = np.round(np.random.normal(loc=pitcher_data["HRV"], scale=1.5, size=7), 1)

fig, ax = plt.subplots()
ax.plot(hrv_trend, marker='o', linestyle='-', color='black')
ax.set_title("HRV Over Last 7 Days")
ax.set_xlabel("Day")
ax.set_ylabel("HRV (ms)")
st.pyplot(fig)

# Coach's Note
st.subheader("Coach's Note")
rpe = pitcher_data["RPE"]
hrv = pitcher_data["HRV"]
torque = pitcher_data["Torque"]

if rpe > 7.8 and hrv < 70:
    st.warning("Pitcher is experiencing elevated fatigue and low recovery. Recommend rest or modified session.")
elif torque > 38 and rpe > 7.4:
    st.info("Torque and exertion are high. Monitor closely and reduce bullpen load.")
elif hrv > 72 and rpe < 7.0:
    st.success("Pitcher is well-recovered and performing efficiently. Maintain current training plan.")
else:
    st.write("Recovery is stable, but continue to monitor for changes.")

# PITCHEASE Sleeve Interactive Overview
st.markdown("---")
st.markdown("## 🎯 PITCHEASE Sleeve Sensor Overview")
st.image("assets/interactive_sleeve_base.png", use_container_width=True)

sensor_clicked = st.radio(
    "Select a Sensor Area:",
    ("None", "Elbow (Torque)", "Forearm (RPE)", "Bicep (HRV)"),
    horizontal=True
)

if sensor_clicked == "Elbow (Torque)":
    st.success("**Elbow Torque Sensor**: Measures rotational stress on the ulnar collateral ligament (UCL). High torque over time correlates with increased Tommy John risk.")
elif sensor_clicked == "Forearm (RPE)":
    st.info("**Forearm RPE Sensor**: Tracks Rate of Perceived Exertion. Informs coach of player-reported fatigue levels and workload perception.")
elif sensor_clicked == "Bicep (HRV)":
    st.warning("**Bicep HRV Sensor**: Monitors Heart Rate Variability. Lower HRV scores after an outing suggest incomplete recovery or fatigue.")
else:
    st.write("Select a sensor to learn more.")





