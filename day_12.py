import time
from useful_code import Point
from functools import reduce
from itertools import cycle


def read_text_file(file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]

    return data


class Region(object):

    def __init__(self, ID: str, point=None):
        self.ID = ID
        self.points = []

        if point:
            self.add_point(point)

    def add_point(self, point: Point):

        self.points.append(point)

    def get_area(self):
        return len(self.points)

    def get_perimeter(self):

        perimeter = 0
        seen_points = []

        for p in self.points:
            perimeter += 4

            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            
                if Point(p.x-i, p.y-j) in seen_points:
                    perimeter -= 2


            seen_points.append(p)
                

        return perimeter

    def get_sides(self):

        current_point = self.points[0]
        sides = 0

        dir_cycle = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])

        while True:

            for count in range(4):
                i, j = next(dir_cycle)
                next_point = Point(current_point.x+i, current_point.x+j)
                if next_point in self.points:
                
                    if count != 1:
                        sides += 1

                    current_point = next_point

                    break
            
            #recycle dir
            for _ in range(3):
                next(dir_cycle)
        
        return

    def get_fence_cost(self):
        return self.get_area()*self.get_perimeter()

    def __repr__(self):
        return f"({self.ID}: {','.join(str(p) for p in self.points)})"
    
    def __str__(self):
         return f"({self.ID}: {','.join(str(p) for p in self.points)})"
    
    def __eq__(self, other):
        if isinstance(other, Region):
            return self.ID == other.ID and reduce(lambda x, y: x and y, [p1==p2 for p1, p2 in zip(self.points, other.points)])
        return False

    def __hash__(self):
        return hash(str(self))
    
    def merge_regions(self, other):

        self.points.extend(other.points)




def part_1(data):

    regions = {}

    for y, row in enumerate(data):
        for x, id in enumerate(row):
            p = Point(x, y)

            lhs_point = Point(x-1, y)
            up_point = Point(x, y-1)


            if lhs_point.in_bounds(data) and regions[lhs_point].ID == id and up_point.in_bounds(data) and regions[up_point].ID == id and regions[lhs_point] is not regions[up_point]:
                #We need to merge the regions:
                regions[lhs_point].merge_regions(regions[up_point])

                for p_adjust in regions[up_point].points:
                    regions[p_adjust] = regions[lhs_point]


            if lhs_point.in_bounds(data) and regions[lhs_point].ID == id:
                regions[lhs_point].add_point(p)
                regions[p] = regions[lhs_point]
            elif up_point.in_bounds(data) and regions[up_point].ID == id:
                regions[up_point].add_point(p)
                regions[p] = regions[up_point]
            else:
                regions[p] = Region(id, p)


    distinct_regions = set(regions.values())

    for region in distinct_regions:
        print(region.ID, region.get_area(), region.get_perimeter())

    return sum([region.get_fence_cost() for region in distinct_regions])


def part_2(data):

    return


if __name__ == "__main__":

    DAY = "12"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    print(part_2(data))
    print(f"Part 2 finished in {time.time() - part_2_start} s")
