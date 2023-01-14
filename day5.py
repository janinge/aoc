import fileinput

stacks = {}
puzzle_input = fileinput.input()

for line in puzzle_input:
    if line.isspace():
        break

    for col, char in enumerate(line):
        if char.isalpha():
            stacks.setdefault(((col - 1) // 4) + 1, []).insert(0, char)

for line in puzzle_input:
    if line.isspace():
        break

    num, fr, to = tuple(map(int, ''.join(c for c in line if not c.isalpha()).split()))
    for _ in range(num):
        stacks[to].append(stacks[fr].pop(-1))

print(''.join(stacks[i][-1] for i, _ in enumerate(stacks.keys(), start=1)))
