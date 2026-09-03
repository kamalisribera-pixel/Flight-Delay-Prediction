from datetime import datetime

from src.database.database import FlightDatabase
from src.inference.feature_builder import FlightFeatureBuilder
from src.inference.predictor import FlightPredictor


class PredictService:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self):

        self.builder = FlightFeatureBuilder()

        self.predictor = FlightPredictor()

    # =========================================================
    # MAKE PREDICTION
    # =========================================================

    def predict(
        self,
        airline,
        origin,
        destination,
        departure_date,
        departure_time
    ):

        # -----------------------------------------------------
        # BUILD FEATURES
        # -----------------------------------------------------

        features = self.builder.build(

            airline=airline,

            origin=origin,

            destination=destination,

            departure_date=departure_date,

            departure_time=departure_time

        )

        # -----------------------------------------------------
        # MODEL PREDICTION
        # -----------------------------------------------------
        result = self.predictor.predict(
            features
        )

        # -----------------------------------------------------
        # SAVE PREDICTION
        # -----------------------------------------------------

        database = FlightDatabase()
        database.connect()

        try:

            database.save_prediction(

                timestamp=datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                airline=airline,

                origin=origin,

                destination=destination,

                probability=result["probability"],

                prediction=result["prediction"]

            )

        finally:

            database.close()

        return result

    # =========================================================
    # AIRLINES
    # =========================================================

    def get_airlines(self):

        database = FlightDatabase()
        database.connect()

        try:

            return database.get_airlines()

        finally:

            database.close()

    # =========================================================
    # AIRPORTS
    # =========================================================

    def get_airports(self):

        database = FlightDatabase()
        database.connect()

        try:

            return database.get_airports()

        finally:

            database.close()

    # =========================================================
    # DESTINATIONS
    # =========================================================

    def get_destinations(
        self,
        origin
    ):

        database = FlightDatabase()
        database.connect()

        try:

            return database.get_destinations(
                origin
            )

        finally:

            database.close()

    # =========================================================
    # CLOSE
    # =========================================================

    def close(self):

        self.builder.close()
