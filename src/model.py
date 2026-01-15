# src/model.py

import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error

class RunTimeRegressor:
    def __init__(self, model_type="ridge", alpha=1.0):
        """
        Initialize the regression model.

        Args:
            model_type (str): "ridge" or "linear"
            alpha (float): Regularization strength for Ridge
        """
        if model_type == "ridge":
            self.model = Ridge(alpha=alpha)
        elif model_type == "linear":
            self.model = LinearRegression()
        else:
            raise ValueError("model_type must be 'ridge' or 'linear'")

    def train(self, X_train, y_train):
        """
        Fit the model to training data.

        Args:
            X_train (pd.DataFrame or np.array): Feature matrix
            y_train (pd.Series or np.array): Target vector
        """
        self.model.fit(X_train, y_train)

    def evaluate(self, X_val, y_val):
        """
        Evaluate the model on validation data.

        Returns:
            dict: MAE and RMSE
        """
        preds = self.model.predict(X_val)
        mae = mean_absolute_error(y_val, preds)
        rmse = np.sqrt(mean_squared_error(y_val, preds))
        return {"mae_minutes": mae, "rmse_minutes": rmse}

    def predict(self, X):
        """
        Predict target values for new data.

        Args:
            X (pd.DataFrame or np.array): Feature matrix

        Returns:
            np.array: Predicted values
        """
        return self.model.predict(X)
