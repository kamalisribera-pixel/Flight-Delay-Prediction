from datetime import datetime, time

import pandas as pd

from src.database.database import FlightDatabase


class FlightFeatureBuilder:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self):

        self.db = FlightDatabase()
        self.db.connect()

    # =========================================================
    # CREATE DEPARTURE TIME BLOCK
    # =========================================================

    def create_departure_time_block(
        self,
        hour: int
    ):

        start = f"{hour:02d}00"
        end = f"{hour:02d}59"

        return f"{start}-{end}"

    # =========================================================
    # CREATE ARRIVAL TIME BLOCK
    # =========================================================

    def create_arrival_time_block(
        self,
        hour: int
    ):

        start = f"{hour:02d}00"
        end = f"{hour:02d}59"

        return f"{start}-{end}"

    
    # =========================================================
    # BUILD FEATURE VECTOR
    # =========================================================

    def build(
        self,
        airline,
        origin,
        destination,
        departure_date,
        departure_time
    ):

        # -----------------------------------------
        # ROUTE INFORMATION
        # -----------------------------------------

        route = self.db.get_route(
            origin,
            destination
        )

        if route is None:
            raise ValueError(
                "Route not found in database."
            )

        # -----------------------------------------
        # AIRPORT INFORMATION
        # -----------------------------------------

        origin_airport = self.db.get_airport(origin)

        destination_airport = self.db.get_airport(destination)

        # -----------------------------------------
        # DATE FEATURES
        # -----------------------------------------
        print(type(departure_date))
        print(departure_date)
        if isinstance(departure_date, str):

            travel_date = datetime.strptime(
                departure_date,
                "%Y-%m-%d"
            )

        else:

            travel_date = datetime.combine(
                departure_date,
                datetime.min.time()
            )

        day_of_month = travel_date.day

        # Monday = 1 ... Sunday = 7
        day_of_week = travel_date.weekday() + 1

        day_of_year = travel_date.timetuple().tm_yday

        weekend = int(
            day_of_week >= 6
        )

        # -----------------------------------------
        # TIME FEATURES
        # -----------------------------------------

        time = datetime.strptime(
            departure_time,
            "%H:%M"
        )

        departure = travel_date.replace(
            hour=time.hour,
            minute=time.minute
        )

        dep_hour = departure.hour

        crs_dep_time = (
            departure.hour * 100 +
            departure.minute
        )

        dep_time_blk = self.create_departure_time_block(
            dep_hour
        )

        elapsed = int(
            round(route["crs_elapsed_time"])
        )

        arrival = departure + pd.Timedelta(
            minutes=elapsed
        )

        crs_arr_time = (
            arrival.hour * 100 +
            arrival.minute
        )

        arr_time_blk = self.create_arrival_time_block(
            arrival.hour
        )          

        features = pd.DataFrame({

            "DAY_OF_MONTH": [day_of_month],
            "DAY_OF_WEEK": [day_of_week],

            "OP_UNIQUE_CARRIER": [airline],
            "OP_CARRIER_FL_NUM": [1],          # placeholder if you don't know flight number

            "ORIGIN_AIRPORT_ID": [origin_airport["airport_id"]],
            "ORIGIN": [origin],
            "ORIGIN_CITY_NAME": [origin_airport["city"]],
            "ORIGIN_STATE_ABR": [origin_airport["state"]],

            "DEST_AIRPORT_ID": [destination_airport["airport_id"]],
            "DEST": [destination],
            "DEST_CITY_NAME": [destination_airport["city"]],
            "DEST_STATE_ABR": [destination_airport["state"]],

            "CRS_DEP_TIME": [crs_dep_time],
            "DEP_TIME_BLK": [dep_time_blk],

            "CRS_ARR_TIME": [crs_arr_time],
            "ARR_TIME_BLK": [arr_time_blk],

            "CRS_ELAPSED_TIME": [elapsed],

            "DISTANCE": [route["distance"]],
            "DISTANCE_GROUP": [route["distance_group"]],

            "DEP_HOUR": [dep_hour],
            "ARR_HOUR": [arrival.hour],

            "IS_WEEKEND": [weekend],
            "DAY_OF_YEAR": [day_of_year],

            "DIVERTED": [0],
            "CANCELLED": [0],

        })

        print(features)

        return features