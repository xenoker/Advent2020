from puzzleinput import get
INPUT = get(6).split('\n\n')
def part1():
    C = 0
    for g in INPUT:
        C+=len(set(g.replace('\n','')))
    return C
def part2():
    C = 0
    for g in INPUT:
        ps = g.split('\n')
        S = set(ps[0])
        for p in ps[1:]:
            S = S & set(p)
        C += len(S)
    return C
assert part1() == 6799
assert part2() == 3354
