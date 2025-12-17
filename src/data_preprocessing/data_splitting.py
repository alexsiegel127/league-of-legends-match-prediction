import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(df, testSize, randomState, target_col: str = "Win",  verbose=True):

    """
    Splits the data into training and testing

    Args:
      df (DataFrame): Input DataFrame
      testSize (Float between 0 and 1): Proportion of samples allocated to test set
      randomState (Integer): Seed that controls random shuffling of data
      verbose (bool): If True, prints the resulting training and testing dataFrame

    Returns:
        tuple: (X_train, y_train, X_test, y_test)
    """

    #Make checks before calling train-test-split
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Data must be a pandas DataFrame")
    
    if not isinstance(testSize, float):
        raise TypeError("Test size must be a float")
    
    if not (isinstance(randomState, int) or randomState is None):
        raise TypeError("Random State must be an Integer or 'None'")
    
    if df.empty:
        raise ValueError("DataFrame can not be empty")
    
    if testSize < 0 or testSize > 1:
        raise ValueError("testSize must be between 0 and 1")
    
    #Now we can check if the target is in the data
    if not target_col in df.columns:
        raise KeyError(f"{target_col} column is not in the data frame")
    
    #Seperate target and features
    Y = df[target_col]
    X = df.drop(columns=[target_col])

    #Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=randomState, test_size=testSize)

    if verbose:
        print(f"X_train: {X_train.shape}, y_train: {y_train.shape}")
        print(f"X_test: {X_test.shape}, y_test: {y_test.shape}")

    return X_train, X_test, y_train, y_test




    





