from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from src.data_preprocessing.data_transforming import get_processing_pipeline

def get_rf_pipeline(COLS_CONFIG, rf_params=None):
    """
    Returns a full pipeline with preprocessing and Random Forest Classifier model
    """
    preprocessing = get_processing_pipeline(COLS_CONFIG)
    rf_model = RandomForestClassifier(**(rf_params or {}))

    model_pipeline = Pipeline([
        ('preprocessing', preprocessing),
        ('rf', rf_model)
    ])

    return model_pipeline
