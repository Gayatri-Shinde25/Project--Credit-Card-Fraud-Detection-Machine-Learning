import streamlit as st
import pickle
import numpy as np

# Load the model
with open('C:/Users/a/Downloads/Credit Card Fraud/LR.pkl', 'rb') as f:
    clf = pickle.load(f)

# Set the page configuration
st.set_page_config(page_title="Fraud Analysis", layout="wide")

# Custom CSS to change background and text color
st.markdown("""
<style>
body {
    background-color: black;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("Fraud Analysis")

# Input fields for the form
input_values = {}
for i in range(1, 30):
    input_values[f'V{i}'] = st.text_input(f'V{i}:')

# Button to submit the form
if st.button("Submit"):
    # Collecting input values
    int_features = [float(input_values[f'V{i}']) for i in range(1, 30) if input_values[f'V{i}']]

    if len(int_features) == 29:  # Ensure all inputs are filled
        final_features = [np.array(int_features)]
        prediction = clf.predict(final_features)
        output = round(prediction[0], 2)

        # Display prediction
        if output == 0:
            st.success("Transaction is authentic.")
        else:
            st.error("Transaction is fraudulent.")
    else:
        st.warning("Please fill in all fields.")