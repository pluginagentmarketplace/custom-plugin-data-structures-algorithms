---
name: data-science-fundamentals
description: Machine learning and data science fundamentals including Python, data preprocessing, model development, and evaluation metrics.
---

# Data Science Fundamentals

## Python Data Analysis

### Pandas Basics

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Exploratory Data Analysis
print(df.head())
print(df.info())
print(df.describe())

# Data cleaning
df = df.dropna()  # Remove missing values
df['column'] = df['column'].astype('int64')  # Type conversion

# Filtering
high_value = df[df['price'] > 100]
subset = df[['name', 'price', 'category']]
```

## Machine Learning Pipeline

### Train-Test Split and Model Training

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score

# Prepare data
X = df[['feature1', 'feature2', 'feature3']]
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)

print(f'Accuracy: {accuracy:.2%}')
print(f'Precision: {precision:.2%}')
```

## Deep Learning with TensorFlow

### Simple Neural Network

```python
import tensorflow as tf
from tensorflow import keras

# Build model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy:.2%}')
```

## Data Visualization

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Distribution plot
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='age', hue='gender', bins=30)
plt.title('Age Distribution by Gender')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlations')
plt.show()
```

## Feature Engineering

```python
# Polynomial features
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encoding categorical variables
df = pd.get_dummies(df, columns=['category'], drop_first=True)
```

## Key Concepts

1. **Data Preprocessing**
2. **Feature Engineering**
3. **Model Selection**
4. **Cross-Validation**
5. **Hyperparameter Tuning**
6. **Evaluation Metrics**
7. **Model Deployment**