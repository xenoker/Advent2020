from puzzleinput import getlines
from functools import reduce
INPUT = getlines(21)
LINPUT = []
ING, CON = set(), set()
for line in INPUT:
    ings,conts = line.split(' (contains ')
    ing = ings.split()
    for i in ing: ING.add(i)
    cont = conts[:-1].split(', ')
    for c in cont: CON.add(c)
    LINPUT.append([ing,cont])
found = set()
D = {}
while CON:
    for con in CON:
        s = [set(i) for i,c in LINPUT if con in c]
        s2 = reduce(lambda a,b:a&b, s)
        s3 = s2-found
        if len(s3)==1:
            CON.remove(con)
            found.update(s3)
            D[s3.pop()] = con
            break
def part1(): return sum(len(set(i)-found) for i,c in LINPUT)
def part2(): return ','.join( sorted(D.keys(),key=lambda x:D[x]))
assert part1() == 2282
assert part2() == "vrzkz,zjsh,hphcb,mbdksj,vzzxl,ctmzsr,rkzqs,zmhnj"
