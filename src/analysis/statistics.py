import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


class FlightStatistics:

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

        self.output_path = Path("reports/statistics")

        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )

    # =========================================================
    # CORRELATION ANALYSIS
    # =========================================================

    def correlation_analysis(self):

        print("=" * 60)
        print("CORRELATION ANALYSIS")
        print("=" * 60)

        correlation = (
            self.df.select_dtypes(include="number")
            .corr(numeric_only=True)["ARR_DELAY"]
            .sort_values(ascending=False)
        )

        print(correlation)

        correlation.to_csv(
            self.output_path / "correlation_analysis.csv"
        )

    # =========================================================
    # AIRLINE DELAY RATE
    # =========================================================

    def airline_delay_rate(self):

        print("=" * 60)
        print("AIRLINE DELAY RATE")
        print("=" * 60)

        delay_rate = (
            self.df.groupby("OP_UNIQUE_CARRIER")["ARR_DEL15"]
            .mean()
            * 100
        )

        delay_rate = delay_rate.sort_values(
            ascending=False
        )

        print(delay_rate)

        plt.figure(figsize=(10, 5))

        delay_rate.plot(kind="bar")

        plt.title("Delay Percentage by Airline")
        plt.ylabel("Delayed Flights (%)")

        plt.tight_layout()

        plt.savefig(
            self.output_path / "airline_delay_rate.png"
        )

        plt.close()

        delay_rate.to_csv(
            self.output_path / "airline_delay_rate.csv"
        )

    # =========================================================
    # DEPARTURE HOUR DELAY RATE
    # =========================================================

    def departure_hour_rate(self):

        print("=" * 60)
        print("DEPARTURE HOUR DELAY RATE")
        print("=" * 60)

        hour_rate = (
            self.df.groupby("DEP_HOUR")["ARR_DEL15"]
            .mean()
            * 100
        )

        print(hour_rate)

        plt.figure(figsize=(10, 5))

        hour_rate.plot(marker="o")

        plt.title("Delay Percentage by Departure Hour")
        plt.ylabel("Delayed Flights (%)")

        plt.tight_layout()

        plt.savefig(
            self.output_path / "departure_hour_delay_rate.png"
        )

        plt.close()

        hour_rate.to_csv(
            self.output_path / "departure_hour_delay_rate.csv"
        )

    # =========================================================
    # WEEKDAY DELAY RATE
    # =========================================================

    def weekday_delay_rate(self):

        print("=" * 60)
        print("WEEKDAY DELAY RATE")
        print("=" * 60)

        weekday_rate = (
            self.df.groupby("DAY_OF_WEEK")["ARR_DEL15"]
            .mean()
            * 100
        )

        print(weekday_rate)

        plt.figure(figsize=(8, 5))

        weekday_rate.plot(kind="bar")

        plt.title("Delay Percentage by Day of Week")
        plt.ylabel("Delayed Flights (%)")

        plt.tight_layout()

        plt.savefig(
            self.output_path / "weekday_delay_rate.png"
        )

        plt.close()

        weekday_rate.to_csv(
            self.output_path / "weekday_delay_rate.csv"
        )

    # =========================================================
    # DISTANCE ANALYSIS
    # =========================================================

    def distance_analysis(self):

        print("=" * 60)
        print("DISTANCE ANALYSIS")
        print("=" * 60)

        distance = (
            self.df.groupby("DISTANCE_GROUP")["ARR_DELAY"]
            .mean()
        )

        print(distance)

        plt.figure(figsize=(8, 5))

        distance.plot(marker="o")

        plt.title("Average Delay by Distance Group")
        plt.ylabel("Average Arrival Delay")

        plt.tight_layout()

        plt.savefig(
            self.output_path / "distance_delay.png"
        )

        plt.close()

        distance.to_csv(
            self.output_path / "distance_delay.csv"
        )

    # =========================================================
    # TOP ROUTES
    # =========================================================

    def top_routes(self):

        print("=" * 60)
        print("TOP ROUTES")
        print("=" * 60)

        routes = (
            self.df.groupby(["ORIGIN", "DEST"])
            .size()
            .sort_values(ascending=False)
            .head(20)
        )

        print(routes)

        routes.to_csv(
            self.output_path / "top_routes.csv"
        )

    # =========================================================
    # ROUTE DELAY RATE
    # =========================================================

    def route_delay_rate(self):

        print("=" * 60)
        print("ROUTE DELAY RATE")
        print("=" * 60)

        delay = (
            self.df.groupby(["ORIGIN", "DEST"])["ARR_DEL15"]
            .mean()
            * 100
        )

        delay = delay.sort_values(
            ascending=False
        ).head(20)

        print(delay)

        delay.to_csv(
            self.output_path / "route_delay_rate.csv"
        )

    # =========================================================
    # MONTHLY ANALYSIS
    # =========================================================

    def monthly_analysis(self):

        print("=" * 60)
        print("MONTHLY ANALYSIS")
        print("=" * 60)

        monthly = (
            self.df.groupby("MONTH")["ARR_DELAY"]
            .mean()
        )

        print(monthly)

        plt.figure(figsize=(8, 5))

        monthly.plot(marker="o")

        plt.title("Monthly Average Arrival Delay")
        plt.ylabel("Arrival Delay (Minutes)")

        plt.tight_layout()

        plt.savefig(
            self.output_path / "monthly_delay.png"
        )

        plt.close()

        monthly.to_csv(
            self.output_path / "monthly_delay.csv"
        )

    # =========================================================
    # RUN
    # =========================================================

    def run(self):

        self.correlation_analysis()

        self.airline_delay_rate()

        self.departure_hour_rate()

        self.weekday_delay_rate()

        self.distance_analysis()

        self.top_routes()

        self.route_delay_rate()

        self.monthly_analysis()

        print("\nStatistical analysis completed successfully.")