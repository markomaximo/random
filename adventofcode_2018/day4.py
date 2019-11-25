from pprint import pprint
from collections import defaultdict

def load_sleepies():
    with open('sleeping_guards.txt') as data_file:
        sleepies = data_file.readlines()
    sleepies = sorted(sleepies, key=lambda x: x.split(']')[0])
    return sleepies

def make_sleepy_structure(sleepies):
    guard_id = -1
    guard_sleepies = defaultdict(list)
    for row in sleepies:
        vals = row.split(' ')
        if len(vals) == 6:
            date, time, type, guard_id, __, __ = vals
            minute = int(time.split(':')[1][:-1])
        elif len(vals) == 4:
            date, time, type, __ = vals
            minute = int(time.split(':')[1][:-1])
            guard_sleepies[guard_id].append('{} {}'.format(minute, type))
        else:
            raise ValueError('Row not parsable: {}'.format(row))

    guard_minute_sleepies = defaultdict(lambda: defaultdict(int))
    for guard_id, events in guard_sleepies.items():
        sleepy_pairs = ' '.join(events)
        sleepy_pairs = sleepy_pairs.split('wakes')
        sleepy_pairs = [p.strip() for p in sleepy_pairs if p.strip()]
        sleepy_pairs = [(int(pair.split(' falls ')[0]), int(pair.split(' falls ')[1])) for pair in sleepy_pairs]
        for pair in sleepy_pairs:
            for minute in range(pair[0], pair[1]):
                guard_minute_sleepies[guard_id][minute] += 1

    return guard_minute_sleepies

def find_sleepiest_guard(guard_minute_sleepies):
    sleepiest_guard = max(guard_minute_sleepies, key=lambda guard_id: sum(guard_minute_sleepies[guard_id].values()))

    sleepiest_guard_record = guard_minute_sleepies[sleepiest_guard]
    sleepiest_minute = max(sleepiest_guard_record, key=lambda minute: sleepiest_guard_record[minute])

    return int(sleepiest_guard[1:]) * sleepiest_minute
    

sleepies = load_sleepies()
guard_minute_sleepies = make_sleepy_structure(sleepies)
print(find_sleepiest_guard(guard_minute_sleepies))
# COMPLETED PART 1

