import fileinput

current_elf, best_elf = 0, 0

for line in fileinput.input():
    stripped_line = line.strip()
    if stripped_line:
        current_elf += int(stripped_line)
    else:
        if current_elf == 0:
            break

        if current_elf > best_elf:
            best_elf = current_elf
        current_elf = 0

print(best_elf)
