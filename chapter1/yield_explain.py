from collections import deque

def simpleGenerateFun():
    yield 1
    yield 2
    yield 3


for value in simpleGenerateFun():
    print(value)

