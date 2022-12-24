import json
from dataclasses import dataclass
from typing import List



def AOC_2022_day2_pt1(rounds):
    outcomes = {'A X': 0 + 3, 'A Y': 3 + 1, 'A Z': 6 + 2,
                'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3,
                'C X': 0 + 2, 'C Y': 3 + 3, 'C Z': 6 + 1}
    score = sum(outcomes[i] for i in rounds)
    return score


if __name__ == '__main__':
    with open('d2-input.txt', 'r') as f:
        rounds = f.read().split('\n')

    print(str(AOC_2022_day2_pt1(rounds)))