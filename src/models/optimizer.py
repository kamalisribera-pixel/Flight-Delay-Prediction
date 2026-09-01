from pathlib import Path

import joblib

from sklearn.model_selection import RandomizedSearchCV
from src.utils.constants import CV_FOLDS, RANDOM_STATE, N_ITER_SEARCH, SCORING


class FlightModelOptimizer:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(
        self,
        models: dict,
        X_train,
        y_train,
        cv: int = CV_FOLDS,
        scoring: str = SCORING,
        n_iter: int = N_ITER_SEARCH,
        random_state: int = RANDOM_STATE,
    ):

        self.models = models

        self.X_train = X_train
        self.y_train = y_train

        self.cv = cv
        self.scoring = scoring
        self.n_iter = n_iter
        self.random_state = random_state

        self.best_models = {}

        self.output_path = Path("models")

        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )

    # =========================================================
    # PARAMETER GRIDS
    # =========================================================

    def parameter_grids(self):

        return {

            "logistic_regression": {

                "C": [0.01, 0.1, 1, 10, 100],

                "solver": [
                    "lbfgs",
                    "liblinear"
                ]
            },

            "decision_tree": {

                "max_depth": [
                    None,
                    10,
                    20,
                    30,
                    40
                ],

                "min_samples_split": [
                    2,
                    5,
                    10
                ],

                "min_samples_leaf": [
                    1,
                    2,
                    4
                ]
            },

            "random_forest": {

                "n_estimators": [
                    100,
                    200,
                    300
                ],

                "max_depth": [
                    None,
                    20,
                    40
                ],

                "min_samples_split": [
                    2,
                    5,
                    10
                ],

                "min_samples_leaf": [
                    1,
                    2,
                    4
                ]
            },

            "gradient_boosting": {

                "n_estimators": [
                    100,
                    200,
                    300
                ],

                "learning_rate": [
                    0.01,
                    0.05,
                    0.1
                ],

                "max_depth": [
                    3,
                    5,
                    7
                ]
            }

        }

    # =========================================================
    # OPTIMIZE SINGLE MODEL
    # =========================================================

    def optimize_model(
        self,
        model_name,
        model,
        parameters
    ):

        print("=" * 60)
        print(f"OPTIMIZING {model_name.upper()}")
        print("=" * 60)

        search = RandomizedSearchCV(

            estimator=model,

            param_distributions=parameters,

            n_iter=self.n_iter,

            scoring=self.scoring,

            cv=self.cv,

            n_jobs=-1,

            random_state=self.random_state,

            verbose=1

        )

        search.fit(
            self.X_train,
            self.y_train
        )

        self.best_models[model_name] = search.best_estimator_

        print()

        print("Best Score")

        print(search.best_score_)

        print()

        print("Best Parameters")

        for key, value in search.best_params_.items():

            print(f"{key} : {value}")

    # =========================================================
    # SAVE MODELS
    # =========================================================

    def save_models(self):

        print("=" * 60)
        print("SAVING OPTIMIZED MODELS")
        print("=" * 60)

        for name, model in self.best_models.items():

            filename = self.output_path / f"{name}_optimized.joblib"

            joblib.dump(
                model,
                filename
            )

            print(f"Saved : {filename}")

    # =========================================================
    # RUN
    # =========================================================

    def run(self):

        grids = self.parameter_grids()

        for model_name, model in self.models.items():

            self.optimize_model(

                model_name,

                model,

                grids[model_name]

            )

        self.save_models()

        print("=" * 60)
        print("MODEL OPTIMIZATION COMPLETE")
        print("=" * 60)

        return self.best_models