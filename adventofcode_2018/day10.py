from statistics import mean
import pandas as pd
from collections import Counter
from sys import stdin


def load_input(filename):
    with open(filename) as data_file:
        data = data_file.readlines()
    positions = [( int(d[10:16]), int(d[18:24])) for d in data]
    deltas = [( int(d[36:38]), int(d[40:42])) for d in data]
    positions = pd.DataFrame(positions)
    deltas = pd.DataFrame(deltas)
    return positions, deltas

def get_entropy2(positions):
    y_counts = Counter(positions.iloc[:, 1])
    return mean([c[1] for c in y_counts.most_common(3)])

def print_out(positions):
    row_string = ''
    for y in range(positions[1].min(), positions[1].max() + 1):
        for x in range(positions[0].min(), positions[0].max() + 1):
            if ((positions[0] == x) & (positions[1] == y)).any():
                row_string += 'X'
            else:
                row_string += ' '
        row_string += '\n'
    print(row_string)


positions, deltas = load_input('sky_lights.txt')
steps = 1
while True:
    if steps % 100 == 0:
        print('step: {}'.format(steps))
    positions = positions + deltas
    if get_entropy2(positions) > 50:
        print('found low entropy on step: {}'.format(steps))
        print_out(positions)
        stdin.readline()
    steps += 1