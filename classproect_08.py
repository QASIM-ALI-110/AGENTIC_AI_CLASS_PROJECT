import streamlit as st

# Simple BMI calculator
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m)", min_value=0.1, step=0.01)

if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")
