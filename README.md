# ✈ Flight Delay Prediction

A Machine Learning application that predicts whether a flight will arrive **15 minutes or more late** using historical U.S. domestic flight data.

The project includes a complete end-to-end machine learning pipeline, from data preprocessing and feature engineering to model training, evaluation, database integration, and real-time prediction through a Streamlit web application.

---

# Features

- Data validation and profiling
- Data cleaning pipeline
- Feature engineering
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Data preprocessing
- Train-test splitting
- Multiple machine learning models
    - Logistic Regression
    - Decision Tree
    - Random Forest
    - Gradient Boosting
- Hyperparameter optimization
- Model evaluation
- SQLite database integration
- Real-time prediction service
- Streamlit web interface

---

# Dataset

Dataset:

**U.S. Department of Transportation - On-Time Performance Reporting**

Target Variable

```
ARR_DEL15
```

- 0 → Flight arrived on time
- 1 → Flight delayed by 15 minutes or more

---

# Project Structure

```text
FDP
│
├── app/
├── data/
│   ├── raw/
│   ├── processed/
│   └── reference/
│
├── database/
│
├── models/
│
├── reports/
│
├── results/
│
├── sql/
│
├── src/
│   ├── analysis/
│   ├── data/
│   ├── database/
│   ├── features/
│   ├── inference/
│   ├── models/
│   └── utils/
│
├── tests/
│
├── main.py
├── README.md
└── requirements.txt
```

---

# Machine Learning Pipeline

```
Raw Dataset
      ↓
Data Validation
      ↓
Data Profiling
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
EDA + Statistics
      ↓
Preprocessing
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Hyperparameter Optimization
      ↓
Model Evaluation
      ↓
Model Deployment
      ↓
Streamlit Application
```

---

# Models

The project trains multiple supervised learning models.

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

Each model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC
- Confusion Matrix

---

# Feature Engineering

Examples of engineered features include:

- Departure Hour
- Route Distance
- Distance Group
- Day of Week
- Day of Month
- Departure Time Block
- Arrival Time Block
- Airline
- Origin Airport
- Destination Airport

---

# Database

SQLite is used to store

- Airport information
- Route information
- Airline information
- Prediction history

---

# Technologies Used

## Programming Language

- Python

## Data Processing

- Pandas
- NumPy

## Machine Learning

- Scikit-learn

## Visualization

- Matplotlib

## Database

- SQLite

## Model Persistence

- Joblib

## Web Application

- Streamlit

---

# Installation

Clone the repository

```bash
git clone https://github.com/kamalisribera-pixel/Flight-Delay-Prediction
```

Move into the project

```bash
cd Flight-Delay-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Training Pipeline

```bash
python main.py
```

---

# Running the Streamlit App

```bash
streamlit run app/streamlit_app.py
```

---

# Results

Model evaluation reports are stored in

```
results/
```

Reports include

- Metrics
- Confusion Matrix
- Model Performance

---

# Future Improvements

- XGBoost
- LightGBM
- CatBoost
- Explainable AI using SHAP
- REST API
- Docker deployment
- Cloud deployment
- Flight tracking API int# ✈️ Flight Delay Prediction System

> An end-to-end Machine Learning system that predicts whether a scheduled commercial flight will experience a departure delay of **15 minutes or more** using historical U.S. flight data.

---

# 📖 Overview

The **Flight Delay Prediction System** is a production-style Machine Learning project that demonstrates the complete lifecycle of an ML application—from raw data preprocessing to an interactive prediction dashboard.

The project combines **Data Engineering, Feature Engineering, Machine Learning, Hyperparameter Optimization, Database Integration, and Web Application Development** into a single modular system.

Rather than focusing solely on model accuracy, the objective of this project was to build a complete, maintainable, and scalable Machine Learning solution that closely resembles an industry workflow.

---

# ✨ Features

- ✈️ Flight Delay Prediction
- 📊 Delay Probability Estimation
- 📈 Model Performance Dashboard
- 📜 Prediction History
- 💾 SQLite Database Integration
- ⚙️ Automated Feature Engineering
- 🤖 Multiple Machine Learning Models
- 🎯 Hyperparameter Optimization
- 🌌 Aerospace Inspired User Interface

---

# 🏗️ System Architecture

> *(Architecture diagram will be added here.)*

```text
Dataset
   │
   ▼
Data Validation
   │
   ▼
Data Cleaning
   │
   ▼
Feature Engineering
   │
   ▼
Data Preprocessing
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Prediction Service
   │
   ▼
SQLite Database
   │
   ▼
Streamlit Dashboard
```

---

# 📸 Application Screenshots

> Screenshots will be added after deployment.

- 🏠 Home Dashboard
- ✈️ Flight Prediction
- 📜 Prediction History
- 📊 Model Performance
- ℹ️ About Page

---

# ⚙️ Machine Learning Pipeline

## 1. Data Validation

- Dataset validation
- Missing value detection
- Duplicate detection
- Schema validation

---

## 2. Data Cleaning

- Removed cancelled flights
- Removed diverted flights
- Missing value handling
- Duplicate removal

---

## 3. Feature Engineering

- Temporal Features
- Airport Features
- Route Features
- Distance Features

---

## 4. Data Preprocessing

- ColumnTransformer
- OneHotEncoder
- StandardScaler
- Train/Test Split

---

## 5. Model Training

The following Machine Learning models were trained and evaluated.

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

---

## 6. Hyperparameter Optimization

- RandomizedSearchCV
- Cross Validation
- Best Parameter Selection

---

## 7. Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

# 📂 Dataset

### Source

U.S. Bureau of Transportation Statistics (BTS)

### Dataset Size

- **517,222 Flights**

### Prediction Target

Whether a scheduled flight will be delayed by **15 minutes or more**.

---

# 🛠️ Technology Stack

## Programming Languages

- Python
- SQL

---

## Libraries

- Pandas
- NumPy
- Scikit-Learn
- Matplotlib

---

## Framework

- Streamlit

---

## Database

- SQLite

---

## Model Serialization

- Joblib

---

# 📁 Project Structure

```text
FDP/

├── app/
│   ├── assets/
│   └── pages/
│
├── src/
│   ├── analysis/
│   ├── data/
│   ├── database/
│   ├── features/
│   ├── inference/
│   ├── models/
│   ├── utils/
│   └── visualization/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
├── docs/
├── models/
├── reports/
├── results/
├── scripts/
├── tests/
│
├── README.md
├── requirements.txt
└── main.py
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Flight-Delay-Prediction.git
```

---

## Navigate to Project

```bash
cd Flight-Delay-Prediction
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app/streamlit_app.py
```

---

# 🎯 Future Improvements

- REST API using FastAPI
- Docker Containerization
- Cloud Deployment
- Real-Time Flight API Integration
- Explainable AI (SHAP)
- Deep Learning Models
- Live Flight Tracking

---

# 👨‍💻 Author

**Lucky KB**

AI Engineering • Machine Learning • Software Engineering

---

# 📜 License

This project is released under the **MIT License**.

---

# ⭐ Acknowledgements

- U.S. Bureau of Transportation Statistics
- Scikit-Learn
- Streamlit
- Pandas
- NumPy
- Matplotlib

---

# License

This project is licensed under the MIT License.