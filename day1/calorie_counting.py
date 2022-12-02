with open("data.txt", "r") as f:
    data = f.readlines()

# split data into a list of lists with an empty line as the delimiter
data = [x.split() for x in data]

elves = []
elf_cal_total = 0
for food in data:
    # check if food is empty
    if len(food) == 0:
        elves.append(elf_cal_total)
        elf_cal_total = 0
        continue
    # get the calories
    elf_cal_total += int(food[0])

print(f"elf with most cals: {max(elves)}")
print(f"sum of top three: {sum(sorted(elves)[-3:])}")
