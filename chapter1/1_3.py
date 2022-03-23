from collections import deque


# Keep the last N items
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('file.txt') as f:
        for line, prev_lines in search(f, 'hello', 5):
            for pline in prev_lines:
                print(pline, end='')
            print('line =', line, end='')
            print('_'*10)
