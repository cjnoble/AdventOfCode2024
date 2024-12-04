import re


def read_text_file(file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]

    return data


def access_if_valid(data, x, y):

    if y < 0 or y >= len(data[0]):
        return False
    
    if x < 0 or x >= len(data):
        return False


    return data[x][y]


def part_1(data):

    count = 0

    for column in range(len(data[0])):
        for row in range(len(data)):

            if data[row][column] == "X":
                for j in [-1, 0, 1]:
                    for i in [-1, 0, 1]:
                        if access_if_valid(data, row + i, column + j) == "M":
                            if access_if_valid(data, row + 2*i, column + 2*j)== "A":
                                if access_if_valid(data, row + 3*i, column + 3*j) == "S":
                                    count += 1

    return count


def part_2(data):

    count = 0

    for column in range(len(data[0])):
        for row in range(len(data)):

            if data[row][column] == "A":

                if access_if_valid(data, row - 1, column - 1) == "M":

                    # Case of M.M/ .A. /S.S
                    if access_if_valid(data, row - 1, column + 1) == "M":
                        if access_if_valid(data, row + 1, column - 1) == "S":
                            if access_if_valid(data, row + 1, column + 1) == "S":
                                count += 1

                    # Case of M.S/ .A. /M.S
                    elif access_if_valid(data, row - 1, column + 1) == "S":
                        if access_if_valid(data, row + 1, column - 1) == "M":
                            if access_if_valid(data, row + 1, column + 1) == "S":
                                count += 1

                elif access_if_valid(data, row - 1, column - 1) == "S":
                        # Case of S.M/ .A. /S.M
                        if access_if_valid(data, row - 1, column + 1) == "M":
                            if access_if_valid(data, row + 1, column - 1) == "S":
                                if access_if_valid(data, row + 1, column + 1) == "M":
                                    count += 1

                        # Case of S.S/ .A. /M.M
                        elif access_if_valid(data, row - 1, column + 1) == "S":
                            if access_if_valid(data, row + 1, column - 1) == "M":
                                if access_if_valid(data, row + 1, column + 1) == "M":
                                    count += 1



    return count


if __name__ == "__main__":

    DAY = "04"
    data = read_text_file(f"{DAY}.txt")
    print(part_1(data))
    print(part_2(data))
