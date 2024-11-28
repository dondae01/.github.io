# XAI Model: Building, Training, and Evaluating the RandomForest Model

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score

# Step 1: Load Dataset
df = pd.read_csv('creditcard.csv')

# Step 2: Data Preprocessing
X = df.drop(columns=['Class'])
y = df['Class']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Step 3: Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 4: Model Training - RandomForestClassifier
param_grid = {
    'n_estimators': [100, 150, 200],
    'max_depth': [10, 15, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

rf_model = RandomizedSearchCV(RandomForestClassifier(random_state=42), param_grid, n_iter=5, cv=3, n_jobs=-1, verbose=2, random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Step 5: Model Evaluation
y_pred = rf_model.best_estimator_.predict(X_test_scaled)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, rf_model.best_estimator_.predict_proba(X_test_scaled)[:, 1]))
