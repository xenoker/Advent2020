from puzzleinput import getlines
INPUT = getlines(5)
CHAR = {'F':-1,'B':1,'L':-1,'R':1}
def seat(code):
    row = int(63.5+sum(i*CHAR[c] for i,c in zip([32,16,8,4,2,1,0.5],code[:7])))
    col = int(3.5+sum(i*CHAR[c] for i,c in zip([2,1,0.5],code[-3:])))
    return row*8+col
seats = sorted(seat(x) for x in INPUT)
def part1(): return max(seats)
def part2(): return [x+1 for x,y in zip(seats[:-1],seats[1:]) if y-x==2][0]
assert part1() == 896
assert part2() == 659


