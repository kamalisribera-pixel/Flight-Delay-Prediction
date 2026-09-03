try:
    from ._bootstrap import ensure_project_root_on_path
except ImportError:
    from _bootstrap import ensure_project_root_on_path

ensure_project_root_on_path()

from src.data.loader import FlightDataLoader
from src.data.validator import FlightDataValidator
from src.data.profiler import FlightDataProfiler

DATA_PATH = "data/raw/T_ONTIME_REPORTING.csv"

def main():

    loader = FlightDataLoader(DATA_PATH)
    df = loader.load()

    FlightDataValidator.validate(df)

    profiler = FlightDataProfiler(df)
    profiler.run()


if __name__ == "__main__":
    main()
