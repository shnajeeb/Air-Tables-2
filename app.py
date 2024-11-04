import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Input from the user
user_input = st.text_input("Enter some text:")

# Displaying the input back to the user
if user_input:
    st.write(f"You entered: {user_input}")

# A simple slider
number = st.slider("Select a number", 0, 100, 50)
st.write(f"You selected: {number}")

# Button that performs an action
if st.button("Click me!"):
    st.write("Button clicked!")

# A line chart
st.line_chart([1, 2, 3, 4, 5])
