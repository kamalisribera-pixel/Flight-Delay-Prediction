from pathlib import Path

import pandas as pd


class FlightDataProfiler:

    def __init__(self, df: pd.DataFrame):

        self.df = df

        self.report_path = Path("reports")
        self.report_path.mkdir(exist_ok=True)

    # ==========================================================
    # OVERALL PROFILE
    # ==========================================================

    def basic_info(self):

        lines = [
            "=" * 60,
            "DATASET PROFILE",
            "=" * 60,
            f"Rows       : {self.df.shape[0]:,}",
            f"Columns    : {self.df.shape[1]}",
            f"Memory     : {self.df.memory_usage(deep=True).sum()/1024**2:.2f} MB",
        ]

        report = "\n".join(lines)

        print(report)

        with open(self.report_path / "profile.txt", "w") as file:
            file.write(report)

    # ==========================================================
    # COLUMN PROFILE
    # ==========================================================

    def column_info(self):

        print("\nCOLUMN INFORMATION")

        info = pd.DataFrame({
            "Data Type": self.df.dtypes,
            "Missing Values": self.df.isna().sum(),
            "Unique Values": self.df.nunique()
        })

        print(info)

        info.to_csv(
            self.report_path / "column_information.csv"
        )

    # ==========================================================
    # MISSING VALUES
    # ==========================================================

    def missing_values(self):

        missing = self.df.isna().sum()
        missing = missing[missing > 0]

        print("\nMISSING VALUES")

        if missing.empty:
            print("No missing values found.")
        else:
            print(missing)

        missing.to_csv(
            self.report_path / "missing_values.csv"
        )

    # ==========================================================
    # DUPLICATE CHECK
    # ==========================================================

    def duplicate_info(self):

        duplicates = self.df[self.df.duplicated()]

        print("\nDUPLICATES")
        print(f"Duplicate Rows : {len(duplicates):,}")

        duplicates.to_csv(
            self.report_path / "duplicates.csv",
            index=False
        )

    # ==========================================================
    # CANCELLED FLIGHTS
    # ==========================================================

    def cancellation_info(self):

        cancelled = self.df[self.df["CANCELLED"] == 1]

        print("\nCANCELLED FLIGHTS")
        print(f"Cancelled : {len(cancelled):,}")

        cancelled.to_csv(
            self.report_path / "cancelled_flights.csv",
            index=False
        )

    # ==========================================================
    # DIVERTED FLIGHTS
    # ==========================================================

    def diversion_info(self):

        diverted = self.df[self.df["DIVERTED"] == 1]

        print("\nDIVERTED FLIGHTS")
        print(f"Diverted : {len(diverted):,}")

        diverted.to_csv(
            self.report_path / "diverted_flights.csv",
            index=False
        )

    # ==========================================================
    # TARGET DISTRIBUTION
    # ==========================================================

    def target_distribution(self):

        print("\nTARGET DISTRIBUTION")

        distribution = (
            self.df["ARR_DEL15"]
            .value_counts(dropna=False)
            .sort_index()
        )

        print(distribution)

        distribution.to_csv(
            self.report_path / "target_distribution.csv"
        )

    # ==========================================================
    # SUMMARY STATISTICS
    # ==========================================================

    def summary_statistics(self):

        print("\nSUMMARY STATISTICS")

        summary = self.df.describe(include="all")

        print(summary)

        summary.to_csv(
            self.report_path / "summary_statistics.csv"
        )

    # ==========================================================
    # RUN COMPLETE PROFILER
    # ==========================================================

    def run(self):

        self.basic_info()

        self.column_info()

        self.missing_values()

        self.duplicate_info()

        self.cancellation_info()

        self.diversion_info()

        self.target_distribution()

        self.summary_statistics()