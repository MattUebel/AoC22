def parse_data(data):
    """Parse the data into a list of intervals."""
    elf_pairs = []
    for line in data:
        elf_pair = []
        for elf in line.split(","):
            start, end = elf.split("-")
            elf_pair.append(range(int(start), int(end)))
        elf_pairs.append(elf_pair)
    return elf_pairs


def find_if_subset(elf_pair):
    if set(elf_pair[0]).issubset(elf_pair[1]):
        return True
    elif set(elf_pair[1]).issubset(elf_pair[0]):
        return True
    else:
        return False


# ChatGPT's function
# Define a function to check if one range fully contains another
def is_contained(range1, range2):
    # Parse the range strings into start and end values
    start1, end1 = map(int, range1.split("-"))
    start2, end2 = map(int, range2.split("-"))
    # Check if one range fully contains the other
    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
        return True
    else:
        return False


def overlaps_at_all(range1, range2):
    # Parse the range strings into start and end values
    start1, end1 = map(int, range1.split("-"))
    start2, end2 = map(int, range2.split("-"))
    # check if the ranges overlap at all
    if (start1 < start2 and end1 < start2) or (start2 < start1 and end2 < start1):
        return False
    else:
        return True


if __name__ == "__main__":

    print("my attempt")
    data = open("data.txt").readlines()
    elf_pairs = parse_data(data)
    print(sum([find_if_subset(elf_pair) for elf_pair in elf_pairs]))

    print("ChatGPT's attempt")

    # Open the input file and read the pairs of ranges
    with open("data.txt") as file:
        pairs = [line.strip() for line in file.readlines()]

    # Count the number of pairs where one range fully contains the other
    count = 0
    for pair in pairs:
        # Split the pair into the two ranges
        range1, range2 = pair.split(",")
        # Check if one range fully contains the other
        if is_contained(range1, range2) or is_contained(range2, range1):
            count += 1

    # find the pairs that overlap at all
    overlap_count = 0
    for pair in pairs:
        # Split the pair into the two ranges
        range1, range2 = pair.split(",")
        # Check if one range fully contains the other
        if overlaps_at_all(range1, range2):
            overlap_count += 1

    print(f"overlaps at all: {overlap_count}")

    # Print the result
    print(f"In {count} assignment pairs, one range fully contains the other.")
