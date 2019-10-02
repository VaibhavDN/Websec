import pandas as pd

def find_in_database(games_name_to_search):
    data = pd.read_csv("games_keywords.csv")

    names_of_games = data.iloc[:, 0]
    for i in range(0, len(names_of_games), 1):
        for word in str(names_of_games[i]).lower().split(' '):
            if games_name_to_search.lower() == word:
                print("Found: " + games_name_to_search + " at: " + str(i) + " in: " + names_of_games[i])
                return 0
            else:
                pass
    return 1
