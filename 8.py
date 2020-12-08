from puzzleinput import getlines
INPUT = [x.split() for x in getlines(8)]
    
class Computer:
    def __init__(self,program):
        self.ACC = 0
        self.prog = program
        self.I = 0
        self.END = len(program)
        self.trace = []
        self.INST = {'nop':self.nop,'acc':self.acc,'jmp':self.jmp}
    def nop(self,val): self.I += 1
    def jmp(self,val): self.I += int(val)
    def acc(self,val):
        self.ACC += int(val)
        self.I+=1
    def step(self):
        if self.I in self.trace: return False #Infinite loop, for now
        self.trace.append(self.I)
        ins,val = self.prog[self.I]
        self.INST[ins](val)
        if self.I >= self.END: return True #Successful termination
    def run(self):
        state = None
        while state is None:
            state = self.step()
        return state

Comp = Computer(INPUT)
Comp.run()
print('Part 1:', Comp.ACC); assert Comp.ACC == 1475
FLIP = {'nop':'jmp','jmp':'nop'}
for i in Comp.trace[::-1]:
    ins,val = INPUT[i]
    if ins == 'acc': continue
    IN = INPUT.copy()
    IN[i] = (FLIP[ins],val)
    C = Computer(IN)
    if C.run():
        print('Part 2:', C.ACC); assert C.ACC == 1270
