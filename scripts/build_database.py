try:
    from ._bootstrap import ensure_project_root_on_path
except ImportError:
    from _bootstrap import ensure_project_root_on_path

ensure_project_root_on_path()

from src.data.loader import FlightDataLoader
from src.data.cleaner import FlightDataCleaner
from src.features.engineer import FlightFeatureEngineer
from src.database.database_builder import FlightDatabaseBuilder

# =========================================================
# CONFIGURATION
# =========================================================

DATA_PATH = "data/raw/T_ONTIME_REPORTING.csv"

# =========================================================
# MAIN
# =========================================================

def main():

    print("=" * 60)
    print("BUILDING FLIGHT DATABASE")
    print("=" * 60)

    loader = FlightDataLoader(DATA_PATH)
    df = loader.load()

    cleaner = FlightDataCleaner(df)
    clean_df = cleaner.run()

    engineer = FlightFeatureEngineer(clean_df)
    feature_df = engineer.run()

    database = FlightDatabaseBuilder(feature_df)
    database.run()

    print("=" * 60)
    print("DATABASE BUILD COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
