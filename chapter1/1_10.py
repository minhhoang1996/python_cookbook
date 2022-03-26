
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
seen = set()
def dedupe(items, key=None):
    # seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            print('var={}'.format(val))
            yield item
            seen.add(val)


print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(seen)