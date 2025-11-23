import streamlit as st
import calculator

st.title("📘 Simple Calculator")

choice = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

a = st.number_input("Enter first number", value=0.0)
b = st.number_input("Enter second number", value=0.0)

if st.button("Calculate"):
    if choice == "Add":
        result = calculator.add(a, b)
    elif choice == "Subtract":
        result = calculator.subtract(a, b)
    elif choice == "Multiply":
        result = calculator.multiply(a, b)
    elif choice == "Divide":
        result = calculator.divide(a, b)

    st.success(f"Result = {result}")
