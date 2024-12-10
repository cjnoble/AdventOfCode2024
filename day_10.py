import time
from useful_code import Point

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def get_next_points(point:Point, grid:list):

    next_points = []

    for i in [1, 0, -1]:
        for j in [1, 0, -1]:

            if i*j == 0 and (i != 0 or j!= 0) :
                next_point = Point(point.x+i, point.y+j)

                if next_point.in_bounds(grid) and next_point.get_data(grid) == 1 + point.get_data(grid):
                    next_points.append(next_point)

    return next_points



def count_9points (point:Point, grid:list, end_points:set):


    if point.get_data(grid) == 9:
        end_points.add(point)
        return 1
        
    else:

        next_points = get_next_points(point, grid)

        if len(next_points) == 0:
            return 0
        
        else:
            count = 0

            for point in next_points:
                count += count_9points(point, grid, end_points)

    return count


def count_trails (point:Point, grid:list):


    if point.get_data(grid) == 9:
        return 1
        
    else:

        next_points = get_next_points(point, grid)

        if len(next_points) == 0:
            return 0
        
        else:
            count = 0

            for point in next_points:
                count += count_trails(point, grid)

    return count


def part_1(data):

    grid = [[int(i) for i in row] for row in data]

    #start_points = [[Point(x, y) for x, val in enumerate(row) if val == 0] for y, row in enumerate(data)]

    start_points = [Point(x, y) for y, row in enumerate(grid) for x, val in enumerate(row) if val == 0]

    trailhead_score = 0

    for start in start_points:

        end_points = set()
        count_9points(start, grid, end_points)

        trailhead_score += len(end_points)

    return trailhead_score

def part_2(data):

    grid = [[int(i) for i in row] for row in data]

    start_points = [Point(x, y) for y, row in enumerate(grid) for x, val in enumerate(row) if val == 0]

    trailhead_score = 0

    for start in start_points:

        trailhead_score += count_trails(start, grid)

    return trailhead_score

if __name__ == "__main__":

    DAY = "10"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    print(part_2(data))
    print(f"Part 2 finished in {time.time() - part_2_start} s")