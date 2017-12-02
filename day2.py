"""
Advent of Code 2017
Python
"""

import csv
from itertools import combinations


def part1():
    total = 0
    with open("day2_input.txt", "r") as tsv_file:
        # csv seems to quote everything. Specifying the quoting will quote what is specifided otherwise it will (for NONNUMERIC) turn it to a float.
        tsv_reader = csv.reader(tsv_file, delimiter="\t", quoting=csv.QUOTE_NONNUMERIC)

        for row in tsv_reader:
            additive = max(row) - min(row)
            # print("{}\t\t{}".format(additive,row))
            total += additive

    return int(total)


def part2():
    # want to check which numbers divide evenly with eachother -> then divide the big one by the small one -> add to total.
    total = 0

    with open("day2_input.txt", "r") as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter="\t", quoting=csv.QUOTE_NONNUMERIC)

        for row in tsv_reader:
            # print('~'*20)
            # create the possible 2 number combinations then divide the max by the min to see which pair evenly divides.
            possibles = combinations(row, 2)

            for pair in possibles:
                # print(pair, max(pair) / min(pair))
                if max(pair) % min(pair) == 0:
                    total += (max(pair) / min(pair))

        return int(total)


print("Part One...", part1())
print("Part Two...", part2())
