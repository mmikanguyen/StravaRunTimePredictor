import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class RunTimeRegressor:
    """
    Linear regression baseline for predicting running time (minutes).
    """

    def __init__(self):
        self.model = LinearRegression()
        self.is_trained = False

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        self.is_trained = True

    def predict(self, X):
        if not self.is_trained:
            raise RuntimeError("Model must be trained before prediction.")
        return self.model.predict(X)

    def evaluate(self, X, y):
        preds = self.predict(X)
        return {
            "MAE": mean_absolute_error(y, preds),
            "RMSE": np.sqrt(mean_squared_error(y, preds)),
            "R2": r2_score(y, preds)
        }


    def coefficients(self, feature_names):
        """
        Returns a dictionary mapping feature names to coefficients.
        """
        if not self.is_trained:
            raise RuntimeError("Model must be trained before accessing coefficients.")

        return dict(zip(feature_names, self.model.coef_))
