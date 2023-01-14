import fileinput

score_map = {
    # Rock
    ('A', 'X'): 0 + 3,
    ('A', 'Y'): 3 + 1,
    ('A', 'Z'): 6 + 2,

    # Paper
    ('B', 'X'): 0 + 1,
    ('B', 'Y'): 3 + 2,
    ('B', 'Z'): 6 + 3,

    # Scissor
    ('C', 'X'): 0 + 2,
    ('C', 'Y'): 3 + 3,
    ('C', 'Z'): 6 + 1,
}

score = 0

for line in fileinput.input():
    stripped_line = line.strip()
    if stripped_line:
        elf, me = stripped_line.split()
        score += score_map[(elf, me)]
    else:
        break

print(score)
