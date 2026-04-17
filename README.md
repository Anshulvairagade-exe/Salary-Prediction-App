Salary Prediction App - https://machine-learning-models-bkerekspzehdtj3bragr5v.streamlit.app/

A Machine Learning web application that predicts an employee's salary based on their details such as age, gender, education level, job title, and years of experience.

Project Overview

This project uses a Random Forest Regressor model to estimate salaries based on input features. It demonstrates a complete ML pipeline including:

Data preprocessing (handling missing values, encoding)
Model training
Model deployment using a simple web interface
🧠 Features
📊 Predict salary based on employee details
⚡ Fast and accurate predictions using Random Forest
🧹 Handles missing values using mean & mode
🔢 Encodes categorical data for ML compatibility
🌐 Simple UI for easy interaction
🛠️ Tech Stack
Python 🐍
Pandas & NumPy
Scikit-learn
Flask (for web app)
📂 Project Structure
.
├── app.py                              # Main Flask application
├── random_forest_regressor_model.pkl   # Trained ML model
├── requirements.txt                    # Dependencies
└── README.md                           # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
▶️ Run the Application
python app.py

📥 Input Features
Age
Gender
Education Level
Job Title
Years of Experience
📤 Output
Predicted Salary 💰
🧩 Model Details
Algorithm: Random Forest Regressor
Handles both numerical and categorical data
Provides better accuracy by combining multiple decision trees
📌 Future Improvements
Add more features (location, company size, skills)
Improve UI/UX
Deploy on cloud (AWS / Render / Vercel)
Use advanced models (XGBoost, Deep Learning)
👨‍💻 Author

Anshul Vairagade
🔗 Portfolio: https://anshulvairagade.dev/

⭐ Contributing

Feel free to fork this repo and improve it!

📜 License

This project is open-source and available under the MIT License.
