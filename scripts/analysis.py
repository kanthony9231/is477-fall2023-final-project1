import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

wine_data = pd.read_csv('data/wine.data', header=None)

feature_names = [
    "Class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
    "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
    "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"
]
wine_data.columns = feature_names

summary_statistics = wine_data.describe()
summary_statistics.to_csv('results/summary_statistics.csv')

X = wine_data[['Flavanoids']]
y = wine_data['Alcohol']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_regression_model = LinearRegression()
linear_regression_model.fit(X_train, y_train)
y_pred = linear_regression_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
with open('results/mean_squared_error.txt', 'w') as mse_file:
    mse_file.write(f'Mean Squared Error: {mse}')

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='black', label='Actual')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Predicted')
plt.title('Linear Regression: Flavanoids vs Alcohol Content')
plt.xlabel('Flavanoids')
plt.ylabel('Alcohol')
plt.legend()
plt.savefig('results/linear_regression_plot.png')
