# 1. TODO: Import the pandas library using its standard alias
import pandas as pd

player_data = {
    "Player_Name": ["Kobbie Mainoo", "Federico Valverde", "Alejandro Garnacho"],
    "Club": ["Manchester United", "Real Madrid", "Manchester United"],
    "Pass_Accuracy": [88.5, 91.2, 79.4],
    "Tackles_Won": [3.2, 2.8, 0.9]
}

# 2. TODO: Create a DataFrame called 'df' from the dictionary above
df = pd.DataFrame(data=player_data)

print(df)

passing_stats = df.loc[:, ["Player_Name", "Pass_Accuracy"]]
print(passing_stats)

defensive_players = df[df["Tackles_Won"] > 2]
print(defensive_players)