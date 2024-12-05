import re
from collections import defaultdict
from functools import cmp_to_key

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def parse_input(data):

    rules = []
    pages = []

    for row in data:
        if "|" in row:
            rules.append([int(i) for i in row.split("|")])

        elif "," in row:
            pages.append([int(i) for i in row.split(",")])

    return rules, pages


def page_correct(page_list, rules_dict):

    correct = True

    for i in range(len(page_list)):
        page = page_list[i] 
        if page in rules_dict.keys():

            prev_pages = page_list[:i]
            next_pages = page_list[i+1:]

            for req_page in rules_dict[page]:

                if req_page in prev_pages:
                    correct = False
                    break

        if not correct:
            break

    return correct



def part_1(data):

    correct_sum = 0

    rules, pages = parse_input(data)

    rules_dict = defaultdict(lambda: list())

    for rule in rules:
        rules_dict[rule[0]].append(rule[1])

    for page_list in pages:

        correct = page_correct(page_list, rules_dict)

        if correct:
            print(f"Correct list {page_list}")
            correct_sum += page_list[len(page_list)//2]


    return correct_sum


class Comparer(object):

    def __init__(self, rules_dict):

        self.rules_dict = rules_dict
        

    def compare_func(self, x, y):

        if x in self.rules_dict[y]:
            return 1
        
        elif y in self.rules_dict[x]:
            return -1
        
        else:
            return 0


def part_2(data):

    result = 0

    incorrect_pages = []

    rules, pages = parse_input(data)

    rules_dict = defaultdict(lambda: list())

    comp = Comparer(rules_dict)

    for rule in rules:
        rules_dict[rule[0]].append(rule[1])

    for page_list in pages:

        if not page_correct(page_list, rules_dict):
            incorrect_pages.append(page_list)

    for incorrect_page in incorrect_pages:

        incorrect_page.sort(key=cmp_to_key(comp.compare_func))
        print(incorrect_page)

        result += incorrect_page[len(incorrect_page)//2]
       

    return result

if __name__ == "__main__":

    DAY = "05"
    data = read_text_file(f"{DAY}.txt")
    print(part_1(data))
    print(part_2(data))