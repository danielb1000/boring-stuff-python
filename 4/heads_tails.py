"""
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.
"""

import random
streaks_of_6 = 0

for _ in range(10000):
    experiment = random.choices("HT", k=100)

    in_a_row = 1
    for i in range(len(experiment)-1):
        if experiment[i] == experiment[i+1]:
            in_a_row += 1
        else:
            in_a_row = 1
        if in_a_row == 6:
                streaks_of_6 += 1
                in_a_row = 1

    print("Streaks of 6 so far:", streaks_of_6)
print("Total streaks of 6:", streaks_of_6)