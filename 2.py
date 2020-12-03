from puzzleinput import getlines
LINES = getlines(2)

def part1():
    C = 0
    for line in LINES:
        left,txt = line.split(':')
        N,L = left.split()
        N1,N2 = N.split('-')
        if int(N1)<=txt.count(L)<=int(N2): C+=1
    return C

def part2():
    C = 0
    for line in LINES:
        left,txt = line.split(':')
        N,L = left.split()
        N1,N2 = N.split('-')
        if ((txt[int(N1)]==L)^(txt[int(N2)]==L)): C+=1
    return C

if __name__ == '__main__':
    assert part1() == 600
    assert part2() == 245
