# Path: day10/cathod_ray_tube.py

# possible registers and their initial value
REGISTERS = {"X": 1}

# possible instructions and their cycle cost
INSTRUCTIONS = {"noop": 1, "addx": 2}

# init cycle
CYCLES = []

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
important_cycles = [20, 60, 100, 140, 180, 220]

# read the progrmam from the file
program_lines = open("input.txt").read().splitlines()

print(program_lines)

for program_line in program_lines:
    if program_line != "noop":
        instruction, argument = program_line.split(" ")
    else:
        instruction = program_line
        argument = None
    cycle_cost = INSTRUCTIONS[instruction]
    while cycle_cost > 0:
        cycle_cost -= 1
        if instruction == "addx" and cycle_cost == 0:
            REGISTERS["X"] += int(argument)
        print(f"cycle {len(CYCLES)} {instruction} {argument} {REGISTERS['X']}")
        CYCLES.append(REGISTERS["X"])

total_signal_strength = 0

for cycle in important_cycles:
    total_signal_strength += cycle * CYCLES[cycle - 1]
    print(f"{cycle} {CYCLES[cycle - 1]}")

print(total_signal_strength)
