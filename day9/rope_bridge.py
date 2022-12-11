# Path: day9/rope_bridge.py

DIRECTIONS = ["U", "D", "L", "R", "UR", "UL", "DR", "DL", "none"]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # implement repr
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def move_a_step(self, direction):
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "none":
            pass

    def move_a_step_diagonal(self, direction):
        if direction == "UR":
            self.y += 1
            self.x += 1
        elif direction == "UL":
            self.y += 1
            self.x -= 1
        elif direction == "DR":
            self.y -= 1
            self.x += 1
        elif direction == "DL":
            self.y -= 1
            self.x -= 1
        elif direction == "none":
            pass


class Rope:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.visited = list()

    def execute_instruction(self, direction):
        # move the head
        self.head.move_a_step(direction)
        adjacent = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        diagonally_adjacent = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

        two_to_left = [-2, 0]
        two_to_right = [2, 0]
        two_up = [0, 2]
        two_down = [0, -2]

        up_left_diagonal = [[-2, 2], [-1, 2], [-2, 1]]
        up_right_diagonal = [[2, 2], [1, 2], [2, 1]]
        down_left_diagonal = [[-2, -2], [-1, -2], [-2, -1]]
        down_right_diagonal = [[2, -2], [1, -2], [2, -1]]

        # find the difference between the head and the tail
        diff = [self.head.x - self.tail.x, self.head.y - self.tail.y]

        if diff == [0, 0]:
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return "none"

        if diff in adjacent or diff in diagonally_adjacent:
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return "none"

        # figure out which direction the tail should move
        if diff == two_to_left:
            self.tail.move_a_step("L")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return "L"
        if diff == two_to_right:
            self.tail.move_a_step("R")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return "R"
        if diff == two_up:
            self.tail.move_a_step("U")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return "U"
        if diff == two_down:
            self.tail.move_a_step("D")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return "D"
        if diff in up_left_diagonal:
            self.tail.move_a_step_diagonal("UL")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return "UL"
        if diff in up_right_diagonal:
            self.tail.move_a_step_diagonal("UR")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return "UR"
        if diff in down_left_diagonal:
            self.tail.move_a_step_diagonal("DL")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return "DL"
        if diff in down_right_diagonal:
            self.tail.move_a_step_diagonal("DR")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return "DR"


def main():
    instructions = open("test.txt", "r").read().splitlines()
    rope = Rope(head=Point(0, 0), tail=Point(0, 0))
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        for step in range(steps):
            rope.execute_instruction(direction)

    print("Part 1 ", len(rope.visited))

    # part 2, 10 knotted rope
    head_knot = Point(0, 0)
    knot_one = Point(0, 0)
    knot_two = Point(0, 0)
    knot_three = Point(0, 0)
    knot_four = Point(0, 0)
    knot_five = Point(0, 0)
    knot_six = Point(0, 0)
    knot_seven = Point(0, 0)
    knot_eight = Point(0, 0)
    knot_nine = Point(0, 0)

    head_rope = Rope(head=head_knot, tail=knot_one)
    knot_one_rope = Rope(head=knot_one, tail=knot_two)
    knot_two_rope = Rope(head=knot_two, tail=knot_three)
    knot_three_rope = Rope(head=knot_three, tail=knot_four)
    knot_four_rope = Rope(head=knot_four, tail=knot_five)
    knot_five_rope = Rope(head=knot_five, tail=knot_six)
    knot_six_rope = Rope(head=knot_six, tail=knot_seven)
    knot_seven_rope = Rope(head=knot_seven, tail=knot_eight)
    knot_eight_rope = Rope(head=knot_eight, tail=knot_nine)

    ropes = [
        head_rope,
        knot_one_rope,
        knot_two_rope,
        knot_three_rope,
        knot_four_rope,
        knot_five_rope,
        knot_six_rope,
        knot_seven_rope,
        knot_eight_rope,
    ]

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        for step in range(steps):
            for rope in ropes:
                direction = rope.execute_instruction(direction)

    print("Part 2 ", len(ropes[-1].visited))


if __name__ == "__main__":
    main()
