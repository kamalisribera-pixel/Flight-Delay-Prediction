from pathlib import Path

import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)


class FlightModelEvaluator:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(
        self,
        models: dict,
        X_test,
        y_test
    ):

        self.models = models

        self.X_test = X_test
        self.y_test = y_test

        self.output_path = Path("results")

        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )

    # =========================================================
    # EVALUATE SINGLE MODEL
    # =========================================================

    def evaluate_model(
        self,
        model_name,
        model
    ):

        print("=" * 60)
        print(f"EVALUATING {model_name.upper()}")
        print("=" * 60)

        predictions = model.predict(self.X_test)

        accuracy = accuracy_score(
            self.y_test,
            predictions
        )

        precision = precision_score(
            self.y_test,
            predictions
        )

        recall = recall_score(
            self.y_test,
            predictions
        )

        f1 = f1_score(
            self.y_test,
            predictions
        )

        roc_auc = roc_auc_score(
            self.y_test,
            predictions
        )

        report = classification_report(
            self.y_test,
            predictions
        )

        matrix = confusion_matrix(
            self.y_test,
            predictions
        )

        print(f"Accuracy : {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall   : {recall:.4f}")
        print(f"F1 Score : {f1:.4f}")
        print(f"ROC AUC  : {roc_auc:.4f}")

        self.save_metrics(
            model_name,
            accuracy,
            precision,
            recall,
            f1,
            roc_auc,
            report
        )

        self.plot_confusion_matrix(
            model_name,
            matrix
        )

    # =========================================================
    # SAVE METRICS
    # =========================================================

    def save_metrics(
        self,
        model_name,
        accuracy,
        precision,
        recall,
        f1,
        roc_auc,
        report
    ):

        file = self.output_path / f"{model_name}_metrics.txt"

        with open(file, "w") as f:

            f.write(f"Model : {model_name}\n\n")

            f.write(f"Accuracy : {accuracy:.4f}\n")
            f.write(f"Precision: {precision:.4f}\n")
            f.write(f"Recall   : {recall:.4f}\n")
            f.write(f"F1 Score : {f1:.4f}\n")
            f.write(f"ROC AUC  : {roc_auc:.4f}\n\n")

            f.write("Classification Report\n")
            f.write("=" * 60 + "\n")
            f.write(report)

        print(f"Saved : {file}")

    # =========================================================
    # CONFUSION MATRIX
    # =========================================================

    def plot_confusion_matrix(
        self,
        model_name,
        matrix
    ):

        display = ConfusionMatrixDisplay(
            confusion_matrix=matrix
        )

        display.plot()

        plt.tight_layout()

        filename = (
            self.output_path /
            f"{model_name}_confusion_matrix.png"
        )

        plt.savefig(
            filename,
            dpi=300
        )

        plt.close()

        print(f"Saved : {filename}")

    # =========================================================
    # RUN PIPELINE
    # =========================================================

    def run(self):

        for model_name, model in self.models.items():

            self.evaluate_model(
                model_name,
                model
            )

        print("=" * 60)
        print("MODEL EVALUATION COMPLETE")
        print("=" * 60)