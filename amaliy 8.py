import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline

np.random.seed(42)
X = 10 * np.random.rand(100, 1)
y = 0.5 * X**3 - 2 * X**2 + X + np.random.normal(0, 10, X.shape) # y = 0.5x^3 - 2x^2 + x + epsilon
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

degree = 3
poly_model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
poly_model.fit(X_train, y_train)
lasso_model = make_pipeline(PolynomialFeatures(degree), Lasso(alpha=0.1)) # L1 Regulyarizatsiya
ridge_model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=0.1)) # L2 Regulyarizatsiya

lasso_model.fit(X_train, y_train)
ridge_model.fit(X_train, y_train)

y_pred = poly_model.predict(X_test)
print(f"MSE: {mean_squared_error(y_test, y_pred)}")
print(f"R2 Score: {r2_score(y_test, y_pred)}")

# 6. Vizualizatsiya
plt.scatter(X, y, color='red', label='Asl ma\'lumotlar', alpha=0.5)
X_seq = np.linspace(0, 10, 100).reshape(-1, 1)
plt.plot(X_seq, poly_model.predict(X_seq), color='blue', label='Polinomial Bashorat')
plt.title('Polinomial Regressiya Modeli')
plt.legend()
plt.show()