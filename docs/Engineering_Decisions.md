# Engineering Decisions

## Flight Delay Prediction System

This document explains the major technical decisions made during the development of the Flight Delay Prediction System.

The purpose of this document is to record the reasoning behind architectural, machine learning, database, and software engineering choices made throughout the project.

---

# 1. Project Architecture Decision

## Decision

The project was structured into separate layers:
app/
src/
models/
database/
data/
results/
docs/


---

## Reason

During the initial development phase, it was possible to build the entire project inside a single Python script.

However, as the project expanded to include:

- data preprocessing
- model training
- inference
- database operations
- Streamlit interface

a modular structure became necessary.

Separating components improves:

- readability
- maintainability
- debugging
- future expansion

---

## Alternative Considered

A single Python file containing:

- data loading
- feature engineering
- training
- prediction
- UI code

---

## Why It Was Not Selected

A single-file architecture mixes multiple responsibilities.

Changes in one component could unintentionally affect another component.

For example:

- UI changes affecting prediction logic
- Database changes affecting application code
- Feature changes breaking inference

---

## Future Improvement

For a production-level system, the architecture can evolve into:


Frontend

↓

API Layer

↓

Machine Learning Service

↓

Database

↓

Monitoring System


---

# 2. Decision: Choosing Streamlit as Frontend

## Decision

Streamlit was selected for developing the user interface.

---

## Reason

The primary objective of this project was to demonstrate Machine Learning engineering rather than frontend development.

Streamlit provides:

- rapid application development
- native Python support
- easy ML integration
- built-in visualization components

---

## Alternative Considered

React + FastAPI architecture.

---

## Why It Was Not Selected

Although React provides a more production-like frontend, implementing a complete frontend would increase project complexity without improving the Machine Learning learning objectives.

---

## Future Improvement

The Streamlit application can later be replaced with:

- React frontend
- Mobile application
- API-based clients

while keeping the ML service unchanged.

---

# 3. Decision: Selecting Machine Learning Algorithms

## Decision

Multiple classification algorithms were implemented:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

---

## Reason

Instead of selecting one algorithm immediately, multiple approaches were compared.

Different algorithms capture different types of relationships:

| Model | Purpose |
|---|---|
| Logistic Regression | Baseline linear classifier |
| Decision Tree | Rule-based non-linear learning |
| Random Forest | Ensemble learning |
| Gradient Boosting | Sequential error correction |

---

## Alternative Considered

Using only one high-performance algorithm.

Example:

Random Forest only.

---

## Why It Was Not Selected

Without comparison, model selection would not be supported by experimental evidence.

Testing multiple models allowed evaluation based on actual performance.

---

# 4. Decision: Preventing Data Leakage

## Decision

Only information available before departure was used as model input.

---

## Reason

A real flight delay prediction system must make predictions before the flight occurs.

Including future information would create unrealistic performance.

---

## Examples of Removed Features

- Actual arrival time
- Actual delay duration
- Post-flight information

---

## Alternative Considered

Using every available dataset feature.

---

## Why It Was Not Selected

The model would appear highly accurate but would fail in real-world usage.

---

# 5. Decision: Database Selection

## Decision

SQLite was selected as the database.

---

## Reason

The application required storage for:

- prediction history
- timestamps
- user inputs
- prediction results

SQLite provides:

- lightweight storage
- zero configuration
- Python compatibility

---

## Alternative Considered

PostgreSQL / MySQL

---

## Why It Was Not Selected

For a student project, managing an external database server introduces unnecessary infrastructure complexity.

---

## Future Improvement

A production system could migrate to:

- PostgreSQL
- AWS RDS
- Cloud SQL

---

# 6. Decision: Saving Models Using Joblib

## Decision

Trained models were saved as `.joblib` files.

---

## Reason

Model training is computationally expensive.

Saving trained artifacts allows the application to:

- load models quickly
- avoid retraining
- separate training and inference

---

## Alternative Considered

Training the model every time the application starts.

---

## Why It Was Not Selected

This would:

- increase startup time
- waste computational resources
- reduce application usability

---

# 7. Decision: Model Evaluation Strategy

## Decision

Multiple evaluation metrics were used.

Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix

---

## Reason

Flight delay prediction is affected by class imbalance.

Accuracy alone does not show whether delayed flights are correctly detected.

---

## Alternative Considered

Evaluating only accuracy.

---

## Why It Was Not Selected

A model could achieve high accuracy while failing to identify delayed flights.

---

# 8. Decision: Prediction History Storage

## Decision

Every prediction is stored in SQLite.

---

## Reason

A practical application should maintain historical information.

This enables:

- analysis
- debugging
- future model monitoring

---

## Alternative Considered

