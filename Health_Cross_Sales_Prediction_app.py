import streamlit as st
import pickle
import pandas as pd

# Load the trained model
@st.cache_resource
def load_model():
    with open("response_predict.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# Streamlit UI
st.title("🚗 Health Insurance Purchase Prediction")

# User Inputs
Gender = st.selectbox("Select Gender", ["Male", "Female"])
Age = st.number_input("Enter Age", min_value=18, max_value=100, step=1)
Driving_License = st.selectbox("Do you have a Driving License?", ["No (0)", "Yes (1)"])
Region_Code = st.number_input("Enter Region Code", min_value=0.0, step=0.1)
Previously_Insured = st.selectbox("Previously Insured?", ["No (0)", "Yes (1)"])
Vehicle_Age = st.selectbox("Vehicle Age", ["< 1 Year", "1-2 Year", "> 2 Years"])
Vehicle_Damage = st.selectbox("Was the Vehicle Damaged?", ["No (0)", "Yes (1)"])
Annual_Premium = st.number_input("Enter Annual Premium (₹)", min_value=1000.0, step=100.0)
Policy_Sales_Channel = st.number_input("Enter Policy Sales Channel", min_value=0.0, step=1.0)
Vintage = st.number_input("Enter Vintage", min_value=0, step=1)

# Encoding categorical inputs
Gender = 1 if Gender == "Male" else 0
Driving_License = int(Driving_License.split()[1][1])  # Extract numeric value
Previously_Insured = int(Previously_Insured.split()[1][1])  # Extract numeric value
Vehicle_Age = {"< 1 Year": 0, "1-2 Year": 1, "> 2 Years": 2}[Vehicle_Age]
Vehicle_Damage = int(Vehicle_Damage.split()[1][1])  # Extract numeric value

# Create DataFrame for Prediction
input_data = pd.DataFrame({
    "Gender": [Gender],
    "Age": [Age],
    "Driving_License": [Driving_License],
    "Region_Code": [Region_Code],
    "Previously_Insured": [Previously_Insured],
    "Vehicle_Age": [Vehicle_Age],
    "Vehicle_Damage": [Vehicle_Damage],
    "Annual_Premium": [Annual_Premium],
    "Policy_Sales_Channel": [Policy_Sales_Channel],
    "Vintage": [Vintage]
})

# Prediction Button
if st.button("Predict 🚀"):
    prediction = model.predict(input_data)
    result = "✅ Will Purchase Insurance" if prediction[0] == 1 else "❌ Will Not Purchase Insurance"
    st.success(f"**Prediction Result:** {result}")
