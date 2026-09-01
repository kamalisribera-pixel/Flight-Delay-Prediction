from src.data import FlightDataLoader, FlightDataCleaner
from src.features import FlightFeatureEngineer
from src.models import FlightPreprocessor, FlightDataSplitter
from src.utils.paths import RAW_DATA

# =========================================================
# CONFIGURATION
# =========================================================

DATA_PATH = RAW_DATA / "T_ONTIME_REPORTING.csv"

# =========================================================
# MAIN
# =========================================================

def main():

    print("=" * 60)
    print("FLIGHT DELAY PREPROCESSING PIPELINE")
    print("=" * 60)

    # -----------------------------------------------------
    # LOAD DATA
    # -----------------------------------------------------

    loader = FlightDataLoader(DATA_PATH)
    df = loader.load()

    # -----------------------------------------------------
    # CLEAN DATA
    # -----------------------------------------------------

    cleaner = FlightDataCleaner(df)
    clean_df = cleaner.run()

    # -----------------------------------------------------
    # FEATURE ENGINEERING
    # -----------------------------------------------------

    engineer = FlightFeatureEngineer(clean_df)
    feature_df = engineer.run()

    # -----------------------------------------------------
    # PREPROCESS FEATURES
    # -----------------------------------------------------

    preprocessor = FlightPreprocessor(feature_df)

    X, y = preprocessor.run()

    # -----------------------------------------------------
    # TRAIN / TEST SPLIT
    # -----------------------------------------------------

    splitter = FlightDataSplitter(
        X=X,
        y=y
    )

    splitter.run()

    print("=" * 60)
    print("PREPROCESSING COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()