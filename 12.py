from puzzleinput import getlines
INPUT = getlines(12)
FACE = {'E':(1,0),'W':(-1,0),'N':(0,1),'S':(0,-1)}
def rotate(V,D,A):
    if D == 'R':
        for i in range(A//90): V = V[1],-V[0]
    else:
        for i in range(A//90): V = -V[1],V[0]
    return V
def part1():
    F,P = (1,0),(0,0)
    for ins in INPUT:
        i,n = ins[0], int(ins[1:])
        if i in 'RL':
            F = rotate(F,i,n)
        elif i in 'NSEW':
            P = P[0]+FACE[i][0]*n, P[1]+FACE[i][1]*n
        elif i == 'F':
            P = P[0]+F[0]*n, P[1]+F[1]*n
    return abs(P[0])+abs(P[1])
def part2():
    F,P,W = (1,0),(0,0),(10,1)
    for ins in INPUT:
        i,n = ins[0], int(ins[1:])
        if i in 'RL':
            W = rotate(W,i,n)
        elif i in 'NSEW':
            W = W[0]+FACE[i][0]*n, W[1]+FACE[i][1]*n
        elif i == 'F':
            P = P[0]+W[0]*n, P[1]+W[1]*n
    return abs(P[0])+abs(P[1])
assert part1() == 1565
assert part2() == 78883
