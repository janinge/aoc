import fileinput

count = 0

for line in fileinput.input():
    stripped_line = line.strip()
    if not stripped_line:
        break

    sec = tuple(map(int, stripped_line.replace('-', ',').split(',')))

    if not ((sec[1] < sec[2] or sec[0] > sec[3]) and
            (sec[3] < sec[1] or sec[2] > sec[1])):
        count += 1

print(count)
