import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def evaluate_model():
    df = pd.read_csv('data/insurance.csv')
    
    # Preprocessing
    df.replace({'sex': {'male': 0, 'female': 1}}, inplace=True)
    df['sex'] = df['sex'].astype(int)
    df.replace({'smoker': {'yes': 1, 'no': 0}}, inplace=True)
    df['smoker'] = df['smoker'].astype(int)
    df.replace({'region': {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}}, inplace=True)
    df['region'] = df['region'].astype(int)
    
    X = df.drop(columns='charges')
    y = df['charges']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Load the model
    best_rf = joblib.load('models/rf_model.pkl')
    
    # Make predictions
    train_pred = best_rf.predict(X_train)  # Use original X_train since scaling is part of the pipeline
    test_pred = best_rf.predict(X_test)    # Use original X_test since scaling is part of the pipeline
    
    # Evaluate the model
    r2_train = r2_score(y_train, train_pred)
    r2_test = r2_score(y_test, test_pred)
    mae_train = mean_absolute_error(y_train, train_pred)
    mae_test = mean_absolute_error(y_test, test_pred)
    mse_train = mean_squared_error(y_train, train_pred)
    mse_test = mean_squared_error(y_test, test_pred)
    rmse_train = np.sqrt(mse_train)
    rmse_test = np.sqrt(mse_test)
    
    print(f'Random Forest Training R^2: {r2_train}')
    print(f'Random Forest Testing R^2: {r2_test}')
    print(f'Random Forest Training MAE: {mae_train}')
    print(f'Random Forest Testing MAE: {mae_test}')
    print(f'Random Forest Training MSE: {mse_train}')
    print(f'Random Forest Testing MSE: {mse_test}')
    print(f'Random Forest Training RMSE: {rmse_train}')
    print(f'Random Forest Testing RMSE: {rmse_test}')

if __name__ == "__main__":
    evaluate_model()
