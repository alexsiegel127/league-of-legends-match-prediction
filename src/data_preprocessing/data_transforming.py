from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from category_encoders import TargetEncoder
import numpy as np

#Defined methods for transformation
def log_transformation(x):
    return np.log1p(x)

def binarize(x):
    return (x > 0).astype(int)

def cap_values(x):
    return np.clip(x, None, 4)

#Create pipelines for each transformation 
symmetric_pipeline = Pipeline([
    ('standardize', StandardScaler())
])

#For skewed num columns
log_pipeline = Pipeline([
    ('log', FunctionTransformer(log_transformation)),
    ('standardize', StandardScaler())
])

#Binary Pipeline
binary_pipeline = Pipeline([
    ('binarize', FunctionTransformer(binarize)),
    ('standardize', StandardScaler())
])

#Capped Pipeline
capped_pipeline = Pipeline([
    ('cap', FunctionTransformer(cap_values)),
    ('standardize', StandardScaler())
])

#Preprocessing pipeline
def get_processing_pipeline(COLS_CONFIG):
    """
    Returns a ColumnTransformer pipeline for preprocessing data.

    Args:
        COLS_CONFIG (dict): keys = transformation names, values = lists of column names

    Returns:
        ColumnTransformer: Preprocessing pipeline
    """
    
    processing_pipeline = ColumnTransformer([
        ('symmetric', symmetric_pipeline, COLS_CONFIG['sym_cols']),
        ('log', log_pipeline, COLS_CONFIG['log_cols']),
        ('binary', binary_pipeline, COLS_CONFIG['bin_cols']),
        ('capped', capped_pipeline, COLS_CONFIG['cap_cols']),
        ('onehot', OneHotEncoder(max_categories=11, handle_unknown='infrequent_if_exist'), COLS_CONFIG['onehot_cols']),
        ('target', TargetEncoder(cols=COLS_CONFIG['targetenc_cols']), COLS_CONFIG['targetenc_cols'])
    ])

    return processing_pipeline

    
