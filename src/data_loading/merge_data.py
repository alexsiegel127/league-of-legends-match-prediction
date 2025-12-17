import pandas as pd

def merge_data(tables, merge_config, verbose=True):
    """
    Merge multiple DataFrames based on merge_config

    Args:
        tables (dict): Keys = table names, Values = DataFrames
        merge_config (list): List of dicts with left/right table names and merge keys
        verbose (bool): If True, print the info, head, and shape of the merged DataFrame

    Returns:
        DataFrame: the fully merged DataFrame
    """

    #Check if tables or config is empty
    if not tables:
        raise ValueError("The 'tables' dictionary is empty. Please load your data before merging")
    
    if not merge_config:
        raise ValueError("Merge configuration is empty. Provide at least one merge step")
    
    #Create copy of MatchStatsTbl to start merge
    merged_data = tables['MatchStatsTbl'].copy()

    #Loop through config
    for config in merge_config:

        right_table = tables[config["right"]]
        #merge data
        merged_data = merged_data.merge(
            right_table, 
            left_on=config["left_on"],
            right_on=config["right_on"],
            how="left"
        )

        #Print step descriptiion if verbose
        if verbose:
            print(f"\nMerging: {config.get('description', config['right'])}")
            print(merged_data.info())
            print(merged_data.head())
            print(merged_data.shape)

    #Rename columns
    merged_data = merged_data.rename(columns={
        'ChampionName_x': 'ChampionName',
        'ChampionName_y': 'EnemyChampionName'
    })

    #Return DataFrame
    return merged_data



