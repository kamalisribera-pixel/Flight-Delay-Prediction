import joblib
import pandas as pd
from pathlib import Path

from src.utils.paths import MODELS


class FlightPredictor:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(
        self,
        model_path: str = "random_forest.joblib",
        preprocessor_path: str = "preprocessor.pkl"
    ):

        self.model_path = self._resolve_artifact_path(model_path)
        self.preprocessor_path = self._resolve_artifact_path(preprocessor_path)

        self.model = None
        self.preprocessor = None

        self.load_preprocessor()
        self.load_model()

    @staticmethod
    def _resolve_artifact_path(path: str) -> Path:

        artifact_path = Path(path)

        if artifact_path.is_absolute():
            return artifact_path

        if artifact_path.parts and artifact_path.parts[0].lower() == "models":
            artifact_path = Path(*artifact_path.parts[1:])

        return MODELS / artifact_path

    # =========================================================
    # LOAD MODEL
    # =========================================================

    def load_model(self):

        self.model = joblib.load(self.model_path)

        print(f"Loaded : {self.model_path}")

    # =========================================================
    # LOAD PREPROCESSOR
    # =========================================================

    def load_preprocessor(self):

        self.preprocessor = joblib.load(
            self.preprocessor_path
        )

        print(f"Loaded : {self.preprocessor_path}")
        print("=" * 80)
        print("EXPECTED FEATURES")
        print("=" * 80)

        for column in self.preprocessor.feature_names_in_:
            print(column)

        print("=" * 80)


        print("=" * 60)
        print("PREPROCESSOR EXPECTS")
        print("=" * 60)

        print(list(self.preprocessor.feature_names_in_))

        print("=" * 60)


    # =========================================================
    # PREPROCESS INPUT
    # =========================================================

    def preprocess(
        self,
        input_df: pd.DataFrame
    ):

        print("=" * 60)
        print("INPUT DATAFRAME")
        print("=" * 60)

        print(input_df)

        print()

        print(input_df.columns.tolist())

        # Temporary fix
        input_df = input_df.copy()

        input_df["DIVERTED"] = 0
        input_df["CANCELLED"] = 0

        print()
        print("AFTER ADDING")
        print(input_df.columns.tolist())

        return self.preprocessor.transform(input_df)
    # =========================================================
    # PREDICT
    # =========================================================

    def predict(
        self,
        input_df: pd.DataFrame
    ):

        X = self.preprocess(input_df)

        prediction = int(
            self.model.predict(X)[0]
        )

        probability = float(
            self.model.predict_proba(X)[0][1]
        )

        return {

            "prediction": prediction,

            "probability": probability,

            "delay_probability": probability,

            "on_time_probability": 1 - probability

        }