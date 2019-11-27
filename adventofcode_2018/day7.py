from collections import defaultdict
from funcy import flatten
from ipdb import set_trace

def load_instructions():
    with open('instructions.txt') as data_file:
        instructions = data_file.readlines()
    return [(i.split(' ')[1], i.split(' ')[7]) for i in instructions]

def follow_instructions(instructions):
    dependencies = defaultdict(list)
    done = []
    not_done = []

    for ins in instructions:
        dependencies[ins[1]].append(ins[0])

    not_done = sorted(set(flatten([[ins[0], ins[1]] for ins in instructions])))

    while not_done:
        for step in not_done:
            if step not in dependencies:
                done.append(step)
                not_done.remove(step)
                break
            deps = dependencies[step]
            if all([True if s in done else False for s in deps]):
                done.append(step)
                not_done.remove(step)
                break
    return ''.join(done)


instructions = load_instructions()
print(follow_instructions(instructions))
# COMPLETED PART 1