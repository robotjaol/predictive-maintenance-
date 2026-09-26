"""
Streamlit dashboard for predictive maintenance monitoring.

Run with: streamlit run dashboard/app.py

Reads the sensor data and shows summary stats. Run notebooks 01 through 03
first for the model to be available for live checks.
"""
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Predictive Maintenance Dashboard", layout="wide")
st.title("Predictive Maintenance Dashboard")

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "sensor_data.csv")

if not os.path.exists(DATA_PATH):
    st.warning("No sensor data found. Run notebooks/01_generate_data.ipynb first.")
else:
    sensor_data = pd.read_csv(DATA_PATH)
    failure_rate = sensor_data["machine_failure"].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Readings", f"{len(sensor_data):,}")
    col2.metric("Failure Rate", f"{failure_rate:.1%}")
    col3.metric("Average Tool Wear", f"{sensor_data['tool_wear_min'].mean():.0f} min")

    st.subheader("Tool Wear Distribution")
    st.bar_chart(sensor_data["tool_wear_min"].value_counts(bins=20).sort_index())

    st.subheader("Average Sensor Values by Failure Status")
    summary = sensor_data.groupby("machine_failure").mean(numeric_only=True)
    st.dataframe(summary.round(2))

st.subheader("Check Risk for a New Reading")
with st.form("risk_form"):
    air_temp = st.number_input("Air Temperature (K)", value=300.0)
    process_temp = st.number_input("Process Temperature (K)", value=310.0)
    rotational_speed = st.number_input("Rotational Speed (rpm)", value=1500.0)
    torque = st.number_input("Torque (Nm)", value=40.0)
    tool_wear = st.number_input("Tool Wear (min)", value=100.0)
    submitted = st.form_submit_button("Check Risk")

if submitted:
    st.info("Send this form data to the /predict endpoint in src/api.py to get a live prediction.")
