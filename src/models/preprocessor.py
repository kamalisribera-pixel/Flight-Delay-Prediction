from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler


class FlightPreprocessor:

    # =========================================================
    # CONFIGURATION
    # =========================================================

    DROP_COLUMNS = [

        # =====================================================
        # CONSTANT COLUMNS
        # =====================================================

        "YEAR",
        "QUARTER",
        "MONTH",

        # =====================================================
        # ORIGINAL DATE
        # =====================================================

        "FL_DATE",

        # =====================================================
        # INFORMATION NOT AVAILABLE BEFORE DEPARTURE
        # =====================================================

        "DEP_TIME",
        "DEP_DELAY",
        "DEP_DELAY_NEW",
        "DEP_DEL15",

        "ARR_TIME",
        "ARR_DELAY",
        "ARR_DELAY_NEW",

        "ACTUAL_ELAPSED_TIME",
        "AIR_TIME"

    ]

    TARGET_COLUMN = "ARR_DEL15"

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(
        self,
        df: pd.DataFrame,
        target_column: str = "ARR_DEL15"
    ):

        self.df = df.copy()

        self.target_column = target_column

        self.X = None
        self.y = None

        self.numeric_columns = None
        self.categorical_columns = None

        self.preprocessor = None

        self.output_path = Path("models")

        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )

    # =========================================================
    # REMOVE UNUSED COLUMNS
    # =========================================================

    def remove_unused_columns(self):

        print("=" * 60)
        print("REMOVE UNUSED COLUMNS")
        print("=" * 60)

        self.df.drop(
            columns=self.DROP_COLUMNS,
            inplace=True,
            errors="ignore"
        )

        print("Dropped Columns:")

        for column in self.DROP_COLUMNS:
            print(f"• {column}")

    # =========================================================
    # SEPARATE FEATURES AND TARGET
    # =========================================================

    def separate_target(self):

        print("=" * 60)
        print("SEPARATE FEATURES AND TARGET")
        print("=" * 60)

        self.X = self.df.drop(
            columns=[self.target_column]
        )

        self.y = self.df[self.target_column]

        print(f"Features : {self.X.shape}")
        print(f"Target   : {self.y.shape}")

    # =========================================================
    # IDENTIFY COLUMN TYPES
    # =========================================================

    def identify_columns(self):

        print("=" * 60)
        print("IDENTIFYING COLUMN TYPES")
        print("=" * 60)

        self.numeric_columns = self.X.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()

        self.categorical_columns = self.X.select_dtypes(
            include=["object"]
        ).columns.tolist()

        print(f"Numeric Columns     : {len(self.numeric_columns)}")
        print(f"Categorical Columns : {len(self.categorical_columns)}")

    # =========================================================
    # BUILD PREPROCESSOR
    # =========================================================

    def build_preprocessor(self):

        print("=" * 60)
        print("BUILDING PREPROCESSOR")
        print("=" * 60)

        self.preprocessor = ColumnTransformer(

            transformers=[

                (
                    "numeric",
                    StandardScaler(),
                    self.numeric_columns
                ),

                (
                    "categorical",
                    OneHotEncoder(
                        handle_unknown="ignore"
                    ),
                    self.categorical_columns
                )

            ]

        )

        print("Preprocessor created successfully.")

    # =========================================================
    # TRANSFORM FEATURES
    # =========================================================

    def transform(self):

        print("=" * 60)
        print("TRANSFORMING FEATURES")
        print("=" * 60)

        self.X = self.preprocessor.fit_transform(
            self.X
        )

        print(f"Processed Shape : {self.X.shape}")

    # =========================================================
    # VALIDATE PREPROCESSED DATA
    # =========================================================

    def validate(self):

        print("=" * 60)
        print("PREPROCESSING VALIDATION")
        print("=" * 60)

        print(f"Samples  : {self.X.shape[0]:,}")
        print(f"Features : {self.X.shape[1]:,}")

    # =========================================================
    # SAVE PREPROCESSOR
    # =========================================================

    def save(self):

        joblib.dump(
            self.preprocessor,
            self.output_path / "preprocessor.pkl"
        )

        self.y.to_csv(
            self.output_path / "y.csv",
            index=False
        )

        print("=" * 60)
        print("PREPROCESSOR SAVED")
        print("=" * 60)
        print("Saved :")
        print(self.output_path / "preprocessor.pkl")
        print(self.output_path / "y.csv")

    # =========================================================
    # RUN PIPELINE
    # =========================================================

    def run(self):

        self.remove_unused_columns()

        self.separate_target()

        self.identify_columns()

        self.build_preprocessor()

        self.transform()

        self.validate()

        self.save()

        return self.X, self.y