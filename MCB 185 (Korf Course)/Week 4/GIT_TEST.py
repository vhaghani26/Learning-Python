#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it
# We will have a variable number of bins (can be months or days)
# And some number of trials for the simulation
# And some number of people whose have random birthdays
# Use assert() to check parameters
# On the command line:
#	python3 birthday.py <bins> <trials> <people>

import sys # Allows us to use sys arg
import random

assert(len(sys.argv) == 4) # 4 arguments written after python3
bins = int(sys.argv[1])
trials = int(sys.argv[2])
people = int(sys.argv[3])

assert(bins > 0)
assert(trials > 0)
assert(people > 1)

collisions = 0

for t in range(trials):
    calendar = [] # Create an empty calendar
    same_day = False
    for i in range(bins):
        calendar.append(0)
    for p in range(people): # Insert people into calendar
        r = random.randint(0, bins-1) # r represents a person's birthday
        calendar[r] += 1
    for day in calendar: # Finds shared birthday
        if day > 1:
            same_day = True
            break # Makes this faster beacuse it breaks the loop as soon as a birthday twin is found
    if same_day:
        collisions += 1
print(collisions/trials)

"""
python3 birthday.py 365 1000 23
0.520
"""

