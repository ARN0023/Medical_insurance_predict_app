import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

def train_model():
    df = pd.read_csv('data/insurance.csv')
    
    # Preprocessing
    df.replace({'sex': {'male': 0, 'female': 1}}, inplace=True)
    df['sex'] = df['sex'].astype(int)
    df.replace({'smoker': {'yes': 1, 'no': 0}}, inplace=True)
    df['smoker'] = df['smoker'].astype(int)
    df.replace({'region': {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}}, inplace=True)
    df['region'] = df['region'].astype(int)
    
    # Shuffle the DataFrame
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    X = df.drop(columns='charges')
    y = df['charges']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create a Pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('rf', RandomForestRegressor(random_state=42))
    ])
    
    # Define parameter grid for GridSearchCV
    param_grid = {
        'rf__n_estimators': [300],
        'rf__max_depth': [10],
        'rf__min_samples_split': [10],
        'rf__min_samples_leaf': [4],
        'rf__bootstrap': [True]
    }
    
    # Perform GridSearchCV
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    print(f'Best Random Forest Parameters: {grid_search.best_params_}')
    print(f'Best Random Forest Cross-Validation Score: {grid_search.best_score_}')
    
    best_rf = grid_search.best_estimator_
    
    # Save the model
    joblib.dump(best_rf, 'models/rf_model.pkl')

if __name__ == "__main__":
    train_model()
