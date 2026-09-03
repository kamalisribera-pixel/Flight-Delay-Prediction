from pathlib import Path
import json
import itertools
import time

import joblib
import pandas as pd
from scipy.sparse import load_npz
from sklearn.base import clone
from sklearn.model_selection import StratifiedKFold, cross_val_score

try:
    from ._bootstrap import ensure_project_root_on_path
except ImportError:
    from _bootstrap import ensure_project_root_on_path

ensure_project_root_on_path()

from src.utils.constants import CV_FOLDS, RANDOM_STATE



# =========================================================
# PATHS
# =========================================================

RESULTS_DIR = Path("results")

CHECKPOINT_DIR = (
    RESULTS_DIR / "optimization_checkpoints"
)

CHECKPOINT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


SUMMARY_FILE = (
    RESULTS_DIR /
    "optimization_summary.csv"
)

SCORING_METHOD = f"{CV_FOLDS}-fold cross-validation f1"


# =========================================================
# OPTIMIZER
# =========================================================

class FlightCheckpointOptimizer:


    def __init__(
        self,
        models,
        X_train,
        y_train,
        scoring="f1"
    ):

        self.models = models

        self.X_train = X_train

        self.y_train = y_train

        self.scoring = scoring

        self.cv = StratifiedKFold(
            n_splits=CV_FOLDS,
            shuffle=True,
            random_state=RANDOM_STATE
        )


        self.parameters = {


            "Logistic Regression": {

                "C": [
                    0.01,
                    0.1,
                    1,
                    10
                ],

                "solver": [
                    "lbfgs",
                    "liblinear"
                ]

            },


            "Decision Tree": {

                "max_depth": [



                    10,
                    20,
                    30
                ],

                "min_samples_split": [
                    2,
                    5,
                    10
                ],

                "min_samples_leaf": [
                    1,
                    2,
                    4
                ]

            },


            "Random Forest": {

                "n_estimators": [
                    100,
                    200,
                    300
                ],

                "max_depth": [
                    None,
                    10,
                    20
                ],

                "min_samples_split": [
                    2,
                    5,
                    10
                ]

            },


            "Gradient Boosting": {

                "n_estimators": [
                    100,
                    200
                ],

                "learning_rate": [
                    0.01,
                    0.1,
                    0.2
                ],

                "max_depth": [
                    3,
                    5,
                    7
                ]

            }

        }



    # =====================================================
    # CHECKPOINT FILE
    # =====================================================

    def checkpoint_file(
        self,
        model_name
    ):

        name = (
            model_name
            .lower()
            .replace(" ", "_")
        )

        return (
            CHECKPOINT_DIR /
            f"{name}.json"
        )



    # =====================================================
    # MODEL SAVE FILE
    # =====================================================

    def model_file(
        self,
        model_name
    ):

        name = (
            model_name
            .lower()
            .replace(" ", "_")
        )

        return (
            RESULTS_DIR /
            f"{name}_best.joblib"
        )



    # =====================================================
    # LOAD CHECKPOINT
    # =====================================================

    def load_checkpoint(
        self,
        model_name
    ):

        file = self.checkpoint_file(
            model_name
        )

        if file.exists():

            with open(file) as f:

                state = json.load(f)

            if state.get("scoring_method") == SCORING_METHOD:
                return state


        return {

            "completed": [],

            "results": [],

            "best_score": 0,

            "best_params": None,

            "scoring_method": SCORING_METHOD

        }



    # =====================================================
    # SAVE CHECKPOINT
    # =====================================================

    def save_checkpoint(
        self,
        model_name,
        state
    ):

        file = self.checkpoint_file(
            model_name
        )


        with open(
            file,
            "w"
        ) as f:

            json.dump(
                state,
                f,
                indent=4
            )



    # =====================================================
    # PARAMETER GENERATOR
    # =====================================================

    def generate_parameters(
        self,
        model_name
    ):

        grid = (
            self.parameters[model_name]
        )


        keys = list(
            grid.keys()
        )


        values = list(
            grid.values()
        )


        combinations = []


        for combo in itertools.product(*values):

            combinations.append(

                dict(
                    zip(
                        keys,
                        combo
                    )
                )

            )


        return combinations



    # =====================================================
    # OPTIMIZE SINGLE MODEL
    # =====================================================

    def optimize_model(
        self,
        model_name,
        model
    ):


        print("=" * 60)

        print(
            f"OPTIMIZING {model_name}"
        )

        print("=" * 60)



        parameters = (
            self.generate_parameters(
                model_name
            )
        )


        state = (
            self.load_checkpoint(
                model_name
            )
        )


        completed = {

            str(x)

            for x in state["completed"]

        }



        best_model = None



        for index, params in enumerate(parameters):


            param_key = str(params)



            if param_key in completed:


                print(
                    f"Skipping completed:"
                )

                print(
                    params
                )

                continue



            print()

            print(
                f"Experiment {index+1}/{len(parameters)}"
            )

            print(
                params
            )



            current_model = clone(
                model
            )


            current_model.set_params(
                **params
            )

            if hasattr(current_model, "n_jobs"):
                current_model.set_params(n_jobs=1)


            start = time.time()


            scores = cross_val_score(
                current_model,
                self.X_train,
                self.y_train,
                scoring=self.scoring,
                cv=self.cv,
                n_jobs=1
            )

            score = float(scores.mean())


            duration = (
                time.time()
                - start
            )


            print(
                "Score:",
                score
            )

            print(
                "Time:",
                duration
            )



            state["completed"].append(
                param_key
            )


            state["results"].append(

                {

                    "params": params,

                    "score": score,

                    "time": duration

                }

            )



            if score > state["best_score"]:


                state["best_score"] = score

                state["best_params"] = params


                joblib.dump(

                    current_model.fit(
                        self.X_train,
                        self.y_train
                    ),

                    self.model_file(
                        model_name
                    )

                )


            self.save_checkpoint(

                model_name,

                state

            )



        return state



    # =====================================================
    # RUN ALL
    # =====================================================

    def run(self):


        summary = []



        for name, model in self.models.items():


            result = self.optimize_model(

                name,

                model

            )


            summary.append(

                {

                    "Model": name,

                    "Best Score":
                        result["best_score"],

                    "Best Parameters":
                        str(
                            result["best_params"]
                        )

                }

            )



        pd.DataFrame(
            summary
        ).to_csv(

            SUMMARY_FILE,

            index=False

        )


        print("=" * 60)

        print(
            "OPTIMIZATION COMPLETE"
        )

        print("=" * 60)


# =========================================================
# MAIN
# =========================================================

def main():
    
    # Load training data
   


    X_train = load_npz(
        "data/processed/X_train.npz"
    )

    y_train = pd.read_csv(
        "data/processed/y_train.csv"
    ).squeeze()
    
    models = {

        "Logistic Regression":
            joblib.load(
                "models/Logistic Regression.joblib"
            ),

        "Decision Tree":
            joblib.load(
                "models/decision_tree.joblib"
            ),

        "Random Forest":
            joblib.load(
                "models/random_forest.joblib"
            ),

        "Gradient Boosting":
            joblib.load(
                "models/gradient_boosting.joblib"
            )

    }
    
    # Run optimization
    optimizer = FlightCheckpointOptimizer(
        models=models,
        X_train=X_train,
        y_train=y_train,
        scoring="f1"
    )
    
    optimizer.run()


if __name__ == "__main__":
    main()


