# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np


prob_sum_dice = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
}

list_of_block_monopoly = [
        "Go",
        "Mediterranean Avenue",
        "Community Chest 1",
        "Baltic Avenue",
        "Income Tax",
        "Reading Railroad",
        "Oriental Avenue",
        "Chance 1",
        "Vermont Avenue",
        "Connecticut Avenue",
        "Jail Visiting",
        "St. Charles Place",
        "Electric Company",
        "States Avenue",
        "Virginia Avenue",
        "Pennsylvania Railroad",
        "St. James Palace",
        "Community Chest 2",
        "Tennessee Avenue",
        "New York Avenue",
        "Free Parking",
        "Kentucky Avenue",
        "Chance 2",
        "Indiana Avenue",
        "Illinois Avenue",
        "B. & O. Railroad",
        "Atlantic Avenue",
        "Ventnor Avenue",
        "Water Works",
        "Marvin Gardens",
        "Go To Jail",
        "Pacific Avenue",
        "North Carolina Avenue",
        "Comunity Chest 3",
        "Pennsylvania Avenue",
        "Short Line",
        "Chance 3",
        "Park Place",
        "Luxury Tax",
        "Boardwalk"
]


"""
    Calculating the probability of the next state give current state
"""
def generate_probability_on_one_roll(starting_point):
    # FOR INDEX REFERENCE YOU MAY SEE THE LIST OF BLOCK IN THE LIST
    # list_of_block_monopoly where 0 is go and so on
    if starting_point == 30:
        starting_point = 10
        
    prob_vector = [0]*40
    for i in prob_sum_dice:
        loc_nxt = (starting_point + i) % 40
        # When the next dice throw to Community Chest
        if loc_nxt == 2 or loc_nxt == 17 or loc_nxt == 33:
            prob_vector[loc_nxt] += (15/17) * prob_sum_dice[i]
            prob_vector[0] += (1/17) * prob_sum_dice[i]
            prob_vector[30] += (1/17) * prob_sum_dice[i]
        # When the next dice throw to Chance
        elif loc_nxt == 7 or loc_nxt == 22 or loc_nxt == 36:
            prob_vector[loc_nxt] += (7/16) * prob_sum_dice[i]
            prob_vector[0] += (1/16) * prob_sum_dice[i]
            prob_vector[24] += (1/16) * prob_sum_dice[i]
            prob_vector[11] += (1/16) * prob_sum_dice[i]
            prob_vector[30] += (1/16) * prob_sum_dice[i]
            prob_vector[5] += (1/16) * prob_sum_dice[i]
            prob_vector[39] += (1/16) * prob_sum_dice[i]
            # The conditional
            if loc_nxt == 7:
                prob_vector[12] += (1/16) * prob_sum_dice[i]
                prob_vector[15] += (1/16) * prob_sum_dice[i]
                prob_vector[4] += (1/16) * prob_sum_dice[i]
            elif loc_nxt == 22:
                prob_vector[28] += (1/16) * prob_sum_dice[i]
                prob_vector[25] += (1/16) * prob_sum_dice[i]
                prob_vector[19] += (1/16) * prob_sum_dice[i]
            elif loc_nxt == 36:
                prob_vector[12] += (1/16) * prob_sum_dice[i]
                prob_vector[5] += (1/16) * prob_sum_dice[i]
                prob_vector[33] += (1/16) * prob_sum_dice[i]
        else:
            prob_vector[loc_nxt] += prob_sum_dice[i]
    return prob_vector
                
"""
    Creating transition Matricx
"""
MAT_PROB = []

for i in range(40):
    MAT_PROB.append(generate_probability_on_one_roll(i))
        
trans_prob = np.array(MAT_PROB)


"""
    Calculating the distribution
"""

A=np.append(trans_prob.transpose()-np.identity(40),[[1] * 40],axis=0)
b = np.array([0]*40 + [1]).transpose()

prob_dist_monopoly = np.linalg.solve(A.transpose().dot(A), A.transpose().dot(b))


for i, j in zip(list_of_block_monopoly,prob_dist_monopoly):
    print(i, end=': ')
    print(j)
    

