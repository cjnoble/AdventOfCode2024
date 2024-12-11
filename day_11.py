import time
from collections import defaultdict

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def blink(data:defaultdict, n):

    for i in range(n):

        new_dict =  defaultdict(lambda :0)


        for key in data.keys():

            if key == 0:

                new_dict[1] += data[0]
            elif key < 10:
                new_dict[key*2024] += data[key]
            elif len(str(key))%2==0:
                k1 = int(str(key)[:len(str(key))//2])
                k2 = int(str(key)[len(str(key))//2:])

                new_dict[k1] += data[key]
                new_dict[k2] += data[key]

            else:
                new_dict[key*2024] += data[key]

        data = new_dict

    return data

def prepare_stone(data):
    stones = defaultdict(lambda :0)

    for stone in data[0].split():

        stones[int(stone)] += 1

    return stones


def part_1(data):

    stones = prepare_stone(data)

    stones = blink(stones, 25)

    return sum(stones.values())

def part_2(data):

    stones = prepare_stone(data)

    stones = blink(stones, 75)

    return sum(stones.values())

if __name__ == "__main__":

    DAY = "11"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    print(part_2(data))
    print(f"Part 2 finished in {time.time() - part_2_start} s")