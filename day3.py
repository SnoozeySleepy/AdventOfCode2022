#!/usr/bin/env python3

import string
import itertools

def prio(x):
    return ''.join([string.ascii_lowercase, string.ascii_uppercase]).index(x) + 1

rucksacks = [line.strip() for line in open("day3_input").readlines()]
# part 1
common = itertools.chain(*[list(set(r[:len(r)//2]).intersection(set(r[len(r)//2:]))) for r in rucksacks])
print(sum(prio(c) for c in common))

# part 2
rs = [set(r) for r in rucksacks]
badges = itertools.chain(*[set.intersection(*r) for r in zip(rs[::3], rs[1::3], rs[2::3])])
print(sum(prio(b) for b in badges))
