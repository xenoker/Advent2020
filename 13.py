from puzzleinput import getlines
from itertools import count
INPUT = getlines(13)
T = int(INPUT[0])
B = [(i,int(x)) for i,x in enumerate(INPUT[1].split(',')) if x!='x' ]
def part1():
    wait,bus = min(((b - T%b, b) for _,b in B), key=lambda x:x[0])
    return wait*bus
def part2():
    x,s = 1,1
    for i,b in B:
        x = next(y for y in count(x,s) if (y+i)%b==0)
        s *= b #all b's prime, ez
    return x
assert part1() == 104
assert part2() == 842186186521918





