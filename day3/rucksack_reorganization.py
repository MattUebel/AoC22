def find_priority(character):
    if character.islower():
        return ord(character) - 96
    else:
        return ord(character) - 38


def find_common_characters(string1, string2):
    common_characters = ""
    for character in string1:
        if character in string2:
            common_characters += character
    return common_characters


def split_data():
    split_data = []
    for item in data:
        split_data.append([item[: len(str(item)) // 2], item[len(str(item)) // 2 :]])
    return split_data


if __name__ == "__main__":
    # load data
    data = open("data.txt", "r").readlines()
    data = [x.strip() for x in data]

    # split it
    split_data = split_data()

    # find the sum of items in both compartments of each rucksack
    priority_sum = 0
    for pair in split_data:
        common_characters = find_common_characters(pair[0], pair[1])
        deduplicated_common_characters = "".join(set(common_characters))
        priorities = [
            find_priority(character) for character in deduplicated_common_characters
        ]
        priority_sum += sum(priorities)
    print(f"part one priority sum is {priority_sum}")

    # Part 2
    # split data list into groups of three
    trisected_data = [data[i : i + 3] for i in range(0, len(data), 3)]

    # find the common characters in each trio of strings
    common_characters = []
    for trio in trisected_datazx:
        common = set.intersection(*map(set, trio))
        common_characters.append(common)

    # find the sum of the priorities of the common characters
    priority_sum = 0
    for item in common_characters:
        for character in item:
            priority_sum += find_priority(character)

    print(f"part two priority sum is {priority_sum}")
