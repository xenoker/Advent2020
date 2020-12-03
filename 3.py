from puzzleinput import getlines
from functools import reduce
LINES = getlines(3)
L = len(LINES[0])

def trees(right,down):
    C = 0
    for i,line in enumerate(LINES[::down]):
        if line[(right*i)%L]=='#': C+=1
    return C

def solve(*slopes):
    return reduce(lambda a,b:a*b, [trees(*x) for x in slopes])

assert solve((3,1)) == 228
assert solve((1,1),(3,1),(5,1),(7,1),(1,2)) == 6818112000

