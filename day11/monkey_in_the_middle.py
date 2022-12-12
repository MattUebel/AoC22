# Path: day11/monkey_in_the_middle.py

# monkey configuration:
# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1
from functools import reduce


def find_prime_factors(number):
    factors = []
    for i in range(2, number + 1):
        while number % i == 0:
            factors.append(i)
            number /= i
    return factors


config = open("test.txt").read().splitlines()

# parse monkey config
monkey_config = {}
for line in config:
    if line.startswith("Monkey"):
        monkey = int(line.split(" ")[1][:-1])
        monkey_config[monkey] = {}
        # run prime factorization on the starting items
        monkey_config[monkey]["items"] = []
        for item in config[config.index(line) + 1][18:].split(", "):
            monkey_config[monkey]["items"].append(find_prime_factors(int(item)))
        monkey_config[monkey]["operation"] = config[config.index(line) + 2][19:]
        monkey_config[monkey]["test"] = config[config.index(line) + 3][21:]
        monkey_config[monkey]["if_true"] = config[config.index(line) + 4][29:]
        monkey_config[monkey]["if_false"] = config[config.index(line) + 5][30:]
        monkey_config[monkey]["examined_count"] = 0

from pprint import pprint

ROUNDS = 10000

for i in range(ROUNDS):
    for monkey in monkey_config.keys():
        while len(monkey_config[monkey]["items"]) > 0:
            # multiple all the items together
            old = int(reduce(lambda x, y: x * y, monkey_config[monkey]["items"].pop(0)))
            monkey_config[monkey]["examined_count"] += 1
            new = eval(monkey_config[monkey]["operation"])
            if new % int(monkey_config[monkey]["test"]) == 0:
                monkey_config[int(monkey_config[monkey]["if_true"])]["items"].append(
                    find_prime_factors(new)
                )
            else:
                monkey_config[int(monkey_config[monkey]["if_false"])]["items"].append(
                    find_prime_factors(new)
                )
    print(f"Round {i + 1} complete")

# pprint(monkey_config)

# find the two monkeys that examined the most items
monkey_and_examined = []
for monkey in monkey_config.keys():
    monkey_and_examined.append((monkey, monkey_config[monkey]["examined_count"]))

sorted_list = sorted(monkey_and_examined, key=lambda x: x[1])
sorted_list[-2:]

print(sorted_list)

top_items = []
for monkey in sorted_list[-2:]:
    top_items.extend(monkey_config[monkey[0]]["items"])

print(f"Part 1: {sorted_list[-2][1] * sorted_list[-1][1]}")
