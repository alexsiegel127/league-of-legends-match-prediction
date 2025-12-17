
# **League of Legends Match Prediction Model**

# Project Overview
This project is an end-to-end machine learning solution designed to predict the outcome of a League of Legends match using individual player statistics such as total gold earned, damage dealt, champion selection, and other in-game metrics.

The project applies data preprocessing pipelines and multiple machine learning algorithms to identify patterns associated with match outcomes. It is intended as an **analytical and educational tool** for understanding competitive match data rather than a real-time gameplay assistant.

The full preprocessing workflow, model selection process, and hyperparameter tuning are documented in `notebook/asiegel7_LOLProject_Notebook.ipynb`. This repository contains the implementation of the best-performing model in a standalone Python environment. A written report summarizing findings and conclusions is included in the `report` directory.

# Features
- Data Preprocessing Pipeline: Feature scaling, Logarithmic transformations, categorical encoding, and handling of special features using scikit-learn pipelines.
- Model Agnostic: Several classification models trained and fine-tuned, including Logistic Regression, Random Forest, and MLPClassifier
- Evaluation Metrics: Classification report on Accuracy, Precision, Recall, and F1 scores


# Prerequisites
Python 3.10 or later is required
* Category Encoders

    `pip install category_encoders`


# Installation
1. Clone the repo

    `git clone https://github.com/alexsiegel127/league-of-legends-match-prediction.git`

2. Install Category Encoders packages

    `pip install category_encoders`

# Usage
1. **Basic Execution**

    To run the main training and evaluation script:

    `python main.py`



2. **Setting the Test Size** 

    The default test size is 0.2. To change this value, use the optional `--test_size` flag:

    `python main.py --test_size (value)`



3. **Enabling Verbose Mode**

    To get more detailed output during execution, use the `-v` or `--verbose` flag:

    `python main.py --verbose`

# The Data
The dataset used for training was downloaded from [Kaggle.com](https://www.kaggle.com/datasets/nathansmallcalder/lol-match-history-and-summoner-data-80k-matches?resource=download). 

Nathan Smallcalder, the owner of the dataset, used an API from RiotGames, the developer of League of Legends, to obtain over 80,000 match records. This dataset captures a wide range of in-game statistics, such as champion selection, player performance metrics, match outcomes, and more. The raw data is split among seven CSV files, five of which are located in the `data` folder to be used. Some notable features of the dataset are:
* `TotalGold`: Total amount of gold a player has earned  
* `TurretDmgDealt`: Amount of damage a player has dealt to enemy turrets
* `ChampionName`: Champion that a player has selected for a match
* `DmgTaken`: Amount of damage a player has taken from enemies
* `Win`: 1 if a player has won a match, 0 otherwise - *this is the feature our model predicts*

**Note on Data Splitting**: The data is carefully split into training and testing sets to prevent data leakage and ensure our model generalizes well to unseen data.

# Model and Methodology
* The core of my solution uses a **RandomForestClassifier**, known for its high accuracy, robustness, and versatility. It is an ensemble learning method that works by creating multiple random subsets of the training data and building many decision trees from these randomized datasets. The final prediction is determined using the majority vote of the trees.
* The best model achieved accuracy, precision, recall, and f1 scores of approximately 0.96 on the test set, indicating a strong fit to the data.

# Roadmap & Contributing
Proposed features for this project include:
* Adding a changelog
* Evaluating hyper-specific features on model accuracy
* Retrieving data directly using the Riot Games' API for testing

Contributions are welcome and greatly appreciated. To contribute, please fork the repository, create a feature branch. commit your changes, push to the branch, and open a pull request. Refer to the [GitHub document on contributing](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) for more details.

# License
This project is licensed under the MIT License - See the LICENSE file for details.

# Contact
Alex Siegel - https://www.linkedin.com/in/alexsiegel127/ | alexsiegel127@gmail.com

Project Link: [Project Link](https://github.com/alexsiegel127/league-of-legends-match-prediction)