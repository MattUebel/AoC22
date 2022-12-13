# Path: day12/hill_climbing_algorithm.py

# test.txt contains
# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi

map = [lines for lines in open("test.txt").read().splitlines()]

print(map)


def get_elevation(map, x, y):
    if map[y][x] == "S":
        return 0
    elif map[y][x] == "E":
        return ord("z") - ord("a")
    else:
        return ord(map[y][x]) - ord("a")


def is_valid_move(map, x, y):
    return 0 <= x < len(map[0]) and 0 <= y < len(map)


# can move up, down, left, right
def get_neighbors(map, x, y):
    neighbors = []
    if is_valid_move(map, x, y - 1):
        neighbors.append((x, y - 1))
    if is_valid_move(map, x, y + 1):
        neighbors.append((x, y + 1))
    if is_valid_move(map, x - 1, y):
        neighbors.append((x - 1, y))
    if is_valid_move(map, x + 1, y):
        neighbors.append((x + 1, y))
    return neighbors


# can go to neightbor if it's elevation is 2 or more than the current
def get_valid_neighbors(map, x, y):
    neighbors = []
    for nx, ny in get_neighbors(map, x, y):
        print(f"elevation: {get_elevation(map, nx, ny)} - {get_elevation(map, x, y)}")
        if get_elevation(map, nx, ny) - get_elevation(map, x, y) >= 2:
            neighbors.append((nx, ny))
    return neighbors


def get_start_point(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "S":
                return (x, y)
    return None


def get_end_point(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "E":
                return (x, y)
    return None


def get_path_from_start_to_end(map):
    start = get_start_point(map)
    end = get_end_point(map)
    print(f"start: {start} end: {end}")
    if start is None or end is None:
        return None

    path = []
    x, y = start
    while (x, y) != end:
        path.append((x, y))
        print(f"path: {path}")
        neighbors = get_valid_neighbors(map, x, y)
        print(f"neighbors: {neighbors}")
        if len(neighbors) == 0:
            return None
        x, y = neighbors[0]
    path.append((x, y))
    print(f"path: {path}")
    return path


def print_map(map, path):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if (x, y) in path:
                print("*", end="")
            else:
                print(map[y][x], end="")
        print()


path = get_path_from_start_to_end(map)
print_map(map, path)
