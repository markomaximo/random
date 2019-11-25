from collections import defaultdict

def load_claims():
    with open('claims.txt') as data_file:
        claims_raw = data_file.readlines()
    claims = []
    for raw_claim in claims_raw:
        xylengths = raw_claim.split(' ')[2:]
        x_start = int(xylengths[0].split(',')[0])
        y_start = int(xylengths[0].split(',')[1][:-1])
        x_end = x_start + int(xylengths[1].split('x')[0])
        y_end = y_start + int(xylengths[1].split('x')[1])
        claims.append((x_start, y_start, x_end, y_end))
    return claims


def make_claims_structure(claims):
    claims_map = defaultdict(lambda: defaultdict(int))
    for claim in claims:
        for x in range(claim[0], claim[2]):
            for y in range(claim[1], claim[3]):
                claims_map[x][y] += 1
    return claims_map

def count_overlaps(claims_map):
    return sum([sum([1 for claim in col.values() if claim > 1]) for col in claims_map.values()])


claims = load_claims()
claims_map = make_claims_structure(claims)
print(count_overlaps(claims_map))