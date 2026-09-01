from pathlib import Path

import pandas as pd

class FlightDataCleaner:

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

        self.output_path = Path("data/processed")

        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )


    # =========================================================
    # REMOVING CANCELLED FLIGHTS
    # =========================================================

    def remove_cancelled(self):

        before = len(self.df)

        self.df = self.df[
            self.df["CANCELLED"] == 0
        ]

        removed = before - len(self.df)

        print("=" * 60)
        print("REMOVE CANCELLED FLIGHTS")
        print("=" * 60)
        print(f"Removed : {removed:,}")
        print(f"Remaining : {len(self.df):,}")


    # =========================================================
    # REMOVING DIVERTED FLIGHTS
    # =========================================================
    
    def remove_diverted(self):

        before = len(self.df)

        self.df = self.df[
            self.df["DIVERTED"] == 0
        ]

        removed = before - len(self.df)

        print("=" * 60)
        print("REMOVE DIVERTED FLIGHTS")
        print("=" * 60)
        print(f"Removed : {removed:,}")
        print(f"Remaining : {len(self.df):,}")


    # =========================================================
    # CHECK MISSING VALUES  
    # =========================================================

    def check_missing_values(self):

        print("=" * 60)
        print("CHECK MISSING VALUES")
        print("=" * 60)

        missing = self.df.isna().sum()

        missing = missing[missing > 0]

        if missing.empty:

            print("No missing values found.")

        else:

            print(missing)


    # =========================================================
    # RESET INDEX
    # =========================================================
    
    def reset_index(self):

        self.df.reset_index(
            drop=True,
            inplace=True
        )

        print("=" * 60)
        print("INDEX RESET")
        print("=" * 60)
        print("Index reset successfully.")


    # =========================================================
    # SAVE CLEANED DATA
    # =========================================================

    def save(self):

        output_file = "data/processed/flights_clean.csv"

        with open(output_file, "w") as f:
            f.write("test")

        print("=" * 60)
        print("DATASET SAVED")
        print("=" * 60)
        print(f"Location : {output_file}")



    # =========================================================
    # RUN CLEANING PIPELINE
    # =========================================================

    def run(self):

        self.remove_cancelled()

        self.remove_diverted()

        self.check_missing_values()

        self.reset_index()

        self.save()

        return self.df