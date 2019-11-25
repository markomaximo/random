from collections import defaultdict

def load_ids():
    with open('warehouse_ids.txt') as data_file:
        return data_file.readlines()

def has_x(id, x):
    letters = defaultdict(int)
    for char in id:
        letters[char] += 1
    if x in letters.values():
        return True
    return False

def checksum(ids):
    twos = sum([1 for id in ids if has_x(id, 2)])
    threes = sum([1 for id in ids if has_x(id, 3)])
    return twos * threes

print(len(load_ids()))
print(checksum(load_ids()))