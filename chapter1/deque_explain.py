from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB', 'color'])

queue.append('4')
queue.appendleft('5')
print(queue)
queue.pop()
queue.popleft()
print(queue)

print(queue.index('color', 2, len(queue)))

queue.insert(len(queue)-1, 'insert_value')
print(queue)

queue.remove('insert_value')
print(queue)

print(queue.count('age'))

queue.extend(['hihi', 'haha'])
print(queue)

queue.extendleft(['huhu', 'hixhix'])
print(queue)

queue.reverse()
print(queue)

queue.rotate(2)

