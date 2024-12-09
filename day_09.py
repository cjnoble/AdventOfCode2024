import time
from collections import namedtuple

Block = namedtuple("Block", ["ID", "Length", "Moved"])
Space = namedtuple("Space", ["Length"])

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def parse_input(data):

    data = [int(i) for i in data[0]]

    length = sum(data)

    system = []

    ID = 0
    data_iter = iter(data)

    while True:

        try:
            file_length = next(data_iter)
            system.extend([Block(ID, file_length, False) for i in range(file_length)])
            
            space_length = next(data_iter)
            system.extend([Space(space_length) for i in range(space_length)])

            ID += 1

        except StopIteration:
            break

    return system

def get_checksum(system):

    checksum = 0

    for i, block in enumerate(system):
        if not isinstance(block, Space):
            checksum += i * block.ID

    return checksum

def part_1(data):

    system = parse_input(data)

    i = 0
    while True:

        if i >= len(system):
            break

        if isinstance(system[i], Space):

            end_data = None

            while True:
                end_data = system.pop()
                if not isinstance(end_data, Space):
                    break
                elif i == len(system):
                    end_data = None
                    break

            if end_data:
                system[i] = end_data 

        i += 1

    return get_checksum(system)

def part_2(data):

    system = parse_input(data)

    pointer = len(system)

    while pointer > 0:

        pointer -= 1

        if isinstance(system[pointer], Space):
            continue

        else:
            if not system[pointer].Moved:

                search = 0
                while search < pointer:

                    if isinstance(system[search], Space):

                        space_length = 1
                        while True:
                            if search + space_length >= len(system):
                                break
                            elif not isinstance(system[search + space_length], Space):
                                break
                            space_length += 1
                            
                        if space_length >= system[pointer].Length:
                        
                            for i in range(system[pointer].Length):

                                if not isinstance(system[pointer - i], Block):
                                    print("problmn")

                                assert isinstance(system[pointer - i], Block )
                                
                                space_temp = system[search + i]

                                system[search + i] = system[pointer - i]
                                system[search + i] = system[search + i]._replace(Moved=True)
                                system[pointer - i] = space_temp
                            break
                        search += space_length
                    else:
                        search += system[search].Length

                #pointer -= system[search].Length
                continue

    return get_checksum(system)

if __name__ == "__main__":

    DAY = "09"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    print(part_2(data))
    print(f"Part 2 finished in {time.time() - part_2_start} s")