Displaying predictions without storing them.

---

## Why It Was Not Selected

Information would be lost after application shutdown.

---

# 9. Decision: Separate Training and Inference

## Decision

Training and prediction were implemented separately.

---

## Reason

Training and inference have different responsibilities.

Training:

- data preparation
- model optimization
- evaluation

Inference:

- loading model
- processing user input
- generating prediction

---

## Benefit

This makes the system easier to maintain and deploy.

---

# Engineering Decision: Consistent Feature Representation Across Training and Optimization

## Problem

During the hyperparameter optimization stage, the optimizer initially loaded the raw training dataset instead of the processed feature matrix used during model training.

The raw dataset contained categorical string values such as:

```
origin = "Kona, HI"
destination = "Chicago, IL"
airline = "AA"
```

Machine learning algorithms such as Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting cannot directly process categorical string values. They require numerical feature representations.

This resulted in the following error:

```
ValueError: could not convert string to float: 'Kona, HI'
```

---

## Root Cause

The training pipeline and optimization pipeline were using different feature representations.

The intended machine learning pipeline was:

```
Raw Flight Data
        |
        v
Data Cleaning
        |
        v
Feature Engineering
        |
        v
Categorical Encoding
        |
        v
Processed Feature Matrix (X_train.npz)
        |
        v
Model Training
        |
        v
Model Optimization
        |
        v
Evaluation
```

However, the optimization pipeline was incorrectly using:

```
Raw Training Data (X_train.csv)
        |
        v
Hyperparameter Optimization
```

This created an inconsistency between model training and model optimization.

---

## Decision

The optimization pipeline was modified to consume the same processed feature artifact used during model training.

The optimizer now loads:

```
data/processed/X_train.npz
```

instead of:

```
data/processed/X_train.csv
```

The `.npz` file contains the encoded numerical feature matrix generated during preprocessing.

---

## Implementation

### Previous Implementation

```python
X_train = pd.read_csv(
    "data/processed/X_train.csv"
)
```

The above approach loaded raw categorical features.

---

### Updated Implementation

```python
from scipy.sparse import load_npz

X_train = load_npz(
    "data/processed/X_train.npz"
)
```

The optimizer now receives the same sparse numerical representation used during training.

---

## Reasoning

Machine learning pipelines require consistency between every stage.

Using different feature representations between training and optimization can lead to:

- Runtime failures
- Invalid model comparisons
- Training-serving inconsistencies
- Incorrect evaluation results
- Difficulty reproducing experiments

Therefore, the optimizer was designed to reuse the feature artifact generated by the preprocessing stage.

---

## Engineering Principle

> Every stage of a machine learning pipeline should consume the output artifact of the previous stage instead of independently recreating transformations.

This improves:

- Reproducibility
- Maintainability
- Debugging efficiency
- Experiment reliability

---

# Engineering Decision: Checkpoint-Based Hyperparameter Optimization

## Problem

The initial implementation used `RandomizedSearchCV` for hyperparameter optimization.

Although effective, long-running optimization experiments could lose all progress if the process was interrupted due to:

- System shutdown
- Hardware limitations
- Resource constraints
- Unexpected failures

Since model optimization can require significant CPU computation, restarting experiments from the beginning was inefficient.

---

## Decision

A custom checkpoint-based optimization system was implemented.

Instead of running all experiments as one process, each hyperparameter configuration is evaluated independently and saved immediately after completion.

The optimizer stores:

- Completed experiments
- Tested parameter combinations
- Evaluation scores
- Best performing parameters
- Best model checkpoint

---

## Optimization Workflow

```
Generate Hyperparameter Combination

              |
              v

Check Existing Checkpoint

              |
        +-----+-----+
        |           |
    Completed    New Experiment
        |           |
        v           v
      Skip       Train Model
                    |
                    v
              Evaluate Performance
                    |
                    v
              Save Checkpoint
                    |
                    v
              Update Best Model
```

---

## Benefits

The checkpoint-based approach provides:

- Recovery after interruptions
- No repeated experiments
- Better resource utilization
- Persistent experiment history
- Easier debugging and comparison

If optimization stops during execution, the next run continues from the last completed experiment instead of restarting.

---

## Engineering Principle

> Long-running machine learning experiments should be fault tolerant and recoverable.

This design makes the optimization stage more reliable when running on limited hardware resources.



# 10. Overall Engineering Philosophy

The main principle followed throughout development was:

> Build a system that is understandable, maintainable, and extendable rather than only focusing on model accuracy.

The project was developed not only as a Machine Learning experiment but as a complete software system.

The decisions made throughout the project were based on balancing:

- learning objectives
- engineering practices
- maintainability
- future scalability
