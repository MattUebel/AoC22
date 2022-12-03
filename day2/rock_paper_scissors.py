def calculate_score(data):
    total_score = [0, 0]
    for trial in data:
        if trial[0] == trial[1]:
            total_score[0] += 3
            total_score[1] += 3
        elif (
            (trial[0] == "Rock" and trial[1] == "Scissors")
            or (trial[0] == "Paper" and trial[1] == "Rock")
            or (trial[0] == "Scissors" and trial[1] == "Paper")
        ):
            total_score[0] += 6
        else:
            total_score[1] += 6

        # add in scoring for the item selected
        if trial[0] == "Rock":
            total_score[0] += 1
        elif trial[0] == "Paper":
            total_score[0] += 2
        else:
            total_score[0] += 3
        if trial[1] == "Rock":
            total_score[1] += 1
        elif trial[1] == "Paper":
            total_score[1] += 2
        else:
            total_score[1] += 3

    return total_score


print("Part 1")
data = open("data.txt", "r").readlines()
data = [x.strip() for x in data]
data = [x.split(" ") for x in data]

# rename list items for readability
for trial in data:
    trial[0] = trial[0].replace("A", "Rock")
    trial[0] = trial[0].replace("B", "Paper")
    trial[0] = trial[0].replace("C", "Scissors")
    trial[1] = trial[1].replace("X", "Rock")
    trial[1] = trial[1].replace("Y", "Paper")
    trial[1] = trial[1].replace("Z", "Scissors")

part_1_score = calculate_score(data)
print(f"Your opponent's score is {part_1_score[0]} and your score is {part_1_score[1]}")
print("Part 2")

# column 1 is the opponent's choice, and column 2 maps to what the outcome should be
# Y means draw, X means lose, Z means win

data = open("data.txt", "r").readlines()
data = [x.strip() for x in data]
data = [x.split(" ") for x in data]

for trial in data:
    trial[0] = trial[0].replace("A", "Rock")
    trial[0] = trial[0].replace("B", "Paper")
    trial[0] = trial[0].replace("C", "Scissors")
    trial[1] = trial[1].replace("X", "lose")
    trial[1] = trial[1].replace("Y", "draw")
    trial[1] = trial[1].replace("Z", "win")

part_2_data = []
for trial in data:
    if trial[1] == "draw":
        part_2_data.append([trial[0], trial[0]])
    elif trial[1] == "win":
        if trial[0] == "Rock":
            part_2_data.append(["Rock", "Paper"])
        elif trial[0] == "Paper":
            part_2_data.append(["Paper", "Scissors"])
        else:
            part_2_data.append(["Scissors", "Rock"])
    else:
        if trial[0] == "Rock":
            part_2_data.append(["Rock", "Scissors"])
        elif trial[0] == "Paper":
            part_2_data.append(["Paper", "Rock"])
        else:
            part_2_data.append(["Scissors", "Paper"])
part_2_score = calculate_score(part_2_data)
print(f"Your opponent's score is {part_2_score[0]} and your score is {part_2_score[1]}")
