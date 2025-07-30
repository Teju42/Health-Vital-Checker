import pandas as pd
import streamlit as st


# Custom CSS for background and styling
st.markdown("""
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1588776814546-ec7bd5bdfa3e');
        background-size: cover;
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 10px;
    }
    .title-style {
        text-align: center;
        color: #023047;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 class='title-style'>🩺Fit Check: One Tap, Total Check </h1>", unsafe_allow_html=True)
st.markdown("### 📋 Enter your basic health vitals below:")

# 🧾 Get user input
def get_user_input():
    age = st.number_input("👤 Age", 0, 120, step=1)
    bp = st.number_input("💓 Blood Pressure (Systolic)", 60, 200)
    sugar = st.number_input("🍬 Blood Sugar Level (mg/dL)", 50, 400)
    hr = st.number_input("❤️ Heart Rate (bpm)", 30, 200)
    temp = st.number_input("🌡️ Body Temperature (°C)", 30.0, 45.0)
    return age, bp, sugar, hr, temp

# ⚠️ Analyze vitals
def analyze_vitals(bp, sugar, hr, temp):
    alerts = []
    status = []

    # Blood Pressure
    if bp < 70 or bp > 120:
        alerts.append("⚠️ Abnormal Blood Pressure | (Normal: 70–120 mmHg)")

    
    # Blood Sugar
    if 70 <= bp <= 120:
        status.append("Blood Pressure is normal ✅")
    else:
        status.append("Blood Pressure is out of range ⚠️")

    
    # Heart Rate
    if hr < 60 or hr > 100:
        alerts.append("⚠️ Abnormal Heart Rate | (Normal: 60–100 bpm)")
    
    # Body Temperature
    if temp < 35 or temp > 37.2:
        alerts.append("⚠️ Abnormal Body Temperature | (Normal: 35–37.2°C)")

    return alerts

# Save log
def log_result(age, bp, sugar, hr, temp, result):
    # Strip emojis and leave only the plain text for CSV
    import re
    clean_result = re.sub(r'[^\x00-\x7F]+', '', result)  # Remove emojis
    clean_result = clean_result.replace("✅", "").replace("⚠️", "").strip()

    with open("patient_log.csv", "a", encoding="utf-8") as f:
        f.write(f"{age},{bp},{sugar},{hr},{temp},{clean_result}\n")

import os

if not os.path.exists("patient_log.csv"):
    with open("patient_log.csv", "w", encoding="utf-8") as f:
        f.write("Age,BP,Sugar,HR,Temp,Result\n")

# Main App
def main():
    age, bp, sugar, hr, temp = get_user_input()

    if st.button("✅ Run Fit Check"):
        alerts = analyze_vitals(bp, sugar, hr, temp)
        result = " | ".join(alerts) if alerts else "✅ All vitals appear normal. Happy Health To You 🥳🎊"

        if alerts:
            st.error(result)
        else:
            st.success(result)

        log_result(age, bp, sugar, hr, temp, result)

main()
