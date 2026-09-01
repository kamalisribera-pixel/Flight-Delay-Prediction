import pandas as pd


class FlightDataValidator:

    REQUIRED_COLUMNS = [
        "YEAR",
        "MONTH",
        "DAY_OF_MONTH",
        "FL_DATE",

        "ORIGIN",
        "DEST",

        "CRS_DEP_TIME",
        "DEP_TIME",

        "CRS_ARR_TIME",
        "ARR_TIME",

        "ARR_DELAY",
        "ARR_DEL15",

        "CANCELLED",
        "DIVERTED",
    ]


    @classmethod
    def validate(cls, df: pd.DataFrame):

        print("=" * 60)
        print("Validating Dataset")
        print("=" * 60)

        missing = []

        for column in cls.REQUIRED_COLUMNS:

            if column not in df.columns:
                missing.append(column)

        if missing:

            raise ValueError(
                f"Missing required columns:\n{missing}"
            )

        print("Required columns exist.")