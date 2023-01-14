import fileinput

count = 0

for line in fileinput.input():
    stripped_line = line.strip()
    if not stripped_line:
        break

    sec = tuple(map(int, stripped_line.replace('-', ',').split(',')))

    if (sec[0] <= sec[2] and sec[1] >= sec[3]) or \
            (sec[2] <= sec[0] and sec[3] >= sec[1]):
        count += 1

print(count)
