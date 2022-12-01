#!/usr/bin/env python3

with open("day1_input") as fh:
    m = [x.strip() for x in fh.readlines()]

calories_per_elf = [ sum(z) for z in [[int(y) for y in x.split(';')] for x in ';'.join(m).split(';;')] ]
print( max(calories_per_elf) )
print( sum(sorted(calories_per_elf, reverse=True)[:3]) )