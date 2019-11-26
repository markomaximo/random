import string

def load_polymer():
    with open('polymer.txt') as data_file:
        polymer = data_file.readline()
    return polymer

def react_polymer(polymer):
    polymer = list(polymer)
    i = 0
    while True:
        if i + 1 == len(polymer):
            break
        unit_1 = polymer[i]
        unit_2 = polymer[i + 1]
        if is_reactive(unit_1, unit_2):
            del polymer[i]
            del polymer[i]
            if i > 0:
                i -= 1
        else:
            i += 1
    return polymer

def is_reactive(unit_1, unit_2):
    if unit_1.lower() == unit_2.lower():
        if unit_1.isupper() and unit_2.islower():
            return True
        if unit_2.isupper() and unit_1.islower():
            return True
    return False

polymer = load_polymer()
reacted_polymer = react_polymer(polymer)
print(len(reacted_polymer))
# COMPLETED PART 1

def remove_unit_type(polymer, type):
    return [u for u in polymer if u.lower() != type.lower()]

def find_blocking_unit(polymer):
        return min([len(react_polymer(remove_unit_type(polymer, unit_type))) for unit_type in string.ascii_lowercase])

print(find_blocking_unit(polymer))
# COMPLETED PART 2