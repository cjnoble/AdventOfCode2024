import re
from enum import Enum
from copy import deepcopy

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data



class Dir(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4


class Guard(object):

    next_dir = {Dir.Up: (0, -1), Dir.Right: (1, 0), Dir.Down: (0, 1), Dir.Left: (-1,  0)}


    def __init__(self, x, y, dir:Dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.visited = set()
        self.loop_check = set()
        self.visited_dir = list()
    

    @classmethod
    def from_location(cls, location):

        return cls(*location)


    def print_grid(self, grid):
        for row in grid:
            print(row)

        print("\n")


    def loop_checker(self):
        current = (self.x, self.y, self.dir)
        if current in self.loop_check:   
            return True
        else:
            self.loop_check.add(current)
            return False 


    def get_loop_coords(self):
        if not self.loop_checker():
            raise Exception("No Loops")
        
        else:
            current = (self.x, self.y, self.dir)
            loop_index = self.visited_dir.index(current)

            return self.visited_dir[loop_index:]


    def rotate_right(self):
        self.dir = Dir((self.dir.value % len(Dir)) + 1) # Rotate 90 degrees clockwise

    def update(self, grid):

        self.visited.add((self.x, self.y))
        self.visited_dir.append((self.x, self.y, self.dir))

        if self.loop_checker():
            return 1

        next = (self.x + self.next_dir[self.dir][0], self.y + self.next_dir[self.dir][1])

        if next[0] < 0 or next[1] < 0:
            raise IndexError

        if grid[next[1]][next[0]] == "#":

            self.rotate_right()
            
            #self.print_grid(grid)

        else:

            assert 0 <= self.x < len(grid[self.y]), f"self.x ({self.x}) is out of bounds for row of length {len(grid[self.y])}"

            #grid[self.y] = grid[self.y][:self.x] + "X" + (grid[self.y][self.x+1:] if self.x+1 < len(grid[self.y]) else "")

            # Ensure row consistency
            assert len(grid[self.y]) == len(grid[0]), "Row lengths are inconsistent!"

            self.x = next[0]
            self.y = next[1]

        return 0    


def part_1(data):

    guard_symbols = {"^": Dir.Up, ">": Dir.Right, "V": Dir.Down, "<": Dir.Left}

    # find the guard
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val in (guard_symbols.keys()):
                guard = Guard(x, y, guard_symbols[val])
                

    while True:
        try:
            guard.update(data)
        except IndexError:
            break

    return len(guard.visited)

def part_2(data):

    guard_symbols = {"^": Dir.Up, ">": Dir.Right, "V": Dir.Down, "<": Dir.Left}

    # find the guard
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val in (guard_symbols.keys()):
                guard = Guard(x, y, guard_symbols[val])
                

    while True:
        try:
            guard.update(data)
        except IndexError:
            break

    visited = guard.visited_dir
    
    #There are all the place we need to check if they form loops

    blocker_locations = set()
    tested_blockers = set()

    start_location = visited[0]

    for location in visited:

        blocker = (location[0] + Guard.next_dir[location[2]][0], location[1] + Guard.next_dir[location[2]][1])

        if blocker in tested_blockers:
            continue # visited earlier on 

        if blocker[0] == start_location[0] and blocker[1] == start_location[1] :
            continue #No blocker at start

        if blocker[0] < 0 or blocker[1] < 0 or blocker[1] >= len(data) or blocker[0] >= len(data[blocker[1]]):
            continue #outside grid so go to next

        if blocker in blocker_locations:
            continue #No point checking if in list already

        if data[blocker[1]][blocker[0]] == "#":
            continue #Already a blocker there

        data_with_blocker = deepcopy(data)
        data_with_blocker[blocker[1]] = data_with_blocker[blocker[1]][:blocker[0]] + "#" + (data_with_blocker[blocker[1]][blocker[0]+1:] if blocker[0]+1 < len(data_with_blocker[blocker[1]]) else "")

        # if location in known_loop_locations:
        #     break

        test_guard = Guard.from_location(location)
        test_guard.rotate_right()

        status = 0
        try:
            while status == 0:
                status = test_guard.update(data_with_blocker)


        except IndexError:
            #not in a loop, go to next
            tested_blockers.add(blocker)
            continue

        # We are in a loop
        blocker_locations.add(blocker)
        # for loc in test_guard.visited_dir:
        #     known_loop_locations.add(loc)

    #print(blocker_locations)

    return len(blocker_locations)

if __name__ == "__main__":

    DAY = "06"
    data = read_text_file(f"{DAY}.txt")
    print(part_1(data))
    print(part_2(data))