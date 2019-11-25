from collections import defaultdict

def load_ids():
    with open('warehouse_ids.txt') as data_file:
        ids = data_file.readlines()
    return [id.strip() for id in ids]

def make_id_structure(ids):
    variants = {}
    for i in range(len(ids[0])):
        variants[i] = [idd[:i] + idd[i + 1:] for idd in ids]
    return variants

def find_near_matches(variants):
    for i, ids in variants.items():
        if len(set(ids)) == len(ids):
            continue
        counts = defaultdict(int)
        for idd in ids:
            counts[idd] += 1
        return [idd for idd, count in counts.items() if count > 1]

ids = load_ids()
variants = make_id_structure(ids)
near_matches = find_near_matches(variants)
print(near_matches)
