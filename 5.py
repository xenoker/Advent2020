from puzzleinput import getlines
INPUT = getlines(5)
CHAR = dict(zip('FBLR','0101'))
def seat(code): return int(''.join(CHAR[x] for x in code),2)
seats = sorted(seat(x) for x in INPUT)
def part1(): return max(seats)
def part2(): return [x+1 for x,y in zip(seats[:-1],seats[1:]) if y-x==2][0]
assert part1() == 896
assert part2() == 659


