import fileinput

current_elf = 0

best_elfs = (0, 0, 0)

for line in fileinput.input():
    stripped_line = line.strip()
    if stripped_line:
        current_elf += int(stripped_line)
    else:
        if current_elf == 0:
            break

        if current_elf >= best_elfs[0]:
            best_elfs = current_elf, *best_elfs[:2]
        elif current_elf >= best_elfs[1]:
            best_elfs = best_elfs[0], current_elf, best_elfs[1]
        elif current_elf >= best_elfs[2]:
            best_elfs = *best_elfs[:2], current_elf
        current_elf = 0

print(sum(best_elfs))
