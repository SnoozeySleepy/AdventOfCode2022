#!/usr/bin/env python3

sections = [ [list(map(int, s.split('-'))) for s in line.split(',')] for line in open("day4_input").read().splitlines()]

full_overlap = sum([a >= c and b <= d or c >= a and d <= b for (a,b),(c,d) in sections])
print(full_overlap)

overlap = sum([a <= c <= b or c <= a <= d for (a,b),(c,d) in sections])
print(overlap)