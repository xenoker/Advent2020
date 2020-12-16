from puzzleinput import get
INPUT = get(16)
SECTIONS = INPUT.split('\n\n')
RULES = {}
for ruleline in SECTIONS[0].split('\n'):
    name,rules = ruleline.split(': ')
    rules = rules.split(' or ')
    RULES[name]= tuple((int(a),int(b)) for a,b in (rule.split('-') for rule in rules))
MYTICKET = list(map(int,SECTIONS[1].split('\n')[1].split(',')))
TICKETS = [tuple(map(int,x.split(','))) for x in SECTIONS[2].split('\n')[1:]]
def testnumber(num):
    for name,rules in RULES.items():
        for a,b in rules:
            if a<=num<=b: return True
    return False   
def testrule(rulename,pos):
    for ticket in TICKETS:
        for a,b in RULES[rulename]:
            if a<=ticket[pos]<=b: break
        else: return False
    return True  
def part1():
    err, bad = 0, []
    for i,ticket in enumerate(TICKETS):
        for num in ticket:
            if not testnumber(num):
                err += num
                bad.append(i)
    return err,bad
def part2():
    location,loclist = {},[]
    out = 1
    for _ in RULES:
        for rulename in (k for k in RULES.keys() if k not in location):
            L = [i for i in range(len(RULES)) if i not in loclist and testrule(rulename,i)]
            if len(L) == 1:
                p = L[0]
                location[rulename] = p
                loclist.append(p)
                if rulename.startswith('departure'): out *= MYTICKET[p]
    return out
part1err, bad = part1()
TICKETS = [t for i,t in enumerate(TICKETS) if i not in bad]
assert part1err == 23009
assert part2() == 10458887314153
