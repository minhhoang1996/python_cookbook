
record = '..122..................100.......513.25..........'
cost = int(record[2:5])

print(cost)
yy = slice(2, 5, 1)
print(yy)
print(int(record[yy]))

# a = slice(1, 44, 3)
# s = 'HelloWorld'
# print(type(a.indices(len(s))))
#
# print(*a.indices(len(s)))
#
# print(*a.indices((len(s))))
# for i in range(*a.indices((len(s)))):
#     print(s[i])

