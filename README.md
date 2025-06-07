# 🫀 Heart Disease Risk Predictor (GUI App)

A modern GUI-based machine learning application that predicts the **10-year risk of coronary heart disease (CHD)** using **logistic regression** trained on the **Framingham Heart Study** dataset.

> ✨ Inspired by: [GeeksforGeeks - Heart Disease Prediction using Logistic Regression](https://www.geeksforgeeks.org/ml-heart-disease-prediction-using-logistic-regression/)

---

## 📊 Project Overview

This project builds a machine learning model using `scikit-learn` and presents it via a stylish desktop application using `Tkinter`.  
It allows users to input clinical data and get an immediate prediction about their heart disease risk.

The app:
- Trains a logistic regression model
- Scales input features using standardization
- Accepts new patient data through a user-friendly GUI
- Predicts heart disease likelihood in real-time
- Displays the model’s accuracy

---

## 🧠 Dataset & Features

- **Dataset**: [Framingham Heart Study Dataset](https://www.kaggle.com/datasets/amanajmera1/framingham-heart-study-dataset)
- **Target variable**: `TenYearCHD`
- **Selected features**:
  - `age`
  - `Sex_male` (0 = female, 1 = male)
  - `cigsPerDay`
  - `totChol`
  - `sysBP`
  - `glucose`

---

## 🛠️ Technologies Used

- Python
- pandas
- numpy
- scikit-learn
- tkinter (GUI)
- ttk (themed widgets)

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/heart-disease-predictor.git
cd heart-disease-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pandas numpy scikit-learn
```

### 3. Run the app

```bash
python app.py
```

---

## 📁 Project Structure

```
📦 heart-disease-predictor
├── framingham.csv         # Dataset (must be present)
├── app.py                 # Main application script
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## 📷 GUI Preview

> _You can add a screenshot of the app window here_

---

## ✅ Features

- ✔️ Logistic Regression Model
- ✔️ StandardScaler for feature normalization
- ✔️ Sleek GUI using `ttk`
- ✔️ Real-time prediction from user input
- ✔️ Model accuracy displayed
- ✔️ Exception handling for invalid inputs

---

## 📌 Acknowledgements

- Thanks to [GeeksforGeeks](https://www.geeksforgeeks.org/ml-heart-disease-prediction-using-logistic-regression/) for the foundational tutorial
- Dataset sourced from [Kaggle](https://www.kaggle.com/datasets/amanajmera1/framingham-heart-study-dataset)

---

## 👨‍💻 Author

**Abdelkareem Hossam**  
📧 [abdelkareemh55@gmail.com](mailto:abdelkareemh55@gmail.com)  
🔗 [GitHub](https://github.com/kilofrakh) | [LinkedIn](https://www.linkedin.com/in/abdelkareem-hossam-862a07240/)

---

## 📜 License

This project is licensed under the MIT License.
