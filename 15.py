INPUT = [18,8,0,5,4,1,20]
def part(n):
    D = dict((b,a) for a,b in enumerate(INPUT[:-1]))
    p = INPUT[-1]
    for x in range(len(D),n-1):
        c = x-D[p] if p in D else 0
        D[p], p = x, c
    return p
assert part(2020) == 253
assert part(30000000) == 13710
