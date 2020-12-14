from puzzleinput import getlines
INPUT = getlines(14)

class DockingComputer:
    def __init__(self):
        self.MEM = {}
        self.mask = ''
    def V1_set(self,adr,val):
        for i,c in enumerate(self.mask):
            if c == '1': val |= 1<<i
            if c == '0': val &= ~(1<<i)
            self.MEM[adr] = val
    def V2_set(self,adr,val,i=0,O=None):
        while i!=36:
            c = self.mask[i]
            if O: c,O = O,None
            if c == '1': adr |= 1<<i
            if c == '-': adr &= ~(1<<i)
            if c == 'X':
                self.V2_set(adr,val,i,'1')
                self.V2_set(adr,val,i,'-')
                return
            i += 1
        self.MEM[adr] = val
    @property
    def memsum(self): return sum(self.MEM.values())

P1 = DockingComputer()
P2 = DockingComputer()
for line in INPUT:
    if line[:4]=='mask':
        mask = line[:6:-1]
        P1.mask = mask
        P2.mask = mask
    else:
        adr = int(line[4:line.find(']')])
        val = int(line.split()[2])
        P1.V1_set(adr,val)
        P2.V2_set(adr,val)
assert P1.memsum == 16003257187056
assert P2.memsum == 3219837697833







