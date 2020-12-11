from puzzleinput import getints
INPUT = getints(10)
INPUT.extend([0,max(INPUT)+3])
INPUT.sort()
def part1():
    D = {1:0,3:0}
    for a,b in zip(INPUT,INPUT[1:]): D[b-a]+=1
    return D[1]*D[3]
def part2():
    A = [1]
    for i in range(1,len(INPUT)):
        A.append(A[-1] + sum(A[i-j] for j in [2,3] if i-j>=0 and INPUT[i]-INPUT[i-j]<=3));
    return A[-1]
assert part1() == 2400
assert part2() == 338510590509056

