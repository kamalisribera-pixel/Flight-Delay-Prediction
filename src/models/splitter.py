from pathlib import Path

import joblib
import pandas as pd

from scipy import sparse
from sklearn.model_selection import train_test_split


class FlightDataSplitter:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(
        self,
        X,
        y,
        test_size: float = 0.2,
        random_state: int = 42
    ):

        self.X = X
        self.y = y

        self.test_size = test_size
        self.random_state = random_state

        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

        self.output_path = Path("data/processed")
        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )

    # =========================================================
    # TRAIN TEST SPLIT
    # =========================================================

    def split(self):

        print("=" * 60)
        print("TRAIN TEST SPLIT")
        print("=" * 60)

        (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test
        ) = train_test_split(
            self.X,
            self.y,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=self.y
        )

        print(f"Training Samples : {self.X_train.shape[0]:,}")
        print(f"Testing Samples  : {self.X_test.shape[0]:,}")

    # =========================================================
    # VALIDATE SPLIT
    # =========================================================

    def validate(self):

        print("=" * 60)
        print("SPLIT VALIDATION")
        print("=" * 60)

        print(f"X Train Shape : {self.X_train.shape}")
        print(f"X Test Shape  : {self.X_test.shape}")
        print(f"y Train Shape : {self.y_train.shape}")
        print(f"y Test Shape  : {self.y_test.shape}")

    # =========================================================
    # SAVE DATASETS
    # =========================================================

    def save(self):

        sparse.save_npz(
            self.output_path / "X_train.npz",
            self.X_train
        )

        sparse.save_npz(
            self.output_path / "X_test.npz",
            self.X_test
        )

        self.y_train.to_csv(
            self.output_path / "y_train.csv",
            index=False
        )

        self.y_test.to_csv(
            self.output_path / "y_test.csv",
            index=False
        )

        print("=" * 60)
        print("DATASETS SAVED")
        print("=" * 60)

        print(self.output_path / "X_train.npz")
        print(self.output_path / "X_test.npz")
        print(self.output_path / "y_train.csv")
        print(self.output_path / "y_test.csv")

    # =========================================================
    # RUN PIPELINE
    # =========================================================

    def run(self):

        self.split()

        self.validate()

        self.save()

        return (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test
        )