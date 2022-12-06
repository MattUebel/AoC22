import re


def parse_data(data):
    # find the crate stacks and also the crate moving instructions
    stacks = []
    instructions = []
    for line in data:
        if line.strip().startswith("["):
            stacks.append(line)
        elif line.strip().startswith("1"):
            stacks.append(line)
        elif line == "":
            continue
        else:
            instructions.append(line)
    return stacks, instructions


def parse_crates(string):
    # Use the re.findall function to extract all the crate IDs and empty spaces
    crates_and_spaces = []
    for i in range(0, len(string), 4):
        crates_and_spaces.append(string[i : i + 3])

    # Use the re.sub function to remove the square brackets from the crate IDs
    crates = [re.sub(r"\[|\]", "", crate) for crate in crates_and_spaces]

    # Return the list of crates and empty spaces
    return crates


def stacks_dict_gen(stacks):
    stacks_dict = {}
    for stack_num in stacks[-1].split(" "):
        if stack_num.isdigit():
            stacks_dict[stack_num] = []
        else:
            continue
    if stacks[-1][1] == "1":
        stacks.pop()
    for stack in stacks:
        # split the stack into a list of crates
        crates = parse_crates(stack)
        crate_index = 1
        print(len(crates))
        print(crates)
        for crate in crates:
            if crate == "   ":
                # empty spot, skip
                crate_index += 1
                continue
            else:
                # add the crate to the stack_dict
                stacks_dict[str(crate_index)].insert(0, crate)
                crate_index += 1
    return stacks_dict


def perform_instructions(stacks_dict, instructions):
    instruction_number = 1
    for instruction in instructions:
        # print(f"Instruction {instruction_number}")
        # create move_total, move_from, move_to by regex extracting the numbers from the instruction
        move_total, move_from, move_to = re.findall(r"\d+", instruction)
        # print(f"move_total: {move_total}, move_from: {move_from}, move_to: {move_to}")
        # move the crates from the move_from stack to the move_to stack one at a time
        # print(f"{stacks_dict[move_from]} -> {stacks_dict[move_to]}")
        for i in range(int(move_total)):
            crate = stacks_dict[move_from].pop()
            stacks_dict[move_to].append(crate)
        # print(f"{stacks_dict[move_from]} - {stacks_dict[move_to]}")

        instruction_number += 1
    top_of_stack_string = ""
    for k, v in stacks_dict.items():
        top_of_stack_string += v[-1]
    return top_of_stack_string


def main():
    data = open("input.txt", "r").read().splitlines()
    stacks, instructions = parse_data(data)
    stacks_dict = stacks_dict_gen(stacks)
    print(stacks_dict)
    top_of_stack_string = perform_instructions(stacks_dict, instructions)
    print(top_of_stack_string)


if __name__ == "__main__":
    main()
