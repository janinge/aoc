import fileinput


def priority(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    return ord(item) - ord('a') + 1


score = 0
elfgroup = {}

for line in fileinput.input():
    stripped_line = line.strip()
    if not stripped_line:
        break

    member = (fileinput.lineno() - 1) % 3
    elfgroup[member] = set(stripped_line)

    if member == 2:
        score += priority(*set.intersection(*elfgroup.values()))

print(score)