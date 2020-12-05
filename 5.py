from puzzleinput import getlines
INPUT = getlines(5)
CHAR = dict(zip('FBLR','0101'))
def seat(code):
    row = int(''.join(CHAR[x] for x in code[:7]),2)
    col = int(''.join(CHAR[x] for x in code[-3:]),2)
    return row*8+col
seats = sorted(seat(x) for x in INPUT)
def part1(): return max(seats)
def part2(): return [x+1 for x,y in zip(seats[:-1],seats[1:]) if y-x==2][0]
assert part1() == 896
assert part2() == 659


