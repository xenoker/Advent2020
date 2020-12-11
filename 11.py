from puzzleinput import get
from copy import deepcopy
INPUT = [list(x) for x in get(11).split('\n')]
class Seating:
    def __init__(self, seats, mintoleave, lookdist):
        self.V = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        self.data = deepcopy(seats)
        self.dist = lookdist
        self.minleave = mintoleave
        self.H = len(INPUT)
        self.W = len(INPUT[1])
    def count(self):
        return sum(r.count('#') for r in self.data)
    def look(self,row,col,r,c):
        for m in range(1,self.dist+1):
            if 0<=(col+c*m)<=(self.W-1) and 0<=(row+r*m)<=(self.H-1):
                see = self.data[row+r*m][col+c*m]
                if see == '#': return True
                if see == 'L': return False
            else: return False
        return False
    def look_around(self,row,col):
        return sum(self.look(row,col,r,c) for r,c in self.V)
    def state(self):
        odata = deepcopy(self.data)
        for c in range(0,self.W):
            for r in range(0,self.H):
                if self.data[r][c] == 'L' and self.look_around(r,c) == 0: odata[r][c]='#'
                if self.data[r][c] == '#' and self.look_around(r,c) >= self.minleave: odata[r][c]='L'
        if odata != self.data:
            self.data = odata
            return True
    def run(self):
        while self.state(): pass
        return self.count()
def part(part):
    lookdist,minleave = {1:(1,4), 2:(200,5)}[part]
    S = Seating(INPUT,minleave,lookdist)
    return S.run()
assert part(1) == 2470
assert part(2) == 2259









