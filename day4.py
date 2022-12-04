#!/usr/bin/env python3

sections = [ [list(map(int, s.split('-'))) for s in line.split(',')] for line in open("day4_input").read().splitlines()]

# Part 1 full overlap
print(sum([a >= c and b <= d or c >= a and d <= b for (a,b),(c,d) in sections]))
# Part 2 any overlap
print(sum([a <= c <= b or c <= a <= d for (a,b),(c,d) in sections]))
