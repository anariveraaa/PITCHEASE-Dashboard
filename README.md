## ⚾ Overview

**PITCHEASE** is a performance-enhancing wearable and dashboard system designed to help coaches and athletic staff at the collegiate level better monitor pitcher workload, recovery, and injury risk.

The system includes:
- A **compression sleeve** embedded with sensors that track physiological and biomechanical stress
- An **interactive Streamlit dashboard** that interprets fatigue data in real time
- A backend system built on sports science models to simulate **RPE**, **HRV**, and **torque**

Together, these tools allow teams to make smarter training and game-day decisions — with the ultimate goal of improving performance, reducing injury, and winning more games.

# PITCHEASE Dashboard

🔗 [Click here to launch the live dashboard](https://anariveraaa-pitchease-dashboard.streamlit.app)

An interactive fatigue monitoring dashboard for NCAA pitchers powered by **PITCHEASE**.

---

## 🎯 Project Goals

- Prevent overuse and injury (especially UCL stress leading to Tommy John surgeries)
- Provide coaches with **practical, visual tools** to monitor fatigue
- Move from guesswork to **data-informed training management**
- Simulate a future-ready athlete monitoring solution for elite baseball programs

---

## 📊 What the Dashboard Shows

- **Real-time metrics** from the wearable:
  - Elbow Torque (Nm)
  - Heart Rate Variability (HRV in ms)
  - Rate of Perceived Exertion (RPE)
  - Pitches Thrown
- **Fatigue Flag** status (Low or Moderate)
- **7-Day HRV Trend Graph** for each pitcher
- **Dynamic coaching recommendations** based on the data

The dashboard is built using [Streamlit](https://streamlit.io/), [Pandas](https://pandas.pydata.org/), and [Matplotlib](https://matplotlib.org/).

---

## 🧠 How the Fatigue Data is Modeled

PITCHEASE doesn’t use arbitrary numbers — it simulates real physiological indicators based on pitcher workload:

```python
RPE = 6.5 + (Pitches_Per_Inning * 0.05) + (BB_per_9 * 0.15)
HRV = 78 - (Pitches_Per_Inning * 0.3) - (BB_per_9 * 0.7)
Torque = 30 + (K_per_9 * 0.5) + (BB_per_9 * 0.4)
