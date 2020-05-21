#!/usr/bin/env python3

# Write a program that creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line:
#	python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>

import gzip
import sys
import math
import random

def rand_dna(lenseq, a, c, g, t):
    dnaseq = []
    for i in range(lenseq):
        r = random.random()
        if r < a: 
            dnaseq.append('A')
        elif r < a+c:
            dnaseq.append('C')
        elif r < a+c+g:
            dnaseq.append('G')
        else:
            dnaseq.append('T')
    return ''.join(dnaseq)
    
count = int(sys.argv[1])

min = int(sys.argv[2])
max = int(sys.argv[3])
a = float(sys.argv[4])
c = float(sys.argv[5])
g = float(sys.argv[6])
t = float(sys.argv[7])

for i in range(count):
    x = random.randint(min, max)
    dna = rand_dna(x, a, c, g, t)
    print(f'>seq-{i}')
    print(dna)


"""
python3 rand_fasta.py 3 10 20 0.1 0.2 0.3 0.4
>seq-0
TCGTTTTGATTACGG
>seq-1
CGGCTGTTCCGTAATGC
>seq-2
TTTCGTGTACTTTCTAGTGA
"""
