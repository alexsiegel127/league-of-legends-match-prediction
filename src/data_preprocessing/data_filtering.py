import pandas as pd

def filter_data(data_frame, columns_to_keep, verbose=True):

    """
    Drops unnecessary features and filters queue type into classic 

    Args:
      data (DataFrame): Input DataFrame
      verbose (bool): If True, prints the resulting DataFrame after filtering and dropping

    Returns:
        DataFrame: Filtered and cleaned DataFrame
    """

    #Check for correct type 
    if not isinstance(data_frame, pd.DataFrame):
        raise TypeError("Data must be a pandas DataFrame")

    filtered_data = data_frame.copy()

    #Filter by QueueType
    filtered_data = filtered_data[filtered_data['QueueType'] .str.upper() == 'CLASSIC']

    #Make sure all columns exist
    missing_cols = [col for col in columns_to_keep if col not in data_frame.columns]

    if missing_cols:
        raise KeyError(f"the following required columns are missing: {missing_cols}")
    
    #Only keep specific columns
    filtered_data = filtered_data[columns_to_keep]

    #Print filtered table if verbose=True
    if verbose:
        filtered_data.info()
        print(filtered_data.head())
        print(filtered_data.shape)

    #Return DataFrame
    return filtered_data


