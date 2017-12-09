"""
Advent of Code 2017
Python


"To do this, it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks.
It continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one."
"""
import csv
import copy


def part1():
    # with open("day6_example_input.txt", "r") as f:
    with open("day6_input.txt", "r") as f:
        nums = [int(num) for num in f.read().strip().split("\t")]

    # to keep track of previous number sequences had
    old_nums = []
    iterations = 0

    while True:
        # input()
        iterations += 1

        # oh... right.... lists are mutable...
        old_nums.append(copy.deepcopy(nums))

        where_the_giver_is = nums.index(max(nums))
        gift = nums[where_the_giver_is]

        # print(nums)
        # print("where: {}\tval: {}\t\tgift: {}".format(
        #     where_the_giver_is, nums[where_the_giver_is], gift))

        # begin gift giving
        current = where_the_giver_is
        nums[where_the_giver_is] = 0
        while gift > 0:
            try:
                # move on to the end of the list giving
                current += 1
                gift -= 1
                nums[current] += 1  # point of exception
                # print(nums)
                # print(gift)
            except IndexError:
                # go to start of list!
                current = 0
                nums[current] += 1
                # print(nums)
                # print(gift)

        # if this number sequence has appeared before
        if nums in old_nums:
            # print this for part 2
            # print(nums)
            return iterations


def part2():
    start = [0, 14, 13, 12, 11, 10, 8, 8, 6, 6, 5, 3, 3, 2, 1, 10]
    nums = [0, 14, 13, 12, 11, 10, 8, 8, 6, 6, 5, 3, 3, 2, 1, 10]

    iterations = 0

    while True:
        iterations += 1
        where_the_giver_is = nums.index(max(nums))
        gift = nums[where_the_giver_is]

        current = where_the_giver_is
        nums[where_the_giver_is] = 0
        while gift > 0:
            try:
                # move on to the end of the list giving
                current += 1
                gift -= 1
                nums[current] += 1  # point of exception
                # print(nums)
                # print(gift)
            except IndexError:
                # go to start of list!
                current = 0
                nums[current] += 1
                # print(nums)
                # print(gift)

        if nums == start:
            return iterations


print("Part One...", part1())
print("Part Two...", part2())
