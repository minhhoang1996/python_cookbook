from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['a'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['b'].add(2)
d['a'].add(4)
print(d)

d = {}
d.setdefault('a', []).append(3)
d.setdefault('b', []).append(4)
d.setdefault('b', []).remove(4)
print(d)
