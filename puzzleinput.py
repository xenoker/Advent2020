
#clipboard for the quick trys in the first few minutes
def CB():
    from tkinter import Tk
    root = Tk()
    root.withdraw()
    return root.clipboard_get().strip()
def CBL():
    return [x for x in CB().split('\n') if x]
def CBI():
    return [int(x) for x in CB().split('\n') if x]


def get(i):
    with open(f'./inputs/{i}.txt') as f:
        return f.read()
def getlines(i):
    with open(f'./inputs/{i}.txt') as f:
        return [x for x in f.read().split('\n') if x]
def getints(i):
    with open(f'./inputs/{i}.txt') as f:
        return [int(x) for x in f.read().split('\n') if x]
