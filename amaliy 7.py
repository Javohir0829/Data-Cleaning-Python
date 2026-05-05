import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


data = {
    'Yurgan_Masofa': [10, 50, 100, 20, 80, 150, 30, 200, 45, 120],
    'Yili': [2023, 2020, 2018, 2022, 2019, 2015, 2021, 2010, 2021, 2017],
    'Narxi': [25000, 18000, 12000, 23000, 15000, 8000, 21000, 5000, 19500, 10000]
}
df = pd.DataFrame(data)

X = df[['Yurgan_Masofa', 'Yili']]
y = df['Narxi']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)

print(f"Bashorat qilingan narxlar: {y_pred}")
print(f"O'rtacha kvadratik xatolik (MSE): {mse}")