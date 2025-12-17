import pandas as pd
import os

def load_data(verbose=True):

    """
    Load CSV files from /data folder

    Args:
      verbose (bool): If True, prints info, head, and shape of each DataFrame 

    Returns:
        tables (dict): Keys = table names, Values = DataFrames 
    """

    #Base directory of the project
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..')) 

    #Path to data folder
    DATA_DIR = os.path.join(BASE_DIR, "data")

    # CSV file mapping
    csv_files = {
        "MatchStatsTbl" : "MatchStatsTbl.csv",
        "SummonerMatchTbl": "SummonerMatchTbl.csv",
        "MatchTbl": "MatchTbl.csv",
        "ChampionTbl": "ChampionTbl.csv",
        "RankTbl": "RankTbl.csv"
    }

    #Store loaded tables
    tables = {}

    #Loop through CSV files
    for table_name, file_name in csv_files.items():

        #Get file path
        file_path = os.path.join(DATA_DIR, file_name)

        #Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist")
        
        #Read file and assign it to DataFrame variable
        DataFrame = pd.read_csv(file_path)
        tables[table_name] = DataFrame

        #Print table info if Verbose=True
        if verbose:
            DataFrame.info()
            print(DataFrame.head())
            print(DataFrame.shape)

    return tables


