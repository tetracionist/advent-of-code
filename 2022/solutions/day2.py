# first read the input and get the data into python
# this could be generic
import os
input_directory = f"{os.path.dirname(os.path.dirname(__file__))}\inputs"
day2_data = f"{input_directory}\day2.txt"

f = open(day2_data, "r")
strategy = f.read()

# A = X = Rock = 1
# B = Y = Paper = 2
# C = Z = Scissors = 3

# [A, Y]
# [B, Z]
# [C, X]

# strategy_list[x][0] is opponents choice
# strategy_list[x][1] is your choice

strategy_list = [i.split(' ') for i in strategy.splitlines()]
score_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
combos = [[['A', 'Z'], ['B', 'X'], ['C', 'Y']],
          [['A', 'X'], ['B', 'Y'], ['C', 'Z']],
          [['A', 'Y'], ['B', 'Z'], ['C', 'X']]]

#print(combos[2])

score_list = []
my_score_list = []

test_list = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

# for a win: game[1] + 6
# for a loss: game[1]
# for a draw: game[0] + game[1]

for game in strategy_list:
    score_list.append([score_dict[move] for move in game])
    if game in combos[0]:
        my_score_list.append(score_dict[game[1]])
    elif game in combos[1]:
        my_score_list.append(score_dict[game[1]] + 3)
    else:
        my_score_list.append(score_dict[game[1]] + 6)

# print(list(zip(my_score_list, score_list, strategy_list)))
print(sum(my_score_list))

# part two
# game[1] == X means loss
# game[1] == Y means draw
# game[1] == Z means win

move_list = []


for game in strategy_list:
    if game[1] == 'X':
        for i in combos[0]:
            if i[0] == game[0]:
                move_list.append([0, i[1]])

    elif game[1] == 'Y':
        for i in combos[1]:
            if i[0] == game[0]:
                move_list.append([3, i[1]])

    else:
        for i in combos[2]:
            if i[0] == game[0]:
                move_list.append([6, i[1]])
        

# print(move_list)

new_list = [i[0] + score_dict[i[1]] for i in move_list]
print(sum(new_list))

        
    



    






