try:
    from ._bootstrap import ensure_project_root_on_path
except ImportError:
    from _bootstrap import ensure_project_root_on_path

ensure_project_root_on_path()

from src.data.loader import FlightDataLoader
from src.data.cleaner import FlightDataCleaner

from src.features.engineer import FlightFeatureEngineer

from src.analysis.eda import FlightEDA
from src.analysis.statistics import FlightStatistics

DATA_PATH = "data/raw/T_ONTIME_REPORTING.csv"

def main():

    loader = FlightDataLoader(DATA_PATH)
    df = loader.load()

    cleaner = FlightDataCleaner(df)
    clean_df = cleaner.run()

    engineer = FlightFeatureEngineer(clean_df)
    feature_df = engineer.run()

    FlightEDA(feature_df).run()
    FlightStatistics(feature_df).run()


if __name__ == "__main__":
    main()
