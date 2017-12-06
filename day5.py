"""
Advent of Code 2017
Python
"""

def part1():
    with open("day5_input.txt", "r") as f:
        lines = [int(line) for line in f.read().splitlines()]

    num = 0
    steps = 0
    while True:
        try:
            # get positions value to see how 'far' to go
            jump = lines[num]
            # increment old position by one
            lines[num] += 1
            # print(lines, num, jump)
            num += jump
            steps += 1
        except IndexError:
            # WE FREE!
            return steps


def part2():
    with open("day5_input.txt", "r") as f:
        lines = [int(line) for line in f.read().splitlines()]

    num = 0
    steps = 0
    while True:
        try:
            jump = lines[num]
            
            # changes to incrementing
            if jump >= 3:
                lines[num] -= 1
            else:
                lines[num] += 1

            # print(lines, num, jump)
            num += jump
            steps += 1
        except IndexError:
            # WE FREE!
            return steps


print("Part One...", part1())
print("Part Two...", part2())
