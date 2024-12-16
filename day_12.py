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
        seen_points = set()
        edge_list = set()

        # Generate edges for each point
        for p in self.points:
            edges = [
                Point(p.x + 0.5, p.y), Point(p.x - 0.5, p.y),  # Horizontal edges
                Point(p.x, p.y + 0.5), Point(p.x, p.y - 0.5)   # Vertical edges
            ]

            for edge in edges:
                if edge in edge_list:
                    edge_list.remove(edge)  # Remove shared edges (internal edges)
                else:
                    edge_list.add(edge)    # Add unique edges

            seen_points.add(p)

        # Count the number of unique sides
        sides = self.count_sides(edge_list)
        return sides

    def count_sides(self, edge_list: set):
        sides = 0

        inital_edges = edge_list.copy()

        while edge_list:
            # Start a new edge traversal
            current_edge = edge_list.pop()
            sides += 1

            stack = [current_edge]
            while stack:
                edge = stack.pop()

                # Determine the orientation of the edge
                if edge.x == int(edge.x):  # Vertical edge
                    neighbors = []
                    # y edge
                    y_edges = [Point(edge.x + 0.5, edge.y+0.5), Point(edge.x + 0.5, edge.y-0.5)]

                    if y_edges[0] not in inital_edges and y_edges[0] not in inital_edges:
                        neighbors.append(Point(edge.x + 1, edge.y))
                    
                    y_edges = [Point(edge.x - 0.5, edge.y+0.5), Point(edge.x - 0.5, edge.y-0.5)]

                    if y_edges[0] not in inital_edges and y_edges[0] not in inital_edges:
                        neighbors.append(Point(edge.x - 1, edge.y))

                else:  # Horizontal edge
                    neighbors = []
                    # y edge
                    y_edges = [Point(edge.x + 0.5, edge.y+0.5), Point(edge.x - 0.5, edge.y+0.5)]

                    if y_edges[0] not in inital_edges and y_edges[0] not in inital_edges:
                        neighbors.append(Point(edge.x, edge.y+1))
                    
                    y_edges = [Point(edge.x + 0.5, edge.y-0.5), Point(edge.x - 0.5, edge.y-0.5)]

                    if y_edges[0] not in inital_edges and y_edges[0] not in inital_edges:
                        neighbors.append(Point(edge.x, edge.y-1))

                for neighbor in neighbors:
                    if neighbor in edge_list:
                        edge_list.remove(neighbor)
                        stack.append(neighbor)

        return sides    


    def get_fence_cost_part1(self):
        return self.get_area()*self.get_perimeter()
    
    def get_fence_cost_part2(self):
        return self.get_area()*self.get_sides()
    
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

    def __repr__(self):
        # Determine the bounds of the region for visualization
        min_x = min(p.x for p in self.points)
        max_x = max(p.x for p in self.points)
        min_y = min(p.y for p in self.points)
        max_y = max(p.y for p in self.points)

        # Create a grid to represent the region
        grid = [["." for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]
        for p in self.points:
            grid[p.y - min_y][p.x - min_x] = self.ID

        # Convert grid to a string representation
        grid_str = "\n".join("".join(row) for row in grid)

        # Return the detailed representation
        return (
            f"Region(ID={self.ID}, Area={self.get_area()}, Perimeter={self.get_perimeter()}, Sides={self.get_sides()})\n"
            f"Visualization:\n{grid_str}"
        )

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

    return sum([region.get_fence_cost_part1() for region in distinct_regions])


def part_2(data):

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
        print(region.__repr__())

    return sum([region.get_fence_cost_part2() for region in distinct_regions])


if __name__ == "__main__":

    DAY = "12"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    print(part_2(data))
    print(f"Part 2 finished in {time.time() - part_2_start} s")
