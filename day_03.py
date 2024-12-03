import re

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def get_mul(data):

    match = re.findall(r"mul\(([0-9][0-9]?[0-9]?),([0-9][0-9]?[0-9]?)\)", data)

    val = 0

    for row in match:
        val += int(row[0]) * int(row[1])
 
    return val


def part_1(data):

    data = "".join(data)

    return get_mul(data)

def part_2(data):

    data = "".join(data)

    data = re.split(r"(do\(\)|don't\(\))", data)

    current = "do()"

    val = 0

    for row in data:

        if row[0] == "d":
            current = row

        else:
            if current == "do()":
                val += get_mul(row)
    

    return val

if __name__ == "__main__":

    DAY = "03"
    data = read_text_file(f"{DAY}.txt")
    print(part_1(data))
    print(part_2(data))