import sqlite3

import pandas as pd
from src.utils.paths import DATABASE


class FlightDatabaseBuilder:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(
        self,
        df: pd.DataFrame
    ):

        self.df = df.copy()

        self.database_path = DATABASE

        self.database_path.mkdir(
            parents=True,
            exist_ok=True
        )

        self.database_file = (
            self.database_path / "flight_delay.db"
        )

        self.connection = None
        self.cursor = None

    # =========================================================
    # CONNECT DATABASE
    # =========================================================

    def connect(self):

        print("=" * 60)
        print("CONNECTING DATABASE")
        print("=" * 60)

        self.connection = sqlite3.connect(
            self.database_file
        )

        self.cursor = self.connection.cursor()

        print(f"Database Created : {self.database_file}")

    # =========================================================
    # CREATE AIRPORT TABLE
    # =========================================================

    def create_airports_table(self):

        print("=" * 60)
        print("CREATING AIRPORTS TABLE")
        print("=" * 60)

        self.cursor.execute("""
        DROP TABLE IF EXISTS airports
        """)

        self.cursor.execute("""
        CREATE TABLE airports(

            airport TEXT PRIMARY KEY,

            airport_id INTEGER,

            city TEXT,

            state TEXT

        )
        """)

        print("Table Created : airports")

    # =========================================================
    # CREATE ROUTES TABLE
    # =========================================================

    def create_routes_table(self):

        print("=" * 60)
        print("CREATING ROUTES TABLE")
        print("=" * 60)

        self.cursor.execute("""
        DROP TABLE IF EXISTS routes
        """)

        self.cursor.execute("""
        CREATE TABLE routes(

            origin TEXT,

            destination TEXT,

            distance REAL,

            distance_group INTEGER,

            crs_elapsed_time REAL,

            PRIMARY KEY(origin,destination)

        )
        """)

        print("Table Created : routes")

    # =========================================================
    # CREATE AIRLINES TABLE
    # =========================================================

    def create_airlines_table(self):

        print("=" * 60)
        print("CREATING AIRLINES TABLE")
        print("=" * 60)

        self.cursor.execute("""
        DROP TABLE IF EXISTS airlines
        """)

        self.cursor.execute("""
        CREATE TABLE airlines(

            carrier TEXT PRIMARY KEY

        )
        """)

        print("Table Created : airlines")

    # =========================================================
    # CREATE PREDICTIONS TABLE
    # =========================================================

    def create_predictions_table(self):

        print("=" * 60)
        print("CREATING PREDICTIONS TABLE")
        print("=" * 60)

        self.cursor.execute("""
        DROP TABLE IF EXISTS predictions
        """)

        self.cursor.execute("""
        CREATE TABLE predictions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            airline TEXT,

            origin TEXT,

            destination TEXT,

            probability REAL,

            prediction INTEGER

        )
        """)

        print("Table Created : predictions")

    # =========================================================
    # INSERT AIRPORTS
    # =========================================================

    def insert_airports(self):

        print("=" * 60)
        print("INSERTING AIRPORTS")
        print("=" * 60)

        origin = self.df[
            [
                "ORIGIN",
                "ORIGIN_AIRPORT_ID",
                "ORIGIN_CITY_NAME",
                "ORIGIN_STATE_ABR"
            ]
        ].copy()

        origin.columns = [
            "airport",
            "airport_id",
            "city",
            "state"
        ]

        destination = self.df[
            [
                "DEST",
                "DEST_AIRPORT_ID",
                "DEST_CITY_NAME",
                "DEST_STATE_ABR"
            ]
        ].copy()

        destination.columns = [
            "airport",
            "airport_id",
            "city",
            "state"
        ]

        airports = pd.concat(
            [origin, destination],
            ignore_index=True
        ).drop_duplicates()

        airports.to_sql(
            "airports",
            self.connection,
            if_exists="append",
            index=False
        )

        print(f"Inserted : {len(airports):,}")

    # =========================================================
    # INSERT ROUTES
    # =========================================================

    def insert_routes(self):

        print("=" * 60)
        print("INSERTING ROUTES")
        print("=" * 60)

        routes = self.df[
            [
                "ORIGIN",
                "DEST",
                "DISTANCE",
                "DISTANCE_GROUP",
                "CRS_ELAPSED_TIME"
            ]
        ].copy()

        routes.columns = [
            "origin",
            "destination",
            "distance",
            "distance_group",
            "crs_elapsed_time"
        ]

        # -----------------------------------------------------
        # Multiple flights exist for the same route.
        # Store one record per route using the average
        # scheduled elapsed time.
        # -----------------------------------------------------

        routes = (
            routes
            .groupby(
                [
                    "origin",
                    "destination"
                ],
                as_index=False
            )
            .agg({
                "distance": "first",
                "distance_group": "first",
                "crs_elapsed_time": "mean"
            })
        )

        routes.to_sql(
            "routes",
            self.connection,
            if_exists="append",
            index=False
        )

        print(f"Inserted : {len(routes):,}")

    # =========================================================
    # INSERT AIRLINES
    # =========================================================

    def insert_airlines(self):

        print("=" * 60)
        print("INSERTING AIRLINES")
        print("=" * 60)

        airlines = pd.DataFrame({

            "carrier":
                sorted(
                    self.df["OP_UNIQUE_CARRIER"].unique()
                )

        })

        airlines.to_sql(
            "airlines",
            self.connection,
            if_exists="append",
            index=False
        )

        print(f"Inserted : {len(airlines):,}")

    # =========================================================
    # SAVE DATABASE
    # =========================================================

    def save(self):

        self.connection.commit()

        print("=" * 60)
        print("DATABASE SAVED")
        print("=" * 60)

        print(self.database_file)

    # =========================================================
    # CLOSE CONNECTION
    # =========================================================

    def close(self):

        if self.connection is not None:

            self.connection.close()

        print("=" * 60)
        print("DATABASE CLOSED")
        print("=" * 60)

    # =========================================================
    # RUN PIPELINE
    # =========================================================

    def run(self):

        try:

            self.connect()

            self.create_airports_table()
            self.create_routes_table()
            self.create_airlines_table()
            self.create_predictions_table()

            self.insert_airports()
            self.insert_routes()
            self.insert_airlines()

            self.save()

        finally:

            self.close()