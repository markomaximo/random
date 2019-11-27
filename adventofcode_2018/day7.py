from collections import defaultdict
from funcy import flatten
from ipdb import set_trace

def load_instructions():
    with open('instructions.txt') as data_file:
        instructions = data_file.readlines()
    return [(i.split(' ')[1], i.split(' ')[7]) for i in instructions]

def follow_instructions_1(instructions):
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
print(follow_instructions_1(instructions))
# COMPLETED PART 1


class worker(object):
    def __init__(self):
        self.step = None
        self.done_at = -1
    
    def start_step(self, step, current_time):
        self.step = step
        self.done_at = current_time + 59 + ord(step) - 64

    def update_state(self, current_time):
        if self.step and self.done_at <= current_time:
            self.step = None

    def get_state(self):
        return self.step

def follow_instructions_2(instructions):
    dependencies = defaultdict(list)
    done = []
    not_started = []
    workers = [worker() for i in range(5)]
    current_time = 0

    for ins in instructions:
        dependencies[ins[1]].append(ins[0])

    not_started = sorted(set(flatten([[ins[0], ins[1]] for ins in instructions])))

    while len(done) < 26:
        done_this_second = []
        for i, w in enumerate(workers):
            prev_state = w.get_state()
            w.update_state(current_time)
            if w.get_state():
                continue
            if prev_state:
                done_this_second.append(prev_state)
                print('{} finished {} at {}'.format(i, prev_state, current_time))
                continue
            for step in not_started:
                if step not in dependencies:
                    not_started.remove(step)
                    w.start_step(step, current_time)
                    print('{} started {} at {}; done at {}'.format(i, w.get_state(), current_time, w.done_at))
                    break
                deps = dependencies[step]
                if all([True if s in done else False for s in deps]):
                    not_started.remove(step)
                    w.start_step(step, current_time)
                    print('{} started {} at {}; done at {}'.format(i, w.get_state(), current_time, w.done_at))
                    break
        done += done_this_second
        current_time += 1
    return current_time


print(follow_instructions_2(instructions))
# COMPLETED PART 2