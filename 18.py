from puzzleinput import getlines
from pyparsing import Literal, Word, Group, ZeroOrMore, Forward, nums
INPUT = getlines(18)
class Parser:
    def push(self, strg, loc, toks):
        self.exprStack.append(toks[0])
    def __init__(self, part1):
        number = Word(nums)
        plus = Literal("+")
        mult = Literal("*")
        lpar = Literal("(").suppress()
        rpar = Literal(")").suppress()
        mopop = mult | plus
        expr = Forward()
        numorparen = number.setParseAction(self.push) | Group(lpar + expr + rpar)
        if part1:
            expr << numorparen + ZeroOrMore((mopop + numorparen).setParseAction(self.push))
        else:
            pfirst = numorparen + ZeroOrMore((plus + numorparen).setParseAction(self.push))
            expr << pfirst + ZeroOrMore((mult + pfirst).setParseAction(self.push))
        self.bnf = expr
        self.op = {"+": lambda a,b:a+b,
                   "*": lambda a,b:a*b}
    def evalStack(self, s):
        op = s.pop()
        if op in "+*":
            op2 = self.evalStack(s)
            op1 = self.evalStack(s)
            return self.op[op](op1, op2)
        else:
            return int(op)
    def eval(self, st, parseAll=True):
        self.exprStack = []
        results = self.bnf.parseString(st, parseAll)
        return self.evalStack(self.exprStack[:])
def part(part1):
    P = Parser(part1)
    return sum(P.eval(line) for line in INPUT)
assert part(part1=True) == 5019432542701
assert part(part1=False) == 70518821989947
