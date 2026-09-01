# =========================================================
# DATASET
# =========================================================

TARGET_COLUMN = "IS_DELAYED"

# =========================================================
# TRAINING
# =========================================================

RANDOM_STATE = 42

TEST_SIZE = 0.20

CV_FOLDS = 5

N_ITER_SEARCH = 10

SCORING = "f1"

# =========================================================
# MODELS
# =========================================================

LOGISTIC_REGRESSION = "logistic_regression.joblib"

DECISION_TREE = "decision_tree.joblib"

RANDOM_FOREST = "random_forest.joblib"

GRADIENT_BOOSTING = "gradient_boosting.joblib"

PREPROCESSOR = "preprocessor.pkl"

# =========================================================
# PREDICTION
# =========================================================

DELAY_THRESHOLD = 15