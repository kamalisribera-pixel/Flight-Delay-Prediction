from pathlib import Path

import pandas as pd

class FlightFeatureEngineer:

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

        self.output_path = Path("data/processed")

        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )

    # ==========================
    # DEPARTURE HOUR   
    # ==========================

    def create_departure_hour(self):

        print("=" * 60)
        print("CREATING DEPARTURE HOUR")
        print("=" * 60)

        self.df["DEP_HOUR"] = (
            self.df["CRS_DEP_TIME"] // 100
        )

        print("Feature Created : DEP_HOUR")



    # =============================================
    # ARRIVAL HOUR
    # =============================================

    def create_arrival_hour(self):

        print("=" * 60)
        print("CREATING ARRIVAL HOUR")
        print("=" * 60)

        self.df["ARR_HOUR"] = (
            self.df["CRS_ARR_TIME"] // 100
        )

        print("Feature Created : ARR_HOUR")



    # =============================================
    # WEEKEND FLAG
    # =============================================

    def create_weekend_flag(self):

        print("=" * 60)
        print("CREATING WEEKEND FLAG")
        print("=" * 60)

        self.df["IS_WEEKEND"] = (
            self.df["DAY_OF_WEEK"] >= 6
        ).astype(int)

        print("Feature Created : IS_WEEKEND")



    # =============================================
    # DAY OF YEAR
    # =============================================

    def create_day_of_year(self):

        print("=" * 60)
        print("CREATING DAY OF YEAR")
        print("=" * 60)

        self.df["FL_DATE"] = pd.to_datetime(
            self.df["FL_DATE"],
            format="%m/%d/%Y %I:%M:%S %p"
        )

        self.df["DAY_OF_YEAR"] = (
            self.df["FL_DATE"].dt.dayofyear
        )

        print("Feature Created :" \
        "" \
        " DAY_OF_YEAR")


    # =============================================
    # VALIDATE FEATURES
    # =============================================

    def validate_features(self):

        print("=" * 60)
        print("FEATURE VALIDATION")
        print("=" * 60)

        features = [
            "DEP_HOUR",
            "ARR_HOUR",
            "IS_WEEKEND",
            "DAY_OF_YEAR"
        ]

        print(self.df[features].head())



    # =============================================
    # SAVE DATASET
    # =============================================

    def save(self):

        output_file = self.output_path / "flights_features.csv"

        self.df.to_csv(
            output_file,
            index=False
        )

        print("=" * 60)
        print("FEATURE DATASET SAVED")
        print("=" * 60)
        print(f"Location : {output_file}")



    # =============================================
    # RUN ENGINEERING FEATURES
    # =============================================

    def run(self):

        self.create_departure_hour()

        self.create_arrival_hour()

        self.create_weekend_flag()

        self.create_day_of_year()

        self.validate_features()

        self.save()

        return self.df