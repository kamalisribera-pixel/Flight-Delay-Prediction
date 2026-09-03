# Flight Delay Prediction

A machine learning application that predicts whether a scheduled U.S. domestic flight is likely to arrive 15 minutes or more late.

The project includes an end-to-end pipeline for data validation, cleaning, feature engineering, preprocessing, model training, hyperparameter optimization, evaluation, SQLite persistence, and prediction through a Streamlit web application.

## Features

- Data validation and profiling
- Data cleaning for cancelled, diverted, duplicate, and missing records
- Feature engineering for route, schedule, time, airport, and distance fields
- Exploratory and statistical analysis
- Sparse preprocessing with scaling and one-hot encoding
- Train/test splitting
- Multiple supervised classification models
- Checkpoint-based hyperparameter optimization
- Model evaluation reports and confusion matrices
- SQLite-backed prediction history
- Streamlit prediction dashboard

## Dataset

The project uses historical U.S. domestic flight data from the Bureau of Transportation Statistics On-Time Performance dataset.

The prediction target is:

```text
ARR_DEL15
```

`ARR_DEL15` indicates whether a flight arrived 15 minutes or more late.

| Value | Meaning |
|---:|---|
| 0 | Flight arrived less than 15 minutes late |
| 1 | Flight arrived 15 minutes or more late |

## Project Structure

```text
FDP/
├── app/
│   ├── assets/
│   └── pages/
├── data/
│   ├── processed/
│   └── raw/
├── database/
├── docs/
├── models/
├── reports/
├── results/
├── scripts/
├── src/
│   ├── analysis/
│   ├── data/
│   ├── database/
│   ├── features/
│   ├── inference/
│   ├── models/
│   └── utils/
├── main.py
├── README.md
└── requirements.txt
```

## Machine Learning Pipeline

```text
Raw dataset
  -> Data validation
  -> Data profiling
  -> Data cleaning
  -> Feature engineering
  -> Preprocessing
  -> Train/test split
  -> Model training
  -> Hyperparameter optimization
  -> Model evaluation
  -> Streamlit application
```

## Models

The training pipeline builds and evaluates:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

Evaluation includes accuracy, precision, recall, F1 score, ROC AUC, classification reports, and confusion matrices.

## Application Screenshots

### Home

![Flight Delay Prediction home page](docs/images/home.png)

### Prediction

![Flight delay prediction form](docs/images/prediction.png)

### Prediction History

![Prediction history page](docs/images/history.png)

### Model Performance

![Model performance dashboard](docs/images/performance.png)

### About

![About page](docs/images/about.png)

## Installation

Install the Python dependencies from the project root:

```bash
pip install -r requirements.txt
```

## Usage

Run the complete pipeline:

```bash
python main.py
```

Run individual stages:

```bash
python scripts/preprocess.py
python scripts/train.py
python scripts/optimize.py
python scripts/evaluate.py
python scripts/build_database.py
```

Run the Streamlit app:

```bash
streamlit run app/streamlit_app.py
```

## Outputs

- Trained models are saved in `models/`.
- Optimized model checkpoints and summaries are saved in `results/`.
- Evaluation metrics and confusion matrices are saved in `results/`.
- Prediction history is stored in `database/flight_delay.db`.

## Future Improvements

- Add automated tests
- Add REST API support with FastAPI
- Add Docker deployment
- Add weather and live flight data
- Add explainability with SHAP
- Compare additional models such as XGBoost, LightGBM, and CatBoost
