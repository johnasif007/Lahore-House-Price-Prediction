# Lahore House Price Predictor 🏠

A Full-Stack Data Science project that predicts residential property prices in Lahore, Pakistan.

## 📊 Model Performance
- **Accuracy**: 91.45%
- **Algorithm**: Linear Regression
- **Dataset**: Lahore Real Estate Data (Scraped/Cleaned)

## ✨ Key Features
- **Unit Specific**: Unlike standard models, this is tailored for the local market using **Marla** as the area unit.
- **Dynamic Locations**: Predicts prices for over 90+ locations including DHA, Bahria Town, and Gulberg.
- **Full Stack**: Includes a Python Flask backend and a custom HTML/CSS/JS frontend.

## 🛠️ Technology Stack
- **Python** (Pandas, Numpy, Scikit-learn)
- **Flask** (Backend API)
- **JavaScript/jQuery** (Frontend logic)
- **HTML5/CSS3** (UI Design)

## 📂 Project Structure
- `/model`: Jupyter Notebook and data cleaning steps.
- `/server`: Flask server files and `util.py`.
- `/server/artifacts`: Saved `.pickle` model and `columns.json`.
- `/server/static & /server/templates`: Webpage UI files.