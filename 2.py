import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import ttk, messagebox


df = pd.read_csv("framingham.csv")
df.drop(['education'], axis=1, inplace=True)
df.rename(columns={'male': 'Sex_male'}, inplace=True)
df.dropna(inplace=True)

X = df[['age', 'Sex_male', 'cigsPerDay', 'totChol', 'sysBP', 'glucose']].values
y = df['TenYearCHD'].values

scaler = preprocessing.StandardScaler().fit(X)
X_scaled = scaler.transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=4)
model = LogisticRegression()
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))

class HeartDiseaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Heart Disease Risk Predictor")
        self.root.geometry("480x460")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.columns = ['age', 'Sex_male', 'cigsPerDay', 'totChol', 'sysBP', 'glucose']
        self.entries = {}

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#1e1e2e", foreground="#ffffff", font=("Segoe UI", 11))
        style.configure("TEntry", padding=5, font=("Segoe UI", 10))
        style.configure("TButton", background="#007acc", foreground="#ffffff", font=("Segoe UI", 10, "bold"))
        style.map("TButton", background=[("active", "#005f99")])

    def create_widgets(self):
        ttk.Label(self.root, text="Heart Disease Risk Predictor", font=("Segoe UI", 16, "bold"), foreground="#fca311").pack(pady=15)

        form_frame = ttk.Frame(self.root)
        form_frame.pack()

        for idx, col in enumerate(self.columns):
            label = ttk.Label(form_frame, text=col)
            label.grid(row=idx, column=0, padx=10, pady=6, sticky='e')
            entry = ttk.Entry(form_frame, width=25)
            entry.grid(row=idx, column=1, padx=10, pady=6)
            self.entries[col] = entry

        ttk.Button(self.root, text="Submit", command=self.predict).pack(pady=15)

        self.accuracy_label = ttk.Label(self.root, text=f"Model Accuracy: {accuracy * 100:.2f}%", foreground="#8be9fd")
        self.accuracy_label.pack()

        self.result_label = ttk.Label(self.root, text="", font=("Segoe UI", 11, "bold"))
        self.result_label.pack(pady=10)

        footer = ttk.Label(self.root, text="Created by Abdelkareem Hossam", font=("Segoe UI", 9), foreground="#888")
        footer.pack(side="bottom", pady=5)

    def predict(self):
        try:
            values = [float(self.entries[col].get()) for col in self.columns]
            values_scaled = scaler.transform([values])
            prediction = model.predict(values_scaled)[0]

            if prediction == 1:
                self.result_label.config(text="⚠️ High Risk of Heart Disease", foreground="red")
                messagebox.showwarning("Risk Prediction", "⚠️ The model predicts a high risk. Please consult a doctor.")
            else:
                self.result_label.config(text="✅ Low Risk of Heart Disease", foreground="green")
                messagebox.showinfo("Risk Prediction", "✅ The model predicts low risk.")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric inputs for all fields.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = HeartDiseaseApp(root)
    root.mainloop()
