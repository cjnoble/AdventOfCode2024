import time
import re
from collections import deque
from copy import deepcopy

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data

def sign(x):

    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
    

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_data(self, grid):

        if self.in_bounds(grid):
            return grid[self.y][self.x]
        
        else:
            raise Exception("Not in bounds")

    def in_bounds(self, grid):
        if self.x < 0 or self.y < 0 :
            return False
        
        if self.y >= len(grid) or self.x >= len(grid[self.y]):
            return False
        
        return True
    
    def get_antinodes_part1(self, other, grid):

        x_dist = other.x - self.x
        y_dist = other.y - self.y

        antinodes = []

        antinodes.append(Point(self.x - x_dist, self.y - y_dist))
        antinodes.append(Point(other.x + x_dist, other.y + y_dist))

        return [a for a in antinodes if a.in_bounds(grid)]
    
    def get_antinodes_part2(self, other, grid):

        x_dist = other.x - self.x
        y_dist = other.y - self.y

        assert abs(x_dist) + abs(y_dist) != 0

        antinodes = []

        i = 0
        while True:

            antinodes.append(Point(self.x - x_dist*i, self.y - y_dist*i))

            if not antinodes[-1].in_bounds(grid):
                break

            i += 1
        
        i = 0
        while True:

            antinodes.append(Point(self.x + x_dist*i, self.y + y_dist*i))

            if not antinodes[-1].in_bounds(grid):
                break

            i += 1

        return [a for a in antinodes if a.in_bounds(grid)]

    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"


def part_1(data):

    antinodes = set()

    for y, row in enumerate(data):
        for x, node in enumerate(row):

            if re.match("[0-9A-Za-z]", node):
                
                #check lines for nodes with same id

                antenna = Point(x, y)
                frequency = node

                print(f"Antenna found at: ({antenna.x},{antenna.y}), frequency: {frequency}")

                test_antenna = deque()

                for test_y, test_row in enumerate(data):
                    for test_x, test_node in enumerate(test_row):
                        test = Point(test_x, test_y)
                        if test_node == frequency and test.x != antenna.x and test.y != antenna.y:
                            test_antenna.append(test)

                print(f"Found test antennas {test_antenna}")

                while test_antenna:
                    test = test_antenna.pop()

                    antinodes.update((a.x, a.y) for a in antenna.get_antinodes_part1(test, data))

    print("Found antinodes:")
    for antinode in antinodes:
        print(antinode)

    return len(antinodes)

def part_2(data):

    antinodes = set()

    for y, row in enumerate(data):
        for x, node in enumerate(row):

            if re.match("[0-9A-Za-z]", node):
                
                #check lines for nodes with same id

                antenna = Point(x, y)
                frequency = node

                print(f"Antenna found at: ({antenna.x},{antenna.y}), frequency: {frequency}")

                test_antenna = deque()

                for test_y, test_row in enumerate(data):
                    for test_x, test_node in enumerate(test_row):
                        test = Point(test_x, test_y)
                        assert test.in_bounds(data)
                        if test_node == frequency and test.x != antenna.x and test.y != antenna.y:
                            test_antenna.append(test)

                print(f"Found test antennas {test_antenna}")

                while test_antenna:
                    test = test_antenna.pop()

                    antinodes.update((a.x, a.y) for a in antenna.get_antinodes_part2(test, data))


    print("Found antinodes:")
    copy_grid = deepcopy(data)
    for antinode in antinodes:
        print(antinode)
        copy_grid[antinode[1]] = copy_grid[antinode[1]][:antinode[0]] + "#" + copy_grid[antinode[1]][antinode[0] + 1:]

    for row in copy_grid:
        print(row)

    

    return len(antinodes)

if __name__ == "__main__":

    DAY = "08"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    print(part_2(data))
    print(f"Part 2 finished in {time.time() - part_2_start} s")