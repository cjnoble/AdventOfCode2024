import re
import time

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def test_part1(test_value, numbers:list, sum=0):

    if len(numbers) == 0:
        if sum == test_value:
            return True
        return False
    
    next_num = numbers.pop(0)

    if test_part1(test_value, numbers.copy(), sum+next_num):
        return True
    elif sum != 0:
        return test_part1(test_value, numbers.copy(), sum*next_num)

    return False

def test_part2(test_value, numbers:list, sum=0):

    if len(numbers) == 0:
        if sum == test_value:
            return True
        return False
    
    next_num = numbers.pop(0)

    if test_part2(test_value, numbers.copy(), sum+next_num):
        return True
    elif sum != 0:
        if test_part2(test_value, numbers.copy(), sum*next_num):
            return True
        else:
            return test_part2(test_value, numbers.copy(), int(str(sum) + str(next_num)))


    return False


def part_1(data):

    res = 0

    for row in data:
        row = row.split()
        test_value = int(row[0][:-1]) #remove trailing :
        numbers = [int(i) for i in row[1:]]

        if test_part1(test_value, numbers):
            res += test_value

    return res

def part_2(data):

    res = 0

    for row in data:
        row = row.split()
        test_value = int(row[0][:-1]) #remove trailing :
        numbers = [int(i) for i in row[1:]]

        if test_part2(test_value, numbers):
            res += test_value

    return res

if __name__ == "__main__":

    DAY = "07"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    print(part_2(data))
    print(f"Part 2 finished in {time.time() - part_2_start} s")