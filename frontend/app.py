import streamlit as st
import numpy as np
import pickle

# frontend/app.py
with open('iris_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    st.session_state.model = model
st.title("🌸 Iris Flower Classifier")
st.markdown("Enter the flower measurements to classify the species.")

# Function to convert input to float
def get_input(label, default):
    value = st.text_input(label, value=str(default))
    try:
        return float(value)
    except ValueError:
        st.warning(f"⚠️ Please enter a valid number for {label}")
        return None

# Inputs
sepal_length = get_input("Sepal Length (cm)", 5.8)
sepal_width = get_input("Sepal Width (cm)", 3.0)
petal_length = get_input("Petal Length (cm)", 4.0)
petal_width = get_input("Petal Width (cm)", 1.2)

# Predict button
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    st.success(f"The predicted species is: **{prediction}**")