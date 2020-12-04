from puzzleinput import get
import re
INPUT = get(4).split('\n\n')
RULES = {
    'byr':lambda x:1920<=int(x)<=2002,
    'iyr':lambda x:2010<=int(x)<=2020,
    'eyr':lambda x:len(x)==4 and 2020<=int(x)<=2030,
    'hgt':lambda x:x[-2:]=='cm' and 150<=int(x[:-2])<=193 or x[-2:]=='in' and 59<=int(x[:-2])<=76,
    'hcl':lambda x:re.match('^#[\da-f]{6}$',x),
    'ecl':lambda x:x in 'amb blu brn gry grn hzl oth'.split(),
    'pid':lambda x:x.isdigit() and len(x)==9,
    }
V = set(RULES)
def part(partone):
    C = 0
    for p in INPUT:
        d = dict(x.split(':') for x in re.split('[\n ]',p))
        if not V-set(d) and (partone or all(RULES[x](y) for x,y in d.items() if x!='cid')): C+=1
    return C
assert part(partone=True) == 228
assert part(partone=False) == 175
