#!/usr/bin/env python3

signals = [line.strip() for line in open("day6_input").readlines()]

def marker(s, w):
    for i in range(len(s) - w +1):
        if len(set(s[i:i + w])) == w:
            return i + w

for signal in signals:
    print(f"Part 1: {marker(signal, 4)}")
    print(f"Part 2: {marker(signal, 14)}")
