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
├── app.py # Flask backend logic <br>
├── columns.json # Feature columns used by the model <br>
├── model.pickle # Trained ML model <br>
├── requirements.txt # Required Python packages <br>
├── templates/ <br>
│ └── index.html # Frontend HTML form <br>
├── static/ <br>
│ └── style.css # Optional: CSS styling (if added) <br>
├── util.py # Helper functions (if any) <br>
└── README.md # This file <br>

---

## 📸 Screenshots


- **🏡 Input Form**  
  ![Input Form]![image](https://github.com/user-attachments/assets/1a8c9e49-7a6e-4e25-9d51-0b7828201d6f)



- **📈 Prediction Output**  
  ![Prediction Output]![image](https://github.com/user-attachments/assets/5137cd10-f834-4c15-8734-7a2364fceab5)


---

## 🚀 How to Use

1. **Clone the repo**  
   ```bash
   git clone https://github.com/blah-bleh-hmm/housing-price-predictor
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
4. **Open your browser and go to**
   ```
   http://localhost:5000
   ```

---

## 📌 Note
This project is for educational and portfolio purposes only.
The dataset used was limited, and the model is not intended for real-world property valuation.

## 👩‍💻 Author

Made with ❤️ by [blah-bleh-hmm](https://github.com/blah-bleh-hmm)






