from src.data.loader import FlightDataLoader
from src.data.validator import FlightDataValidator
from src.data.profiler import FlightDataProfiler
from src.data.cleaner import FlightDataCleaner
from src.features.engineer import FlightFeatureEngineer
from src.analysis.eda import FlightEDA
from src.analysis.statistics import FlightStatistics
from src.models.preprocessor import FlightPreprocessor
from src.models.splitter import FlightDataSplitter
from src.models.trainer import FlightModelTrainer
from src.models.evaluator import FlightModelEvaluator

DATA_PATH = "data\\raw\\T_ONTIME_REPORTING.csv"


def main():

    # ==========================
    # Load Dataset
    # ==========================
    loader = FlightDataLoader(DATA_PATH)
    df = loader.load()

    # ==========================
    # Validate Dataset
    # ==========================
    FlightDataValidator.validate(df)

    # ==========================
    # Profile Dataset
    # ==========================
    profiler = FlightDataProfiler(df)
    profiler.run()

    # ==========================
    # Clean Dataset
    # ==========================
    cleaner = FlightDataCleaner(df)
    clean_df = cleaner.run()

    # ==========================
    # Feature Engineering
    # ==========================
    engineer = FlightFeatureEngineer(clean_df)
    feature_df = engineer.run()

    # ==========================
    # Exploratory Data Analysis
    # ==========================
    eda = FlightEDA(feature_df)
    eda.run()

    # ==========================
    # Statistical Analysis
    # ==========================
    stats = FlightStatistics(feature_df)
    stats.run()

    # -------------------------
    # PREPROCESSING
    # -------------------------

    preprocessor = FlightPreprocessor(feature_df)

    X, y = preprocessor.run()

    # -------------------------
    # TRAIN TEST SPLIT
    # -------------------------

    splitter = FlightDataSplitter(X, y)

    X_train, X_test, y_train, y_test = splitter.run()

    # -------------------------
    # MODEL TRAINING
    # -------------------------

    trainer = FlightModelTrainer(X_train, y_train)

    models = trainer.run()

    evaluator = FlightModelEvaluator(
        models=models,
        X_test=X_test,
        y_test=y_test
    )

    evaluator.run()

if __name__ == "__main__":
    main()