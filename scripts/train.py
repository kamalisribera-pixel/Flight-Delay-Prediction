from pathlib import Path

import pandas as pd
from scipy.sparse import load_npz

try:
    from ._bootstrap import ensure_project_root_on_path
except ImportError:
    from _bootstrap import ensure_project_root_on_path

ensure_project_root_on_path()

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
    print("FLIGHT DELAY MODEL TRAINING")
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

    print(f"X Train : {X_train.shape}")
    print(f"y Train : {y_train.shape}")

    # -----------------------------------------------------
    # TRAIN MODELS
    # -----------------------------------------------------

    trainer = FlightModelTrainer(
        X_train=X_train,
        y_train=y_train
    )

    trainer.run()

    print("=" * 60)
    print("MODEL TRAINING COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
