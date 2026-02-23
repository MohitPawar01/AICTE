import streamlit as st

st.title(" Basic Calculator")


num1 = st.number_input("Enter First Number", step=1)
num2 = st.number_input("Enter Second Number", step=1)

operation = st.selectbox(
    "Select Operation",
    ["Add", "Sub", "Mult", "Div"]
)

if st.button("Calculate"):

    if operation == "Add":
        result = num1 + num2

    elif operation == "Sub":
        result = num1 - num2

    elif operation == "Mult":
        result = num1 * num2

    elif operation == "Div":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    st.success(f"Result: {result}")