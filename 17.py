from puzzleinput import get
from itertools import product
INPUT = get(17)
def makeinput(n):
    inputset = set()
    for ln,line in enumerate(INPUT.split()):
        for rn,state in enumerate(line):
            if state == '#':
                inputset.add(tuple([rn,ln]+[0 for x in range(n-2)]))
    return inputset
def nextstate(AS,p):
    state = p in AS
    AN,IN = 0,0
    ncheck = set()
    for ip in product(*[(x-1,x,x+1) for x in p]):
        if ip == p: continue
        ncheck.add(ip)
        s = ip in AS
        if s: AN += 1
        else: IN += 1
    if state and AN in [2,3]: return True,ncheck
    if not state and AN == 3: return True,ncheck
    return False,ncheck
def part(n):
    AS = makeinput(n)
    for cycle in range(6):
        newAS = set()
        ncheck = set()
        for p in AS:
            newstate,nc = nextstate(AS,p)
            if newstate: newAS.add(p)
            ncheck.update(nc)
        for p in ncheck-AS:
            newstate,nc = nextstate(AS,p)
            if newstate: newAS.add(p)
        AS = newAS
    return len(AS)
assert part(3) == 280
assert part(4) == 1696
