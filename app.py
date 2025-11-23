import streamlit as st
import calculator  # MUST match actual filename

st.title("🧮 Simple Calculator")

operation = st.selectbox(
    "Choose Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

if st.button("Calculate"):
    if operation == "Add":
        result = calculator.add(num1, num2)
    elif operation == "Subtract":
        result = calculator.subtract(num1, num2)
    elif operation == "Multiply":
        result = calculator.multiply(num1, num2)
    elif operation == "Divide":
        result = calculator.divide(num1, num2)

    st.success(f"Result = {result}")
