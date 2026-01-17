# src/model.py
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

class RunTimeRegressor:
    def __init__(self, alpha=1.0):
        self.model = Ridge(alpha=alpha)

    def train(self, X, y):
        self.model.fit(X, y)

    def evaluate(self, X, y):
        preds = self.model.predict(X)
        return {
            "MAE_min": mean_absolute_error(y, preds),
            "RMSE_min": np.sqrt(mean_squared_error(y, preds))
        }

    def predict(self, X):
        return self.model.predict(X)
