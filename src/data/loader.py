from pathlib import Path
import pandas as pd


class FlightDataLoader:
    """
    Responsible only for loading the raw BTS dataset.
    """

    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)

    def load(self) -> pd.DataFrame:
        if not self.csv_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.csv_path}"
            )

        print("=" * 60)
        print("Loading dataset...")
        print("=" * 60)

        df = pd.read_csv(
            self.csv_path,
            low_memory=False
        )

        print(f"Rows    : {df.shape[0]:,}")
        print(f"Columns : {df.shape[1]}")
        print(
            f"Memory  : {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB"
        )

        return df