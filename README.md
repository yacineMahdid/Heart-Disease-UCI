Heart Disease EDA
==============================

Simple project where we do a exploratory data analysis on classification data from a [heart disease dataset](https://www.kaggle.com/ronitf/heart-disease-uci)

This is my first time using the [cookiecutter](https://drivendata.github.io/cookiecutter-data-science/) for datascience so I'm learning at the same time what the structure of the thing is.

## Setup
Use a virtualenvironment in order to run the analysis.
- `python3 -m venv env`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

## Dataset
The dataset `heart_kaggle.csv` comes from [Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci) and can be download as a zip file directly.

The variables are the following: 
- **age:** age
- **sex:** sex
- **cp:** chest pain type (4 values)
- **trestbps:** resting blood pressure
- **chol:** serum cholestoral in mg/dl
- **fbs:** fasting blood sugar > 120 mg/dl
- **restecg:** resting electrocardiographic results (values 0,1,2)
- **thalach:** maximum heart rate achieved
- **exang:** exercise induced angina
- **oldpeak:** oldpeak = ST depression induced by exercise relative to rest
- **slope:** the slope of the peak exercise ST segment
- **ca:** number of major vessels (0-3) colored by flourosopy
- **thal:** 3 = normal; 6 = fixed defect; 7 = reversable defect

### Caveat
> This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. In particular, the Cleveland database is the only one that has been used by ML researchers to
this date. The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4. 

This whole description is very messy. Something is off with the target.
What we actually care about is `cp`(chest pain) with value from 0 (no symptom) to 4.

The dataset is also a bit messy, we should use instead the dataset in [the UCI portal](https://archive.ics.uci.edu/ml/datasets/heart+Disease).