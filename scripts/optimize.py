from pathlib import Path

import pandas as pd
from scipy.sparse import load_npz

from src.models.optimizer import FlightModelOptimizer
from src.models.trainer import FlightModelTrainer

# =========================================================
# CONFIGURATION
# =========================================================

DATA_PATH = Path("data/processed")

# =========================================================
# MAIN
# =========================================================

def main():

    print("=" * 60)
    print("FLIGHT MODEL OPTIMIZATION")
    print("=" * 60)

    # -----------------------------------------------------
    # LOAD TRAINING DATA
    # -----------------------------------------------------

    X_train = load_npz(
        DATA_PATH / "X_train.npz"
    )

    y_train = pd.read_csv(
        DATA_PATH / "y_train.csv"
    ).squeeze()

    # -----------------------------------------------------
    # LOAD MODELS
    # -----------------------------------------------------

    trainer = FlightModelTrainer(
        X_train=X_train,
        y_train=y_train
    )

    models = trainer.load_models()

    # -----------------------------------------------------
    # OPTIMIZE
    # -----------------------------------------------------

    optimizer = FlightModelOptimizer(
        models=models,
        X_train=X_train,
        y_train=y_train,
        scoring="f1",
        cv=5,
        n_iter=10
    )

    optimizer.run()

    print("=" * 60)
    print("MODEL OPTIMIZATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()