import re
from collections import Counter
from functools import reduce

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    
    return data


def parse_data(data):

    data = [line.split() for line in data]

    list_1 = [int(row[0]) for row in data]

    list_2 = [int(row[1]) for row in data]

    return list_1, list_2

def part_1(data):

    list_1, list_2 = parse_data(data)    

    list_1.sort()
    list_2.sort()

    dist = 0

    for i1, i2 in zip(list_1, list_2):
        dist += abs(i1-i2)

    return dist

def part_2_Counter(data):

    list_1, list_2 = parse_data(data)

    list_2_count = Counter(list_2)

    score = 0

    for i1 in list_1:
        score += i1 * list_2_count[i1]

    return score

def part_2(data):

    list_1, list_2 = parse_data(data)

    score = 0

    for i1 in list_1:
        score += i1 * get_count(list_2, i1)

    return score

def get_count(a_list, i):

    return sum([a == i for a in a_list])
    

if __name__ == "__main__":

    DAY = "01"
    data = read_text_file(f"{DAY}.txt")
    print(part_1(data))
    print(part_2(data))