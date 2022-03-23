# add 10 to argument a, and return the result:
x = lambda a: a + 10
print(x(5))

# multiply arg a with arg b and return the result
x = lambda a, b: a*b
print(x(5, 2))

# summarize arg a, b, and c and return the result
x = lambda a, b, c: a + b + c
print(x(1, 2, 3))
print(type(x))