# Path: day9/rope_bridge.py

DIRECTIONS = ["U", "D", "L", "R", "UR", "UL", "DR", "DL"]


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


class Rope:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.visited = list()

    def execute_instruction(self, direction):
        # move the head
        print(f"moving the head {direction}")
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
        print(f"diff: {diff}")

        if diff == [0, 0]:
            print("head and tail are in the same position")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return True

        if diff in adjacent or diff in diagonally_adjacent:
            print("head and tail are adjacent")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return True

        # figure out which direction the tail should move
        if diff == two_to_left:
            print("moving the tail to the left")
            self.tail.move_a_step("L")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return True
        if diff == two_to_right:
            print("moving the tail to the right")
            self.tail.move_a_step("R")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return True
        if diff == two_up:
            print("moving the tail up")
            self.tail.move_a_step("U")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return True
        if diff == two_down:
            print("moving the tail down")
            self.tail.move_a_step("D")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return True
        if diff in up_left_diagonal:
            print("moving the tail up left")
            self.tail.move_a_step_diagonal("UL")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return True
        if diff in up_right_diagonal:
            print("moving the tail up right")
            self.tail.move_a_step_diagonal("UR")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return True
        if diff in down_left_diagonal:
            print("moving the tail down left")
            self.tail.move_a_step_diagonal("DL")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return True
        if diff in down_right_diagonal:
            print("moving the tail down right")
            self.tail.move_a_step_diagonal("DR")
            if not (self.tail.x, self.tail.y) in self.visited:
                self.visited.append((self.tail.x, self.tail.y))
            return True


def main():
    instructions = open("input.txt", "r").read().splitlines()
    rope = Rope(head=Point(0, 0), tail=Point(0, 0))
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        for step in range(steps):
            rope.execute_instruction(direction)

    print(len(rope.visited))


if __name__ == "__main__":
    main()
