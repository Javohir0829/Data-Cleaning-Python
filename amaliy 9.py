import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# 1. Ma'lumotlarni yuklash
iris = load_iris()

# Xatoliklarni chetlab o'tish uchun lug'at ko'rinishida murojaat qilamiz
X = iris['data'] 
y = iris['target']

# 2. Ma'lumotlarni o'qitish va test to'plamlariga bo'lish (70/30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)[cite: 7]

# 3. Algoritmlar ro'yxati
models = {
    "K-NN (3-qo'shni)": KNeighborsClassifier(n_neighbors=3),[cite: 7]
    "Logistik Regressiya": LogisticRegression(max_iter=200),[cite: 7]
    "SVM (Chiziqli)": SVC(kernel='linear'),[cite: 7]
    "Qaror daraxti": DecisionTreeClassifier(),[cite: 7]
    "Random Forest": RandomForestClassifier(n_estimators=100)[cite: 7]
}

print("--- Sinflashtirish natijalari ---")

# 4. Har bir modelni sikl yordamida tekshirish
for name, model in models.items():
    # Modelni o'qitish
    model.fit(X_train, y_train)[cite: 7]
    
    # Bashorat qilish
    y_pred = model.predict(X_test)[cite: 7]
    
    # Aniqlikni hisoblash
    accuracy = accuracy_score(y_test, y_pred)[cite: 7]
    
    print(f"{name} aniqligi: {accuracy:.2f}")