#!/usr/bin/env python3

score = {
    'X' : { 'A':1+3, 'B':1+0, 'C':1+6 }, # Rock defeats Scissors
    'Y' : { 'A':2+6, 'B':2+3, 'C':2+0 }, # Paper defeats Rock
    'Z' : { 'A':3+0, 'B':3+6, 'C':3+3 }  # Scissors defeats Paper
}

strategy = {
    'X' : { 'A':'Z', 'B':'X', 'C':'Y' }, # lose
    'Y' : { 'A':'X', 'B':'Y', 'C':'Z' }, # draw
    'Z' : { 'A':'Y', 'B':'Z', 'C':'X' }  # win
}
m = [x.strip().split() for x in open("day2_input").readlines()]
print( sum(score[h][g] for g,h in m) )
print( sum(score[strategy[h][g]][g] for g,h in m) )
