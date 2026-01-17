# src/model.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

class RunTimeRegressor:
    def __init__(self, n_estimators=200, max_depth=None, random_state=42):
        """
        Random Forest regressor for running time prediction.

        Args:
            n_estimators: number of trees
            max_depth: max depth of each tree (None = unlimited)
            random_state: for reproducibility
        """
        self.model = RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=random_state
        )

    def train(self, X, y):
        """
        Train the Random Forest model.
        X: pandas DataFrame or numpy array of features
        y: pandas Series or numpy array of target (running time)
        """
        self.model.fit(X, y)

    def evaluate(self, X, y):
        """
        Evaluate the model and return MAE and RMSE.
        """
        preds = self.model.predict(X)
        return {
            "MAE_min": mean_absolute_error(y, preds),
            "RMSE_min": np.sqrt(mean_squared_error(y, preds))
        }

    def predict(self, X):
        """
        Predict running time for given features.
        """
        return self.model.predict(X)

    def feature_importances(self, feature_names):
        """
        Return feature importance dictionary.
        """
        if hasattr(self.model, "feature_importances_"):
            return dict(zip(feature_names, self.model.feature_importances_))
        else:
            raise AttributeError("Model has no feature_importances_ attribute")
