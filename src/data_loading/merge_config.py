"""
merge_config: List of Dicts that contain left df, right df, left_on, and right_on. 
"""

merge_config = [
    {
        "right": "SummonerMatchTbl",
        "left_on": "SummonerMatchFk",
        "right_on": "SummonerMatchId",
        "desciption": " Link MatchStatsTbl with SummonerMatchTbl"
    },
    {
        "right": "MatchTbl",
        "left_on": "MatchFk",
        "right_on": "MatchId",
        "desciption": "Link SummonerMatchTbl with MatchTbl"
    },
    {
        "right": "ChampionTbl",
        "left_on": "ChampionFk",
        "right_on": "ChampionId",
        "desciption": " Link SummonerMatchTbl with ChampionTable"
    },
    {
        "right": "ChampionTbl",
        "left_on": "EnemyChampionFk",
        "right_on": "ChampionId",
        "desciption": "Link MatchStatsTbl with ChampionTable"
    },
    {
        "right": "RankTbl",
        "left_on": "RankFk",
        "right_on": "RankId",
        "desciption": "Link MatchTbl with RankTbl"
    }
]