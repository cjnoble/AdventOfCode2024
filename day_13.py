import time
import numpy as np
import re
from math import ceil, floor

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def parse_input(data, offset = 0):

    M_list = []
    Prize_list = []

    for i in range(ceil(len(data)/4)):
        A = data[4*i]
        B = data[4*i+1]
        Prize = data[4*i+2]

        A_match = re.findall(r"[XY]\+([0-9]+)", A)
        xA = int(A_match[0])
        yA = int(A_match[1])

        B_match = re.findall(r"[XY]\+([0-9]+)", B)
        xB = int(B_match[0])
        yB = int(B_match[1])

        Prize_match = re.findall(r"[XY]\=([0-9]+)", Prize)
        Prize_x = int(Prize_match[0]) + offset
        Prize_y = int(Prize_match[1]) + offset

        M = np.array([[xA, xB], [yA, yB]])
        Prize =  np.array([Prize_x, Prize_y])
        M_list.append(M)
        Prize_list.append(Prize)

    return M_list, Prize_list


def AB_generator(N):
    for A in range(N):
        for B in range(N):
            yield A, B

def part_1_brute_force(data):

    cost = 0
    AB_list = []

    M_list, Prize_list = parse_input(data)

    for M, Prize in zip(M_list, Prize_list):

        for A,B in AB_generator(100):

            if M[0][0]*A + M[0][1]*B == Prize[0] and M[1][0]*A + M[1][1]*B == Prize[1]:

                #print(A, B)
                cost += 3*A + B
                AB_list.append(tuple((A, B)))
                break

    return cost, AB_list

def part_1(data):

    M_list, Prize_list = parse_input(data)

    x_list = [np.linalg.solve(M, Prize) for M, Prize in zip(M_list, Prize_list)]

    cost = 0
    tol = 1/20
    x_list_solve = [x for x in x_list if abs(x[0] - round(x[0])) < tol and abs(x[1] - round(x[1])) < tol]
    x_removed = [x for x in x_list if not np.any(np.isin(x, x_list_solve))]

    print("\n")
    for x in x_list_solve:
        #print(x)
        cost += 3*round(x[0])
        cost += 1*round(x[1])

    # print("\n")
    # for x in x_removed:
    #     print(x)

    return cost, x_list_solve

def part_2(data):

    M_list, Prize_list = parse_input(data, 10000000000000)

    x_list = [np.linalg.solve(M, Prize) for M, Prize in zip(M_list, Prize_list)]

    cost = 0
    tol = 1/20
    x_list_solve = [x for x in x_list if abs(x[0] - round(x[0])) < tol and abs(x[1] - round(x[1])) < tol]
    x_removed = [x for x in x_list if not np.any(np.isin(x, x_list_solve))]

    print("\n")
    for x in x_list_solve:
        #print(x)
        cost += 3*round(x[0])
        cost += 1*round(x[1])

    # print("\n")
    # for x in x_removed:
    #     print(x)

    return cost, x_list_solve

if __name__ == "__main__":

    DAY = "13"
    data = read_text_file(f"{DAY}.txt")

    cost, AB_BF_list = part_1_brute_force(data)
    print(cost)

    part_1_start = time.time()
    cost, AB_list = part_1(data)
    print(cost)
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    # for i, j in zip(AB_BF_list, AB_list):
    #     print(i, j)

    part_2_start = time.time()
    print(part_2(data)[0])
    print(f"Part 2 finished in {time.time() - part_2_start} s")