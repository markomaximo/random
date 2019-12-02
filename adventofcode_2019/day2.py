from collections import defaultdict, deque, Counter
from funcy import flatten
from pprint import pprint
from sys import stdin
from math import floor


def load_input(filename):
    with open(filename) as data_file:
        return [l.strip() for l in data_file.readlines()]

def condition_input(r_input, noun, verb):
    code = [int(c) for c in r_input[0].split(',')]
    code[1] = noun
    code[2] = verb
    return code

def crawl_execute(instructions):
    current = 0
    while current < len(instructions):
        if instructions[current] == 99:
            return instructions
        if instructions[current] == 1:
            add_1 = instructions[current + 1]
            add_2 = instructions[current + 2]
            store = instructions[current + 3]
            instructions[store] = instructions[add_1] + instructions[add_2]
        if instructions[current] == 2:
            add_1 = instructions[current + 1]
            add_2 = instructions[current + 2]
            store = instructions[current + 3]
            instructions[store] = instructions[add_1] * instructions[add_2]
        current += 4
    return instructions

r_input = load_input('/Users/markus/Projects/random/adventofcode_2019/day2_input.txt')
conditioned_input = condition_input(r_input, 12, 2)
pprint(crawl_execute(conditioned_input)[0])


program = condition_input(r_input, 66, 35)
print(crawl_execute(program)[0])