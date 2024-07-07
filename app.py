import streamlit as st
import pickle
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier as gbc
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the trained model from the pickle file
@st.cache_resource
def load_model(filename):
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    return model

# Function to preprocess user input
def preprocess_input(age, gender, bmi, smoking, genetic_risk, physical_activity, alcohol_intake, cancer_history):
    # Create a DataFrame from user input without an index
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'BMI': [bmi],
        'Smoking': [smoking],
        'GeneticRisk': [genetic_risk],
        'PhysicalActivity': [physical_activity],
        'AlcoholIntake': [alcohol_intake],
        'CancerHistory': [cancer_history]
    }, index=[0])
    return input_data

# Function to predict cancer
def predict_cancer(model, input_data):
    prediction = model.predict(input_data)
    return prediction[0]

def main():
    st.title("Cancer Prediction App")
    st.write("Enter patient details to predict if they have cancer.")

    # Input fields for user to enter patient details
    Age = st.number_input("Age", min_value=1, max_value=150, value=30)
    Gender = st.selectbox("Gender", ["Male", "Female"])
    BMI = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
    Smoking = st.selectbox("Smoking History", ["No", "Yes"])
    GeneticRisk = st.selectbox("Genetic Risk Level", ["Low", "Medium", "High"])
    PhysicalActivity = st.number_input("Physical Activity (hours/week)", min_value=0.0, max_value=20.0, value=2.0)
    AlcoholIntake = st.number_input("Alcohol Intake (units/week)", min_value=0.0, max_value=50.0, value=5.0)
    CancerHistory = st.selectbox("Cancer History", ["No", "Yes"])

    # Convert categorical inputs to numerical
    Gender = 1 if Gender == "Male" else 0
    Smoking = 1 if Smoking == "Yes" else 0
    CancerHistory = 1 if CancerHistory == "Yes" else 0  # Convert CancerHistory to numerical
    if GeneticRisk == "Low":
        GeneticRisk = 0
    elif GeneticRisk == "Medium":
        GeneticRisk = 1
    else:
        GeneticRisk = 2

    # When the user clicks the predict button
    if st.button("Predict"):
        # Load the model
        model = load_model("gbc_model.pkl")

        # Preprocess input data
        input_data = preprocess_input(Age, Gender, BMI, Smoking, GeneticRisk, PhysicalActivity, AlcoholIntake, CancerHistory)

        # Predict
        prediction = predict_cancer(model, input_data)

        # Display prediction
        if prediction == 1:
            st.error("Patient is predicted to have cancer.")
        else:
            st.success("Patient is predicted to not have cancer.")

if __name__ == "__main__":
    main()
