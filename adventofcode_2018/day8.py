from pprint import pprint

def load_license():
    with open('license.txt') as data_file:
        return data_file.readline().split()

def parse_license(license, num_siblings):
    if num_siblings == 0:
        return [], 0

    num_children = license[0]
    num_meta = license[1]
    print('num_chil: {}, num_meta: {}'.format(num_children, num_meta))
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


license = load_license()
tree = parse_license(license, 1)
pprint(tree)