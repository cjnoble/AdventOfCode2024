import time



def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def parse_input(data):

    data = [int(i) for i in data]

    length = sum(data)

    system = []

    ID = 0
    data_iter = iter(data)
    while True:

        try:
            file_length = next(data_iter)
            system.extend([ID for i in range(file_length)])
            
            space = next(data_iter)
            system.extend(["." for i in range(space)])

            ID += 1

        except StopIteration:
            break


def part_1(data):

    parse_input(data)

    return

def part_2(data):

    return

if __name__ == "__main__":

    DAY = "09"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    print(part_2(data))
    print(f"Part 2 finished in {time.time() - part_2_start} s")