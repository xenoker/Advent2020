from puzzleinput import getints
INPUT = getints(9)
def part1(nums,P):
    for i,n in enumerate(nums[P:],P):
        pre = INPUT[i-P:i]
        if not any(x for x in pre if n-x in pre): return n,i
def part2(nums,find,at):
    for i in range(at-2,-1,-1): #loop by initial position first
        for n in range(2,at-i): #so number of ints can abort
            L = nums[i:i+n]
            S = sum(L)
            if S > find: break #as soon as its too large
            if S == find: return min(L)+max(L)
P1,at = part1(INPUT,25)
P2 = part2(INPUT,P1,at)
assert P1 == 1398413738
assert P2 == 169521051
