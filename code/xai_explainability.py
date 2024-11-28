# XAI Explainability: SHAP and LIME Analysis

import shap
import lime
import lime.lime_tabular
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Step 1: Load Scaled Test Data (Assuming you already have scaled data)
scaler = StandardScaler()
X_test_scaled = scaler.fit_transform(X_test)  # Fit and transform if scaler is not retained from previous step
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns, index=X_test.index)

# Step 2: SHAP Analysis
explainer = shap.TreeExplainer(rf_model.best_estimator_)
shap_values = explainer.shap_values(X_test_scaled)

if isinstance(shap_values, list):
    shap_values = shap_values[1]  # Assuming the second output represents the positive class

# Plot SHAP Summary
shap.summary_plot(shap_values, X_test_scaled, plot_type="bar")
plt.title("SHAP Feature Importance")
plt.show()

# SHAP Dependence Plot for Top Features
important_features = ['V16', 'V14', 'V12', 'V17']  # Top features determined earlier
for feature in important_features:
    try:
        shap.dependence_plot(feature, shap_values, X_test_scaled, interaction_index='auto', show=False)
        plt.title(f"SHAP Dependence Plot for Feature: {feature}")
        plt.show()
    except (IndexError, ValueError) as e:
        print(f"An error occurred while plotting SHAP dependence plot for {feature}: {e}")

# Step 3: LIME Analysis
lime_explainer = lime.lime_tabular.LimeTabularExplainer(X_train_scaled, feature_names=X_train.columns, class_names=['Non-Fraud', 'Fraud'], discretize_continuous=True, random_state=42)

# Generate LIME Explanation for a single instance
instance = X_test_scaled.iloc[0]
explanation = lime_explainer.explain_instance(instance, rf_model.best_estimator_.predict_proba, num_features=10)
explanation.show_in_notebook(show_table=True, show_all=False)
