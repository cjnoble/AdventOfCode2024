import time
from useful_code import Point
from collections import deque
from functools import reduce

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data

instruction_dict = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

class Robot(object):

    def __init__(self, position:Point):
        self.position = position


    def update(self, instruction:str, boxes, grid):

        next_point = Point(self.position.x + instruction_dict[instruction][0], self.position.y + instruction_dict[instruction][1])

        if next_point.in_bounds(grid) and next_point.get_data(grid) != "#":
            ## possible valid next position

            check_positions = []
            for box in boxes:
                if isinstance(box, WideBox):
                    check_positions.extend(box.positions)
                else:
                    check_positions.append(box.position)

            if next_point not in check_positions:
                self.position = next_point
                return True
            else:
                # There is a box

                box = [box for box in boxes if box.check_position(next_point)][0]

                if box.update(instruction, boxes, grid):
                    self.position = next_point
                    return True

        return False

class Box(Robot):
    def check_position(self, point:Point):

        if point == self.position:
            return True
        else:
            return False
        
    def get_gps(self):
        return self.position.x + 100*self.position.y

class WideBox(Box):

    def __init__(self, positions:list):
        self.positions = positions

    def get_gps(self):
        return self.positions[0].x + 100*self.positions[0].y

    def check_position(self, point:Point):

        if point in self.positions:
            return True
        else:
            return False

    def update(self, instruction: str, boxes, grid, move=True):
        # Compute the next positions for the wide box
        next_points = [
            Point(pos.x + instruction_dict[instruction][0], pos.y + instruction_dict[instruction][1])
            for pos in self.positions
        ]

        # Check if all next positions are valid (in bounds and not walls)
        if not all(p.in_bounds(grid) and p.get_data(grid) != "#" for p in next_points):
            return False

        # Check for collisions with other boxes
        other_boxes = [box for box in boxes if box != self]
        boxes_to_move = set()
        for point in next_points:
            for box in other_boxes:
                if box.check_position(point):
                    # Attempt to move the blocking box
                    if not box.update(instruction, boxes, grid, move=False):
                        return False
                    boxes_to_move.add(box)

        # If all checks pass, move the box
        if move:
            self.positions = next_points
            for box in boxes_to_move:
                box.update(instruction, boxes, grid)

        return True


def get_gps(boxes):

    return sum([box.get_gps() for box in boxes])


def parse_data(data):

    boxes = []
    instructions = []
    grid = []

    for y, row in enumerate(data):

        if row == "":
            continue

        elif "<" in row or "^" in row or ">" in row or "v" in row:
            instructions.append(row)

        else:

            grid.append(row)

            for x, s in enumerate(row):
                if s == "@":
                    robot = Robot(Point(x, y))
                elif s == "O":
                    boxes.append(Box(Point(x, y)))

    instructions = "".join(instructions)

    return robot, boxes, instructions, grid

def parse_data_2(data):

    boxes = []
    instructions = []
    grid = []

    for y, row in enumerate(data):

        if row == "":
            continue

        elif "<" in row or "^" in row or ">" in row or "v" in row:
            instructions.append(row)

        else:

            grid_row = ""
            
            for x, s in enumerate(row):
                if s == "@":
                    robot = Robot(Point(2*x, y))
                    grid_row += "@."
                elif s == "O":
                    boxes.append(WideBox([Point(2*x, y), Point(2*x+1, y)]))
                    grid_row += "[]"

                elif s == ".":
                    grid_row += ".."

                elif s == "#":
                    grid_row +="##"

            grid.append(grid_row)

    instructions = "".join(instructions)

    return robot, boxes, instructions, grid

def part_1(data):

    robot, boxes, instructions, grid = parse_data(data)

    instructions = deque(instructions)

    while instructions:
        instruction = instructions.popleft()

        robot.update(instruction, boxes, grid)

    return get_gps(boxes)

def part_2(data):

    robot, boxes, instructions, grid = parse_data_2(data)

    instructions = deque(instructions)

    visualize_grid(robot, boxes, grid)

    while instructions:
        instruction = instructions.popleft()
        robot.update(instruction, boxes, grid)

        # Check for overlaps
        all_positions = [pos for box in boxes for pos in (box.positions if isinstance(box, WideBox) else [box.position])]
        if len(all_positions) != len(set(all_positions)):
            raise ValueError("Overlap detected between boxes!")
        
    visualize_grid(robot, boxes, grid)


    return get_gps(boxes)

def visualize_grid(robot, boxes, grid):
    """
    Visualize the grid with the robot and boxes after each instruction.

    :param robot: The Robot object.
    :param boxes: List of Box and WideBox objects.
    :param grid: The grid (list of strings).
    """
    # Create a mutable grid copy
    grid_visual = [list(row) for row in grid]

    # Clear any previous robot or box markers ('@', 'O', '[]')
    for y, row in enumerate(grid_visual):
        for x, char in enumerate(row):
            if char in {'@', 'O', '[', ']'}:
                grid_visual[y][x] = '.'  # Reset to empty space

    # Place the boxes
    for box in boxes:
        if isinstance(box, WideBox):
            for pos, symbol in zip(box.positions, "[]"):
                grid_visual[pos.y][pos.x] = symbol
        else:
            grid_visual[box.position.y][box.position.x] = 'O'

    # Place the robot
    grid_visual[robot.position.y][robot.position.x] = '@'

    # Convert grid back to strings and print it
    print("\n".join("".join(row) for row in grid_visual))
    print("\n" + "-" * 20 + "\n")


if __name__ == "__main__":

    DAY = "15"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    print(part_2(data))
    print(f"Part 2 finished in {time.time() - part_2_start} s")