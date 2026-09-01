from pathlib import Path
import joblib

from sklearn.linear_model import LogisticRegression


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
            random_state=42
        )

        model.fit(
            self.X_train,
            self.y_train
        )

        self.models["Logistic Regression"] = model

        print("Training Complete.")

    # =========================================================
    # SAVE MODELS
    # =========================================================

    def save_models(self):

        print("=" * 60)
        print("SAVING MODELS")
        print("=" * 60)

        for name, model in self.models.items():

            filename = (
                name.lower()
                .replace(" ", "_")
                + ".joblib"
            )

            joblib.dump(
                model,
                self.output_path / filename
            )

            print(f"Saved : {filename}")

    # =========================================================
    # RUN PIPELINE
    # =========================================================

    def run(self):

        self.train_logistic_regression()

        self.save_models()

        return self.models
