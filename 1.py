from puzzleinput import getints
from itertools import combinations as comb
INTS = getints(1)

def part1():
    for a,b in comb(INTS,2):
        if a+b==2020:
            return a*b

def part2():
    for a,b,c in comb(INTS,3):
        if a+b+c==2020:
            return a*b*c

if __name__ == '__main__':
    assert part1()==252724
    assert part2()==276912720

