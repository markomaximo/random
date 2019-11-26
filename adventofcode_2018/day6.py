"""
Notes:
Bound the area examined using min and max coordinates of the points on hand.
Any coord that has a nearest point on the border is eliminated for infinite area.
"""

from collections import defaultdict
from pprint import pprint

def load_coords():
    with open('coords.txt') as data_file:
        coords = data_file.readlines()
    coords = [(int(c.split(', ')[0]), int(c[:-1].split(', ')[1])) for c in coords]
    return coords

def get_min_max(coords):
    min_x = min(coords, key=lambda x: x[0])[0]
    max_x = max(coords, key=lambda x: x[0])[0]
    min_y = min(coords, key=lambda x: x[1])[1]
    max_y = max(coords, key=lambda x: x[1])[1]
    return min_x, max_x, min_y, max_y

def make_map(coords, min_max):
    min_x, max_x, min_y, max_y = min_max
    
    coord_map = defaultdict(lambda: defaultdict(int))
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            coord_distances = {i: get_distance((x, y), coord) for i, coord in enumerate(coords)}
            distances = sorted(list(coord_distances.values()))

            # If tie for min distance, no one gets it
            if distances[0] == distances[1]:
                coord_map[x][y] = -1
            else:
                coord_map[x][y] = min(coord_distances, key=lambda coord: coord_distances[coord])
    return coord_map

def get_distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

def get_largest_area(coord_map, min_max):
    # Get set of coords with infinite area
    min_x, max_x, min_y, max_y = min_max
    bad_coords = set()
    bad_coords.update([coord for coord in coord_map[min_x].values()])
    bad_coords.update([coord for coord in coord_map[max_x].values()])
    for x in range(min_x, max_x + 1):
        bad_coords.add(coord_map[x][min_y])
        bad_coords.add(coord_map[x][max_y])

    # Sum up coord areas
    coord_areas = defaultdict(int)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            coord_areas[coord_map[x][y]] += 1

    # Remove bad/infinite coords
    for bad_coord in bad_coords:
        del coord_areas[bad_coord]

    return max(coord_areas.values())

        
coords = load_coords()
min_max = get_min_max(coords)
coord_map = make_map(coords, min_max)
print(get_largest_area(coord_map, min_max))
# COMPLETED PART 1

