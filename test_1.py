import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

disease_df = pd.read_csv("framingham.csv")
disease_df.drop(['education'], axis=1, inplace=True)
disease_df.rename(columns={'male': 'Sex_male'}, inplace=True)
disease_df.dropna(axis=0, inplace=True)

X = np.asarray(disease_df[['age', 'Sex_male', 'cigsPerDay', 
                           'totChol', 'sysBP', 'glucose']])
y = np.asarray(disease_df['TenYearCHD'])

scaler = preprocessing.StandardScaler().fit(X)
X = scaler.transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=4)


logreg = LogisticRegression()
logreg.fit(X_train, y_train)

columns = ['age', 'Sex_male', 'cigsPerDay', 'totChol', 'sysBP', 'glucose']

def submit():
    try:
        values = [float(entries[col].get()) for col in columns]
        values_scaled = scaler.transform([values]) 
        pred = logreg.predict(values_scaled)
        messagebox.showinfo("Prediction", f"Predicted TenYearCHD: {int(pred[0])}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

y_pred = logreg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

root = tk.Tk()
root.title("Heart Disease Prediction")
root.geometry("400x300")


entries = {}

for idx, col in enumerate(columns):
    label = ttk.Label(root, text=col)
    label.grid(row=idx, column=0, padx=5, pady=5, sticky='e')
    entry = ttk.Entry(root)
    entry.grid(row=idx, column=1, padx=5, pady=5)
    entries[col] = entry

submit_btn = ttk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=len(columns), column=0, columnspan=2, pady=10)
accuracy_label = ttk.Label(root, text=f"Model Accuracy: {accuracy*100:.2f}%")
accuracy_label.grid(row=len(columns)+1, column=0, columnspan=2, pady=5)


root.mainloop()
