from collections import defaultdict
from funcy import flatten
from pprint import pprint
from sys import stdin
from math import floor


def load_input(filename):
    with open(filename) as data_file:
        return [l.strip() for l in data_file.readlines()]

def condition_input(r_input):
    
    return [int(l) for l in r_input]

def make_structure(input):
    
    return input

def get_fuel(mass):
    return floor(mass/3) - 2
    
def get_solution(structure):
    
    return sum([get_fuel(mass) for mass in structure])


r_input = load_input('/Users/markus/Projects/random/adventofcode_2019/day1_input.txt')
print(r_input)
conditioned_input = condition_input(r_input)
structure = make_structure(conditioned_input)
print(get_solution(structure))
# COMPLETED PART 1

def get_all_fuel(structure):
    all_fuel = 0
    for mass in structure:
        new_fuel = mass
        while True:
            new_fuel = get_fuel(new_fuel)
            if new_fuel <= 0:
                break
            all_fuel += new_fuel
    return all_fuel


print(get_all_fuel(structure))
# COMPLETED PART 2