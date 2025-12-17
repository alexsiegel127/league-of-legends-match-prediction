from src.data_loading.load_data import load_data
from src.data_loading.merge_config import merge_config
from src.data_loading.merge_data import merge_data
from src.data_preprocessing.data_filtering import filter_data
from src.data_preprocessing.data_splitting import split_data
from src.models.randomforest_pipeline import get_rf_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, classification_report
import argparse

#List of columns to keep. Includes the target
features = ['MinionsKilled', 'DmgDealt', 'DmgTaken', 'TurretDmgDealt', 
                    'TotalGold', 'Win', 'kills', 'deaths', 
                    'assists', 'CurrentMasteryPoints', 'DragonKills', 'BaronKills', 
                    'visionScore', 'GameDuration', 'ChampionName', 'EnemyChampionName', 'RankName']

#Parameter Variables
target = "Win"
verbose = True
random_state = 42
test_size = 0.2

#Column Configuration for processing pipeline
COLS_CONFIG = {
    "sym_cols": ['MinionsKilled', 'DmgDealt', 'DmgTaken', 'TotalGold', 'GameDuration'],
    "log_cols": ['TurretDmgDealt', 'kills', 'deaths', 'assists', 'CurrentMasteryPoints', 'visionScore'],
    "bin_cols": ['BaronKills'],
    "cap_cols": ['DragonKills'],
    "onehot_cols": ['RankName'],
    "targetenc_cols": ['ChampionName', 'EnemyChampionName']
}

#RandomForest Parameters
RF_PARAMS = {
    "max_depth": None,
    "min_samples_leaf": 1,
    "min_samples_split": 2,
    "n_estimators": 200
}

def main():
    # Create a parser object and provide a description
    parser = argparse.ArgumentParser(description="Runs model using optional verbose, random state, and test size arguments")

    # Add optional arguments
    parser.add_argument("--test_size", type=float, default=0.2, help="Portion of data reserved for the test set, between 0 and 1. Default value is 0.2")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    # Parse the arguments from the command line
    args = parser.parse_args()

    #Random state variable
    random_state = 42

    #Run project 
    run_project(args.test_size, random_state, args.verbose)


def run_project(test_size, random_state, verbose):

    #Start message
    print("Running project...\n")

    #Load and merge tables
    tables = load_data(verbose)
    merged_df = merge_data(tables, merge_config, verbose)

    #Start of preprocessing
    filtered_df = filter_data(merged_df, features, verbose)

    #Split data into training and testing
    X_train, X_test, y_train, y_test = split_data(filtered_df, test_size, random_state, target, verbose)

    #Get model pipeline
    rf_pipeline = get_rf_pipeline(COLS_CONFIG, RF_PARAMS)

    #Check CV accuracy
    cv_score = cross_val_score(rf_pipeline, X_train, y_train, cv=5)
    print(f"CV Score: {cv_score.mean()}")

    #Fit the pipeline
    rf_pipeline.fit(X_train, y_train)

    #Prediction using the test data
    y_pred = rf_pipeline.predict(X_test)
    print("Test Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()