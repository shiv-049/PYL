# ASSIGNMENT A04 - Scikit-learn Functions

# 1. LOAD DATASET
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("First 5 rows:\n", X[:5])


# 2. SPLIT DATASET
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

print("\nTraining shape:", X_train.shape)
print("Testing shape:", X_test.shape)


# 3. TRAIN MODEL (KNN)
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("\nAccuracy:", metrics.accuracy_score(y_test, y_pred))


# 4. SAMPLE PREDICTION
sample = [[5, 5, 3, 2], [2, 4, 3, 5]]
preds = model.predict(sample)

pred_species = [iris.target_names[p] for p in preds]
print("Predictions:", pred_species)


# 5. MODEL PERSISTENCE (SAVE & LOAD)
import joblib

joblib.dump(model, "iris_model.joblib")
loaded_model = joblib.load("iris_model.joblib")

print("\nModel saved and loaded successfully")


# 6. PREPROCESSING - MEAN REMOVAL
import numpy as np
from sklearn import preprocessing

input_data = np.array([
    [2.1, -1.9, 5.5],
    [-1.5, 2.4, 3.5],
    [0.5, -7.9, 5.6],
    [5.9, 2.3, -5.8]
])

print("\nMean =", input_data.mean(axis=0))
print("Std Dev =", input_data.std(axis=0))

scaled_data = preprocessing.scale(input_data)

print("After Mean Removal Mean =", scaled_data.mean(axis=0))
print("After Mean Removal Std Dev =", scaled_data.std(axis=0))


# 7. PREPROCESSING - MINMAX SCALING
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
scaled_minmax = scaler.fit_transform(input_data)

print("\nMin-Max Scaled Data:\n", scaled_minmax)

print("\n----- PROGRAM COMPLETED -----")
