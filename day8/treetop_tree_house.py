# Path: day8/treetop_tree_house.py

grid = open("input.txt").read().splitlines()

DIRECTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


def get_in_direction(grid, i, j, direction):
    di, dj = DIRECTIONS[direction]
    elements = []
    # return an empty list if the current element is on the edge of the grid
    if (
        i == 0
        and di == -1
        or i == len(grid) - 1
        and di == 1
        or j == 0
        and dj == -1
        or j == len(grid[0]) - 1
        and dj == 1
    ):
        return elements
    while i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
        i += di
        j += dj
        # return elements if the loop has gone past the edge of the grid
        if (
            direction == "up"
            and i < 0
            or direction == "down"
            and i > len(grid) - 1
            or direction == "left"
            and j < 0
            or direction == "right"
            and j > len(grid[0]) - 1
        ):
            return elements
        try:
            elements.append(grid[i][j])
        except IndexError:
            pass
    return elements


def check_if_tallest(grid, i, j):
    direction_results = []
    # check if on edge of grid
    if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
        return True
    for direction in DIRECTIONS:
        if grid[i][j] > max(get_in_direction(grid, i, j, direction)):
            direction_results.append(True)
    if True in direction_results:
        return True
    else:
        return False


def find_scenic_score(grid, i, j):
    # scenic score is found by find all trees shorter than the tree house up until the first as tall as the tree house
    shorter_trees_by_direction = {"up": [], "down": [], "left": [], "right": []}
    for direction in DIRECTIONS:
        trees = get_in_direction(grid, i, j, direction)
        if trees == []:
            shorter_trees_by_direction[direction] = []
        for tree in trees:
            if tree < grid[i][j]:
                shorter_trees_by_direction[direction].append(tree)
            elif tree >= grid[i][j]:
                shorter_trees_by_direction[direction].append(tree)
                break
            else:
                print(f"shorter trees by direction: {shorter_trees_by_direction}")
                break

    return (
        len(shorter_trees_by_direction["up"])
        * len(shorter_trees_by_direction["down"])
        * len(shorter_trees_by_direction["left"])
        * len(shorter_trees_by_direction["right"])
    )


def main():
    tree_house_count = 0
    max_scenic_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # check if the scenic score is the highest
            if find_scenic_score(grid, i, j) > max_scenic_score:
                max_scenic_score = find_scenic_score(grid, i, j)
            if check_if_tallest(grid, i, j):
                tree_house_count += 1
    print(f"Part 1: total visible trees {tree_house_count}")
    print(f"Part 2: max scenic score {max_scenic_score}")


if __name__ == "__main__":
    main()
