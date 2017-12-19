"""
Advent of Code 2017
Python

Wanted to use eval for solving this.
Things get weird -- probably because I got started and then did not touch what code I had for a while. Got what I was trying to do working.
"""

with open("day8_input.txt", "r") as f:
    instructions = [instruction.split()
                    for instruction in f.read().splitlines()]


def part1():
    # >>> eval(asdf[-3]+asdf[-2]+asdf[-1])
    values = {}

    # instructions = [['wui', 'inc', '-120', 'if', 'i', '>', '-2038']]
    for instruction in instructions:
        # print(instruction)
        # print(values)
        if str(instruction[-3]) in values:
            if str(instruction[0]) not in values:
                values.update({instruction[0]: 0})
            #                               value           operator            value
            # if eval(str(values[str(instruction[-3])]) + instruction[-2] + instruction[-1]):
            if eval(str(values[str(instruction[-3])]) + instruction[-2] + instruction[-1]):
                # do thing
                if instruction[1] == "inc":
                    values[instruction[0]] += int(instruction[2])
                if instruction[1] == "dec":
                    values[instruction[0]] -= int(instruction[2])

        # have to initialize
        else:
            values.update({instruction[-3]: 0})
            # print("NEW!", values)
            # handle first
            if str(instruction[0]) not in values:
                values.update({instruction[0]: 0})

            if eval(str(values[str(instruction[-3])]) + instruction[-2] + instruction[-1]):
                # do thing
                if instruction[1] == "inc":
                    values[instruction[0]] += int(instruction[2])
                if instruction[1] == "dec":
                    values[instruction[0]] -= int(instruction[2])

    return max(values.values())


print("Part One...", part1())
# print("Part Two...", part2())
