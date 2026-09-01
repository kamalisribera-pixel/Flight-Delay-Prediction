from pathlib import Path

import pandas as pd
from scipy.sparse import load_npz

from src.models.trainer import FlightModelTrainer
from src.models.evaluator import FlightModelEvaluator

# =========================================================
# CONFIGURATION
# =========================================================

DATA_PATH = Path("data/processed")

# =========================================================
# MAIN
# =========================================================

def main():

    print("=" * 60)
    print("FLIGHT MODEL EVALUATION")
    print("=" * 60)

    # -----------------------------------------------------
    # LOAD TEST DATA
    # -----------------------------------------------------

    X_test = load_npz(
        DATA_PATH / "X_test.npz"
    )

    y_test = pd.read_csv(
        DATA_PATH / "y_test.csv"
    ).squeeze()

    print(f"X Test : {X_test.shape}")
    print(f"y Test : {y_test.shape}")

    # -----------------------------------------------------
    # LOAD TRAINED MODELS
    # -----------------------------------------------------

    trainer = FlightModelTrainer(
        X_train=None,
        y_train=None
    )

    models = trainer.load_models()

    # -----------------------------------------------------
    # EVALUATE
    # -----------------------------------------------------

    evaluator = FlightModelEvaluator(
        models=models,
        X_test=X_test,
        y_test=y_test
    )

    evaluator.run()

    print("=" * 60)
    print("MODEL EVALUATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()