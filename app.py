import streamlit as st
import pandas as pd
import pickle
import numpy as np
from datetime import datetime

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Salary Predictor Pro",
    page_icon="💼",
    layout="wide"
)

# -------------------- LOAD MODEL --------------------
model_filename = 'random_forest_regressor_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# -------------------- MAPPINGS --------------------
gender_options = {'Male': 1, 'Female': 0}

education_options = {
    "Bachelor's Degree": 0,
    "Master's Degree": 3,
    "PhD": 5,
    "High School": 2,
    "Associate's Degree": 1,
    "Some College": 6
}

job_title_options = {
    'Software Engineer': 177,
    'Data Analyst': 18,
    'Senior Manager': 145,
    'Sales Associate': 116,
    'Director': 26,
    'Marketing Manager': 97,
    'Sales Executive': 118,
    'Director of Marketing': 27,
    'Financial Manager': 50,
    'Software Engineer Manager': 178
}

# -------------------- SESSION STATE --------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------- SIDEBAR --------------------
st.sidebar.title("⚙️ Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 History", "ℹ️ About"])

st.sidebar.markdown("---")
st.sidebar.info("💡 Built with Random Forest Model")

# -------------------- HOME PAGE --------------------
if page == "🏠 Home":

    st.title("💼 Salary Prediction Pro")
    st.markdown("### Enter employee details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider('Age', 18, 65, 30)
        experience = st.slider('Experience (Years)', 0, 40, 5)
        gender = st.selectbox('Gender', list(gender_options.keys()))

    with col2:
        education = st.selectbox('Education', list(education_options.keys()))
        job_title = st.selectbox('Job Title', list(job_title_options.keys()))

    st.markdown("---")

    # -------------------- PREDICT --------------------
    if st.button("🚀 Predict Salary", use_container_width=True):

        input_data = pd.DataFrame({
            'Age': [age],
            'Gender': [gender_options[gender]],
            'Education Level': [education_options[education]],
            'Job Title': [job_title_options[job_title]],
            'Years of Experience': [experience]
        })

        prediction = model.predict(input_data)[0]

        # Save to history
        record = {
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Age": age,
            "Gender": gender,
            "Education": education,
            "Job Title": job_title,
            "Experience": experience,
            "Salary": round(prediction, 2)
        }

        st.session_state.history.append(record)

        # -------------------- OUTPUT --------------------
        st.success(f"💰 Predicted Salary: ${prediction:,.2f}")

        colA, colB, colC = st.columns(3)

        colA.metric("Experience", f"{experience} yrs")
        colB.metric("Age", age)
        colC.metric("Prediction", f"${prediction:,.0f}")

# -------------------- HISTORY PAGE --------------------
elif page == "📊 History":

    st.title("📊 Prediction History")

    if len(st.session_state.history) == 0:
        st.warning("No predictions yet!")
    else:
        df = pd.DataFrame(st.session_state.history)

        st.dataframe(df, use_container_width=True)

        st.markdown("### 📈 Salary Trends")
        st.line_chart(df["Salary"])

        # Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download History",
            data=csv,
            file_name="salary_history.csv",
            mime="text/csv"
        )

        # Clear history
        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.success("History cleared!")

# -------------------- ABOUT PAGE --------------------
elif page == "ℹ️ About":

    st.title("ℹ️ About This App")

    st.markdown("""
    ### 💡 Salary Prediction Pro

    This app uses a **Random Forest Regressor** to estimate salaries based on:

    - Age
    - Gender
    - Education
    - Job Title
    - Experience

    ### 🚀 Features
    - Real-time predictions
    - Prediction history tracking
    - Download results
    - Interactive UI

    ### ⚠️ Note
    Predictions depend on training data quality.
    """)