#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 15:02:23 2025
@author: ernestmugambi
"""
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings('ignore')

# get first dataset
trn_data_1 = pd.read_csv('original_train_set.csv')
trn_data_1 = trn_data_1.reset_index(drop=True)
trn_data_2 = pd.read_csv('new_url_features.csv')
trn_data_2 = trn_data_2.reset_index(drop=True)
# get 
df_list = [trn_data_2] * 8
concatenated_df = pd.concat(df_list)
concatenated_df = concatenated_df.reset_index(drop=True)

all_data = pd.concat([trn_data_1,concatenated_df])
xgb_model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='logloss', use_label_encoder=False)
param_grid = {
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2],
        'n_estimators': [100, 200, 300],
        'subsample': [0.7, 0.9],
        'colsample_bytree': [0.7, 0.9]
    }
grid_search = GridSearchCV(estimator=xgb_model,
                               param_grid=param_grid,
                               scoring='accuracy',  # Or 'roc_auc', 'neg_log_loss', etc.
                               cv=5,
                               n_jobs=-1,  # Use all available CPU cores
                               verbose=1)
y_train = all_data['class']
del all_data['class']
X_train = all_data
grid_search.fit(X_train, y_train)
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")
best_xgb_model = grid_search.best_estimator_
y_test = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]
del trn_data_2['class']
X_test = trn_data_2
test_accuracy = best_xgb_model.score(X_test, y_test)
print(f"Test accuracy of the new retrained model: {test_accuracy}")
new_predictions = best_xgb_model.predict(X_test)
print(f"predictions after retraining: {new_predictions}")
