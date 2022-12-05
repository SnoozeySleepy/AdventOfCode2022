#!/usr/bin/env python3

import re
import copy

crates = []
with open("day5_input") as fh:
    # read in stacks of crates
    line = fh.readline()
    while line != '\n':
        crates.append(line)
        line = fh.readline()

    # extract the stack IDs
    # assumption: stack IDs are numerical and correspond to the stack number
    stackid = [int(x) for x in crates[-1].split()]

    stacks = list([] for _ in range(stackid[-1] + 1))
    for h in crates[:-1]:
        for id in stackid:
            crate = h[4 * (id - 1) + 1]
            if crate != ' ':
                stacks[id].append(crate)
    
    # read in rearrangement instructions
    rearrangement = [[int(x) for x in re.findall("\d+", line)] for line in fh.readlines()]

# for part 2
stacks_copy = copy.deepcopy(stacks)

def simulate(stacks, rearrangement, m, old_crane=True):
    for n,f,t in rearrangement:
        if old_crane:
            stacks[t][0:0] = stacks[f][:n][::-1]
        else:
            stacks[t][0:0] = stacks[f][:n]
        stacks[f] = stacks[f][n:]
    # assume all stacks have at least one crate
    return ''.join([stacks[i][0] for i in range(1, m + 1)])

# Part 1
print(simulate(stacks, rearrangement, len(stackid)))
# Part 2
print(simulate(stacks_copy, rearrangement, len(stackid), old_crane=False))
