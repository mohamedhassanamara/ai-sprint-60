import numpy as np

# 1. The Data: 5 Midfielders, 4 Stats per 90 min (Pass Accuracy %, Tackles, Distance (km), Key Passes)
# Shape: (5, 4)
midfielders = np.array([
    [89.5, 2.1, 11.2, 1.5], # Bellingham
    [92.1, 1.5, 10.5, 2.1], # Modric
    [88.0, 3.5, 12.0, 0.8], # Tchouameni
    [94.2, 1.1, 11.8, 2.5], # Kroos
    [86.5, 4.2, 11.5, 0.5]  # Camavinga
])

# 2. League Averages for those exact 4 stats
# Shape: (4,)
league_avg = np.array([85.0, 2.0, 10.0, 1.0])

# 3. The Tactical Model: 4 Stats matching to 2 Systems (Ancelotti Control vs High Press)
# Shape: (4, 2)
tactics_weights = np.array([
    [0.6, 0.1],  # Pass Accuracy weight
    [0.1, 0.5],  # Tackles weight
    [0.1, 0.3],  # Distance weight
    [0.2, 0.1]   # Key Passes weight
])

# --- YOUR MISSION ---

# TODO 1: Use broadcasting to subtract the league average from the midfielders' stats.
# This will give us a "Value Over Average" matrix.
value_over_average = midfielders - league_avg

# TODO 2: Use matrix multiplication to multiply the 'value_over_average' matrix by the 'tactics_weights'.
# This will output the final tactical fit scores for all 5 players across both systems.
tactical_fit_scores = value_over_average @ tactics_weights

print(tactical_fit_scores)