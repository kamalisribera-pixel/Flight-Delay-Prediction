from pathlib import Path

import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)
from src.utils.constants import RANDOM_STATE, CV_FOLDS


class FlightModelTrainer:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(
        self,
        X_train,
        y_train,
    ):

        self.X_train = X_train
        self.y_train = y_train

        self.models = {}

        self.output_path = Path("models")

        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )

    # =========================================================
    # LOGISTIC REGRESSION
    # =========================================================

    def train_logistic_regression(self):

        print("=" * 60)
        print("TRAINING LOGISTIC REGRESSION")
        print("=" * 60)

        model = LogisticRegression(
            max_iter=1000,
            random_state=RANDOM_STATE,
            class_weight="balanced"
        )

        model.fit(
            self.X_train,
            self.y_train
        )

        self.models["Logistic Regression"] = model

        print("Training Complete.")

    # =========================================================
    # DECISION TREE
    # =========================================================

    def train_decision_tree(self):

        print("=" * 60)
        print("TRAINING DECISION TREE")
        print("=" * 60)

        model = DecisionTreeClassifier(
            random_state=RANDOM_STATE
        )

        model.fit(
            self.X_train,
            self.y_train
        )

        self.models["decision_tree"] = model

        print("Training Complete.")
    

    # =========================================================
    # RANDOM FOREST
    # =========================================================

    def train_random_forest(self):

        print("=" * 60)
        print("TRAINING RANDOM FOREST")
        print("=" * 60)

        model = RandomForestClassifier(
            n_estimators=100,
            random_state=RANDOM_STATE,
            n_jobs=1
        )

        model.fit(
            self.X_train,
            self.y_train
        )

        self.models["random_forest"] = model

        print("Training Complete.")


    # =========================================================
    # GRADIENT BOOSTING
    # =========================================================

    def train_gradient_boosting(self):

        print("=" * 60)
        print("TRAINING GRADIENT BOOSTING")
        print("=" * 60)

        model = GradientBoostingClassifier(
            random_state=RANDOM_STATE
        )

        model.fit(
            self.X_train,
            self.y_train
        )

        self.models["gradient_boosting"] = model

        print("Training Complete.")

    # =========================================================
    # LOAD MODELS
    # =========================================================

    def load_models(self):

        return {

            "Logistic Regression": joblib.load(
                "models/Logistic Regression.joblib"
            ),


            "Decision Tree": joblib.load(
                "models/decision_tree.joblib"
            ),


            "Random Forest": joblib.load(
                "models/random_forest.joblib"
            ),


            "Gradient Boosting": joblib.load(
                "models/gradient_boosting.joblib"
            )

        }



    # =========================================================
    # SAVE MODELS
    # =========================================================

    def save(self):

        print("=" * 60)
        print("SAVING MODELS")
        print("=" * 60)

        for name, model in self.models.items():

            path = self.output_path / f"{name}.joblib"

            joblib.dump(
                model,
                path
            )

            print(f"Saved : {path}")

    # =========================================================
    # RUN PIPELINE
    # =========================================================

    def run(self):

        self.train_logistic_regression()

        self.train_decision_tree()

        self.train_random_forest()

        self.train_gradient_boosting()

        self.save()

        return self.models
