Salary Prediction App

Live Demo
https://machine-learning-models-bkerekspzehdtj3bragr5v.streamlit.app/

Description

This project is a Machine Learning web application that predicts an employee's salary based on input features such as age, gender, education level, job title, and years of experience.

It demonstrates an end-to-end machine learning workflow including data preprocessing, model training, and deployment through a web interface.

Project Overview

The application uses a Random Forest Regressor model to estimate salaries. The workflow includes:

Data preprocessing (handling missing values and encoding categorical features)
Model training using supervised learning
Deployment via a web-based interface
Features
Predicts salary based on user input
Uses Random Forest for improved accuracy
Handles missing values using mean and mode
Encodes categorical variables for model compatibility
Provides a simple and interactive user interface
Tech Stack
Python
Pandas
NumPy
Scikit-learn
Streamlit
Project Structure
.
├── app.py
├── random_forest_regressor_model.pkl
├── requirements.txt
└── README.md
Installation and Setup
Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
Install dependencies
pip install -r requirements.txt
Run the Application

If using Streamlit:

streamlit run app.py

If using Flask:

python app.py
Input Features
Age
Gender
Education Level
Job Title
Years of Experience
Output
Predicted Salary
Model Details
Algorithm: Random Forest Regressor
Handles both numerical and categorical features
Improves prediction accuracy using ensemble learning
Future Improvements
Add more features such as location, skills, and company size
Enhance user interface and experience
Deploy using cloud platforms like AWS or Render
Experiment with advanced models such as XGBoost or deep learning
Author

Anshul Vairagade
Portfolio: https://anshulvairagade.dev/

Contributing

Contributions are welcome. Feel free to fork the repository and submit a pull request.

License

This project is open source and available under the MIT License.
