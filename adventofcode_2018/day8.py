from pprint import pprint
from sys import stdin

def load_license(filename):
    with open(filename) as data_file:
        return [int(c) for c in data_file.readline().split()]

def parse_license(license, num_siblings):
    if num_siblings == 0:
        return [], 0

    num_children = license[0]
    num_meta = license[1]
    total_offset = 2

    children, chil_offset = parse_license(license[total_offset:], num_children)
    total_offset += chil_offset
    meta = license[total_offset: total_offset + num_meta]
    total_offset += num_meta
    siblings, sib_offset = parse_license(license[total_offset:], num_siblings - 1)
    total_offset += sib_offset

    node = {'num_children': num_children,
            'num_meta': num_meta,
            'meta': meta,
            'children': children}
    return [node] + siblings, total_offset

def add_meta(node):
    return sum(node['meta']) + sum([add_meta(child) for child in node['children']])


license = load_license('/Users/markus/Projects/random/adventofcode_2018/license.txt')
tree, _ = parse_license(license, 1)
print(add_meta(tree[0]))
# COMPLETED PART 1