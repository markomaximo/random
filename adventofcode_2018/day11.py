# Grid serial number is 9995
from collections import defaultdict
from funcy import flatten
import pandas as pd
from pprint import pprint


def make_fuel_grid(grid_serial):
    grid = defaultdict(lambda: defaultdict(int))
    for x in range(1, 301):
        for y in range(1, 301):
            power = (((x + 10) * y) + grid_serial) * (x + 10)
            power_str = str(power)
            if len(power_str) < 3:
                power = -5
            else:
                power = int(power_str[-3]) - 5
            grid[x][y] = power
    return grid

def find_highest_fuel_cells(grid, subgrid):
    max_power = -100
    max_power_i = (0, 0)
    for x in range(1, 302 - subgrid):
        for y in range(1, 302 - subgrid):
            this_power = sum([sum([grid[this_x][this_y] for this_x in range(x, x + subgrid)]) for this_y in range(y, y + subgrid)])
            if this_power > max_power:
                # print(this_power)
                # print((x,y))
                max_power = this_power
                max_power_i = (x, y)
    return (max_power, max_power_i)    

grid = make_fuel_grid(9995)
print(find_highest_fuel_cells(grid, 3))
# COMPLETED PART 1


def find_highest_subgrid(grid):
    max_power = -10000
    for subgrid in range(1, 301):
        print('looking at subgrids of {}x{}'.format(subgrid, subgrid))
        this_power, this_power_i = find_highest_fuel_cells(grid, subgrid)
        if this_power > max_power:
            print('new max power: {}'.format(this_power))
            print('x,y: {}'.format(this_power_i))
            max_power = this_power
            max_power_i = this_power_i
            max_power_subgrid = subgrid
    return (max_power, max_power_i, max_power_subgrid)

print(find_highest_subgrid(grid))
# Completed PART 2