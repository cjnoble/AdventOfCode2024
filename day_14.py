import time, re
from PIL import Image

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


class Robot(object):

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self, max_x, max_y):
        self.x = (self.x + self.vx)%max_x
        self.y = (self.y + self.vy)%max_y
 
    def quadrant(self, max_x, max_y):
        mid_x = max_x//2
        mid_y = max_y//2

        if self.x < mid_x and self.y < mid_y:
            return 1
        elif self.x > mid_x and self.y < mid_y:
            return 2
        elif self.x < mid_x and self.y > mid_y:
            return 3
        elif self.x > mid_x and self.y > mid_y:
            return 4

        return 0
    
def parse_data(data):

    robots = []

    for row in data:
        #p=1,79 v=-93,36

        match = re.findall(r"(-*[\d]+),(-*[\d]+)", row)

        robots.append(Robot(int(match[0][0]), int(match[0][1]), int(match[1][0]), int(match[1][1])))
    
    return robots
        
def visualize_robots(robots, max_X, max_Y, printer=True):

    grid = [[0 for x in range(max_X)] for row in range(max_Y)]
    
    for robot in robots:
        grid[robot.y][robot.x] += 1 

    if printer:
        for row in grid:
            print(" ".join(str(cell) for cell in row))
        
    return grid

def save_image(grid, max_X, max_Y, output_filename):
    img = Image.new('RGB', (max_X, max_Y), color='black')  # Start with a black image

    pixels = img.load()

    for y in range(max_Y):
        for x in range(max_X):
            if grid[y][x] > 0:
                pixels[x, y] = (0, 255, 0)  # Green for robots (1 or more)
            else:
                pixels[x, y] = (0, 0, 0)    # Black for no robots

    img.save(output_filename)

def part_1(data, max_X, max_Y):

    robots = parse_data(data)

    visualize_robots(robots, max_X, max_Y)
    print("\n")

    for i in range(100):
        for robot in robots:
            robot.update(max_X, max_Y)

        visualize_robots(robots, max_X, max_Y)
        print("\n")

    
    sf_1 = sum([1 for robot in robots if robot.quadrant(max_X, max_Y) == 1])
    sf_2 = sum([1 for robot in robots if robot.quadrant(max_X, max_Y) == 2])
    sf_3 = sum([1 for robot in robots if robot.quadrant(max_X, max_Y) == 3])
    sf_4 = sum([1 for robot in robots if robot.quadrant(max_X, max_Y) == 4])

    safety_factor = (
    sf_1
    * sf_2
    * sf_3
    * sf_4
    )

    return safety_factor

def part_2(data, max_X, max_Y):

    robots = parse_data(data)

    #visualize_robots(robots, max_X, max_Y)
    print("\n")

    for i in range(6620):
        for robot in robots:
            robot.update(max_X, max_Y)

        grid = visualize_robots(robots, max_X, max_Y, printer=False)
    save_image(grid, max_X, max_Y, f"{i+1}.png")
  

if __name__ == "__main__":

    DAY = "14"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data, 101, 103))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    print(part_2(data, 101, 103))
    print(f"Part 2 finished in {time.time() - part_2_start} s")