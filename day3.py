import fileinput


def priority(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    return ord(item) - ord('a') + 1


score = 0

for line in fileinput.input():
    if not line.strip():
        break

    compartment_size = len(line) // 2  # assume single char EOL
    score += priority(*(set(line[:compartment_size]) &
                        set(line[compartment_size:-1])))

print(score)
