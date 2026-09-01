import sqlite3

from .queries import (
    GET_AIRPORTS,
    GET_AIRLINES,
    GET_ROUTE,
    GET_AIRPORT,
    INSERT_PREDICTION,
    GET_PREDICTIONS,
    DELETE_PREDICTIONS
)

from src.utils.paths import DATABASE


class FlightDatabase:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self):

        self.database = DATABASE / "flight_delay.db"

        self.connection = None
        self.cursor = None

    # =========================================================
    # CONNECT
    # =========================================================

    def connect(self):

        self.connection = sqlite3.connect(
            self.database,
            check_same_thread=False
        )

        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
    # =========================================================
    # CLOSE
    # =========================================================

    def close(self):

        if self.connection is not None:
            self.connection.close()

    # =========================================================
    # GET AIRPORTS
    # =========================================================

    def get_airports(self):

        self.cursor.execute(GET_AIRPORTS)

        return [
            row["airport"]
            for row in self.cursor.fetchall()
        ]

    # =========================================================
    # GET AIRLINES
    # =========================================================

    def get_airlines(self):

        self.cursor.execute(GET_AIRLINES)

        return [
            row["carrier"]
            for row in self.cursor.fetchall()
        ]

    # =========================================================
    # GET ROUTE
    # =========================================================

    def get_route(
        self,
        origin,
        destination
    ):

        self.cursor.execute(
            GET_ROUTE,
            (origin, destination)
        )

        route = self.cursor.fetchone()

        if route is None:
            raise ValueError(
                f"Route not found: {origin} → {destination}"
            )

        return route

    # =========================================================
    # CHECK ROUTE
    # =========================================================

    def route_exists(
        self,
        origin,
        destination
    ):

        try:
            self.get_route(origin, destination)
            return True
        except ValueError:
            return False

    # =========================================================
    # GET AIRPORT
    # =========================================================

    def get_airport(
        self,
        airport
    ):

        self.cursor.execute(
            GET_AIRPORT,
            (airport,)
        )

        airport_info = self.cursor.fetchone()

        if airport_info is None:
            raise ValueError(
                f"Airport not found: {airport}"
            )

        return airport_info

    # =========================================================
    # GET DESTINATIONS
    # =========================================================

    def get_destinations(
        self,
        origin
    ):

        self.cursor.execute("""

            SELECT destination

            FROM routes

            WHERE origin = ?

            ORDER BY destination

        """, (origin,))

        return [

            row["destination"]

            for row in self.cursor.fetchall()

        ]

    # =========================================================
    # SAVE PREDICTION
    # =========================================================

    def save_prediction(
        self,
        timestamp,
        airline,
        origin,
        destination,
        probability,
        prediction
    ):

        self.cursor.execute(

            INSERT_PREDICTION,

            (
                timestamp,
                airline,
                origin,
                destination,
                probability,
                prediction
            )

        )

        self.connection.commit()

    # =========================================================
    # GET PREDICTIONS
    # =========================================================

    def get_predictions(self):

        self.cursor.execute("""
            SELECT
                timestamp,
                airline,
                origin,
                destination,
                probability,
                prediction
            FROM predictions
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    # =========================================================
    # CLEAR PREDICTIONS
    # =========================================================

    def clear_predictions(self):

        self.cursor.execute("""
            DELETE FROM predictions
        """)

        self.connection.commit()