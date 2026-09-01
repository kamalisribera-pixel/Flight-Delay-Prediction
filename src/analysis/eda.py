from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class FlightEDA:

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

        self.output_path = Path("reports/figures")

        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )



    # =============================================
    # DATASET OVERVIEW
    # =============================================
    
    def dataset_overview(self):

        print("=" * 60)
        print("DATASET OVERVIEW")
        print("=" * 60)

        print(f"Flights : {len(self.df):,}")

        print(
            f"Delayed Flights : {(self.df['ARR_DEL15'] == 1).sum():,}"
        )

        print(
            f"On-Time Flights : {(self.df['ARR_DEL15'] == 0).sum():,}"
        )

        print()

        print(self.df["ARR_DELAY"].describe())



    # =============================================
    # DELAY DISTRIBUTION PLOT   
    # =============================================
    def arrival_delay_distribution(self):

        print("=" * 60)
        print("ARRIVAL DELAY DISTRIBUTION")
        print("=" * 60)

        plt.figure(figsize=(10,6))

        self.df["ARR_DELAY"].hist(
            bins=100
        )

        plt.xlabel("Arrival Delay (minutes)")
        plt.ylabel("Flights")
        plt.title("Arrival Delay Distribution")

        plt.tight_layout()

        plt.savefig(
            self.output_path / "arrival_delay_distribution.png"
        )

        plt.close()

        print("Saved : arrival_delay_distribution.png")


    # ===========================================
    # DELAY CLASS DISTRIBUTION PLOT
    # ===========================================

    def delay_class_distribution(self):

        plt.figure(figsize=(6,6))

        self.df["ARR_DEL15"].value_counts().plot(
            kind="bar"
        )

        plt.title("Delay Classification")
        plt.xlabel("Delayed")
        plt.ylabel("Flights")

        plt.tight_layout()

        plt.savefig(
            self.output_path / "delay_class_distribution.png"
        )

        plt.close()

        print("Saved : delay_class_distribution.png")

    # ===========================================
    # AIRLINE ANALYSIS
    # ===========================================
    def airline_analysis(self):

        print("=" * 60)
        print("AIRLINE ANALYSIS")
        print("=" * 60)

        airline_delay = (
            self.df
            .groupby("OP_UNIQUE_CARRIER")["ARR_DELAY"]
            .mean()
            .sort_values(ascending=False)
        )

        print(airline_delay)

        plt.figure(figsize=(12,6))

        airline_delay.plot(kind="bar")

        plt.title("Average Arrival Delay by Airline")
        plt.xlabel("Airline")
        plt.ylabel("Average Delay (minutes)")

        plt.tight_layout()

        plt.savefig(
            self.output_path /
            "airline_delay.png"
        )

        plt.close()

        print("Saved : airline_delay.png")

    # ===========================================
    # DEPARTURE HOUR ANALYSIS
    # ===========================================
    def departure_hour_analysis(self):

        print("=" * 60)
        print("DEPARTURE HOUR ANALYSIS")
        print("=" * 60)

        hourly = (
            self.df
            .groupby("DEP_HOUR")["ARR_DELAY"]
            .mean()
        )

        print(hourly)

        plt.figure(figsize=(12,6))

        hourly.plot(
            marker="o"
        )

        plt.title("Average Arrival Delay by Departure Hour")
        plt.xlabel("Departure Hour")
        plt.ylabel("Average Delay (minutes)")

        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            self.output_path /
            "departure_hour_delay.png"
        )

        plt.close()

        print("Saved : departure_hour_delay.png")


    # ===========================================
    # WEEKDAY ANALYSIS
    # ===========================================
    
    def weekday_analysis(self):

        print("=" * 60)
        print("DAY OF WEEK ANALYSIS")
        print("=" * 60)

        weekday = (
            self.df
            .groupby("DAY_OF_WEEK")["ARR_DELAY"]
            .mean()
        )

        print(weekday)

        plt.figure(figsize=(10,5))

        weekday.plot(kind="bar")

        plt.title("Average Arrival Delay by Day of Week")
        plt.xlabel("Day")
        plt.ylabel("Average Delay (minutes)")

        plt.tight_layout()

        plt.savefig(
            self.output_path /
            "weekday_delay.png"
        )

        plt.close()

        print("Saved : weekday_delay.png")

    # ===========================================
    # DESTINATION AIRPORT ANALYSIS
    # ===========================================

    def destination_airport_analysis(self):

        print("=" * 60)
        print("DESTINATION AIRPORT ANALYSIS")
        print("=" * 60)

        airport_delay = (
            self.df
            .groupby("DEST")["ARR_DELAY"]
            .mean()
            .sort_values(ascending=False)
            .head(20)
        )

        print(airport_delay)

        plt.figure(figsize=(14,6))

        airport_delay.plot(kind="bar")

        plt.title("Top 20 Destination Airports by Average Arrival Delay")
        plt.xlabel("Destination Airport")
        plt.ylabel("Average Delay (minutes)")

        plt.tight_layout()

        plt.savefig(
            self.output_path / "top20_destination_airport_delay.png"
        )

        plt.close()

        print("Saved : top20_destination_airport_delay.png")

    # ===========================================
    # FLIGHT COUNT BY AIRLINE
    # ===========================================

    def airline_flight_count(self):

        print("=" * 60)
        print("AIRLINE FLIGHT COUNTS")
        print("=" * 60)

        counts = (
            self.df["OP_UNIQUE_CARRIER"]
            .value_counts()
        )

        print(counts)

        plt.figure(figsize=(12,6))

        counts.plot(kind="bar")

        plt.title("Number of Flights by Airline")
        plt.xlabel("Airline")
        plt.ylabel("Flights")

        plt.tight_layout()

        plt.savefig(
            self.output_path / "airline_flight_counts.png"
        )

        plt.close()

        print("Saved : airline_flight_counts.png")

    # ===========================================
    # FLIGHT COUNT BY DEPARTURE HOUR
    # ===========================================
    def departure_hour_counts(self):

        print("=" * 60)
        print("DEPARTURE HOUR COUNTS")
        print("=" * 60)

        counts = (
            self.df["DEP_HOUR"]
            .value_counts()
            .sort_index()
        )

        print(counts)

        plt.figure(figsize=(12,6))

        counts.plot(marker="o")

        plt.title("Flights by Departure Hour")
        plt.xlabel("Hour")
        plt.ylabel("Flights")

        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            self.output_path / "departure_hour_counts.png"
        )

        plt.close()

        print("Saved : departure_hour_counts.png")

    # ===========================================
    # AIRPORT ANALYSIS
    # ===========================================
    def airport_analysis(self):

        print("=" * 60)
        print("ORIGIN AIRPORT ANALYSIS")
        print("=" * 60)

        airport_delay = (
            self.df
            .groupby("ORIGIN")["ARR_DELAY"]
            .mean()
            .sort_values(ascending=False)
            .head(20)
        )

        print(airport_delay)

        plt.figure(figsize=(14,6))

        airport_delay.plot(kind="bar")

        plt.title("Top 20 Origin Airports by Average Arrival Delay")
        plt.xlabel("Origin Airport")
        plt.ylabel("Average Delay (minutes)")

        plt.tight_layout()

        plt.savefig(
            self.output_path / "top20_origin_airport_delay.png"
        )

        plt.close()

        print("Saved : top20_origin_airport_delay.png")


    # ===========================================
    # RUN ALL EDA
    # ===========================================

    def run(self):

        self.dataset_overview()

        self.arrival_delay_distribution()

        self.delay_class_distribution()

        self.airline_analysis()

        self.departure_hour_analysis()

        self.weekday_analysis()

        self.airport_analysis()

        self.destination_airport_analysis()

        self.airline_flight_count()

        self.departure_hour_counts()