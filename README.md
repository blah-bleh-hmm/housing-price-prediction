# 🏠 Housing Price Predictor 🔢

A machine learning-powered web app that predicts housing prices based on user input like square footage, number of bedrooms, and location.  
Built with **Python (Flask)** for the backend and **HTML/CSS** for the frontend.

This project was created to learn full stack development by combining a trained ML model with a working user interface.

---

## 🔍 Features

- 🔸 Trained ML model (Linear Regression or similar)
- 🔸 User-friendly form to input housing features
- 🔸 Real-time price prediction using Flask backend
- 🔸 Clean UI built with HTML + CSS
- 🔸 Dropdown menu for location (populated from model's data)
- 🔸 Basic JavaScript for form validation and interactivity

---

## 💡 What I Learned

- How to integrate ML models with web apps using Flask
- Saving and loading models using `pickle`
- Building dynamic web forms with HTML and Jinja2 templating
- Handling JSON and POST requests in Flask
- Organizing code into backend and frontend structure

---

## 📁 Project Structure

housing-price-predictor/
├── app.py # Flask backend logic
├── columns.json # Feature columns used by the model
├── model.pickle # Trained ML model
├── requirements.txt # Required Python packages
├── templates/
│ └── index.html # Frontend HTML form
├── static/
│ └── style.css # Optional: CSS styling (if added)
├── util.py # Helper functions (if any)
└── README.md # This file

---

## 📸 Screenshots


- **🏡 Input Form**  
  ![Input Form]![image](https://github.com/user-attachments/assets/e4bf6ab0-56aa-49ac-95c6-1128e50d2544)


- **📈 Prediction Output**  
  ![Prediction Output](![image](https://github.com/user-attachments/assets/3ef1e251-2469-4730-b594-11c543300016)
)

---

## 🚀 How to Use

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/housing-price-predictor
   cd housing-price-predictor
   ```
   
2. **Install dependencies**
   (Make sure you have Python 3 installed)
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Flask server**
   ```bash
   python app.py
   ```
4. **Open your browser and go to
   ```
   http://localhost:5000
   ```

---

## 📌 Note
This project is for educational and portfolio purposes only.
The dataset used was limited, and the model is not intended for real-world property valuation.

## 👩‍💻 Author

Made with ❤️ by [blah-bleh-hmm](https://github.com/blah-bleh-hmm)






