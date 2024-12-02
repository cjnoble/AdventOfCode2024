import re
from itertools import tee


def read_text_file(file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]

        data = [row.split() for row in data]
        data = [[int(i) for i in row] for row in data]

    return data


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def test_safe(row):
    diffs = [p2 - p1 for p1, p2 in pairwise(row)]

    # Test if all assending or all desending
    if max(diffs) * min(diffs) <= 0:
        return False

    else:
        if max(diffs) > 3 or min(diffs) < -3:
            return False

    return True


def part_1(data):

    safe_rows = 0

    for row in data:
        safe_rows += 1 if test_safe(row) else 0

    return safe_rows


def part_2(data):

    safe_rows = 0

    for row in data:
        if test_safe(row):
            safe_rows += 1

        else:
            for i in range(len(row)):
                test_row = row[0:i] + row[i+1: len(row)]

                if test_safe(test_row):
                    safe_rows += 1
                    break

    return safe_rows


if __name__ == "__main__":

    DAY = "02"
    data = read_text_file(f"{DAY}.txt")
    print(part_1(data))
    print(part_2(data))
