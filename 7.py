from puzzleinput import get
import re
INPUT = re.sub(" bags?\.?","",get(7)).split('\n')
BAGS = {}
for line in INPUT:
    bag, content = line.split(' contain ')
    content = (y.split(maxsplit=1) for y in content.split(', '))
    BAGS[bag] = dict((y,int(x)) for x,y in content if x!='no')
def check(bag): return any(b=='shiny gold' or check(b) for b in BAGS[bag].keys())
def num(bag): return sum(n+n*num(b) for b,n in BAGS[bag].items())
def part1(): return sum(map(check,BAGS.keys()))
def part2(): return num('shiny gold')
assert part1() == 179
assert part2() == 18925
