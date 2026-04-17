
import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load the trained model
model_filename = 'random_forest_regressor_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# --- Hardcoded Mappings from training --- 
# In a real application, you'd save these encoders or their mappings during training
# and load them here. For this example, we infer them from the known data.
gender_options = {'Male': 1, 'Female': 0}

# These mappings would ideally be saved and loaded, or recreated based on all unique values
# encountered during training. For demonstration, we use common values and assume consistency.
# For a more robust solution, the LabelEncoder objects themselves should be pickled.
education_options = {
    'Bachelor\'s Degree': 0, 'Master\'s Degree': 3, 'PhD': 5, 
    'High School': 2, 'Associate\'s Degree': 1, 'Some College': 6
} # Add more as per your training data's unique values

job_title_options = {
    'Software Engineer': 177, 'Data Analyst': 18, 'Senior Manager': 145, 
    'Sales Associate': 116, 'Director': 26, 'Marketing Manager': 97, 
    'Sales Executive': 118, 'Director of Marketing': 27, 'Financial Manager': 50,
    'Software Engineer Manager': 178 # Add more as per your training data's unique values
} 
# Note: This list is incomplete and should contain ALL unique job titles from your training data.
# If a job title not in this list is selected, the app will not encode it correctly.

# Streamlit App Title
st.title('Salary Prediction App')

st.write("Enter the employee's details to predict their salary.")

# Input Features
age = st.slider('Age', min_value=18, max_value=65, value=30)
years_of_experience = st.slider('Years of Experience', min_value=0, max_value=40, value=5)

gender_display = st.selectbox('Gender', options=list(gender_options.keys()))
education_display = st.selectbox('Education Level', options=list(education_options.keys()))
job_title_display = st.selectbox('Job Title', options=list(job_title_options.keys()))

# Encode categorical inputs using the hardcoded mappings
gender_encoded = gender_options[gender_display]
education_encoded = education_options[education_display]
job_title_encoded = job_title_options[job_title_display]

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [gender_encoded],
    'Education Level': [education_encoded],
    'Job Title': [job_title_encoded],
    'Years of Experience': [years_of_experience]
})

# Predict button
if st.button('Predict Salary'):
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Salary: ${prediction:,.2f}')
