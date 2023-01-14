import fileinput

score_map = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,

    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,

    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

score_bonus = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

score = 0

for line in fileinput.input():
    stripped_line = line.strip()
    if stripped_line:
        elf, me = stripped_line.split()
        score += score_map[(elf, me)] + score_bonus[me]
    else:
        break

print(score)
