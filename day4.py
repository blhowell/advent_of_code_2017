"""
Advent of Code 2017
Python
"""


def part1():
    """Check if 'word' repeats. Determines invalidity and subtracts from total to get valid lines."""
    total = 0
    invalid = 0

    with open("day4_input.txt", "r") as pass_file:
        passphrases = pass_file.read().splitlines()

    for passphrase in passphrases:
        total += 1
        passphrase = passphrase.split()
        for word in passphrase:
            if passphrase.count(word) > 1:
                # print(word, "invalid")
                invalid += 1
                break

    return total - invalid


def part2():
    """Sort each word for each passphrase. Check for matches. Determines invalidity and subtracts from total to get valid lines."""
    total = 0
    invalid = 0
    sorted_passphrases = []

    with open("day4_input.txt", "r") as pass_file:
        passphrases = pass_file.read().splitlines()

    # sort the passphrases for a sorted_passphrases list
    for passphrase in passphrases:
        passphrase = passphrase.split()
        bucket = []  # hold the phrases sorted 'words'
        for word in passphrase:
            bucket.append(''.join(sorted(word)))

        sorted_passphrases.append(bucket)

    for passphrase in sorted_passphrases:
        total += 1
        for word in passphrase:
            if passphrase.count(word) > 1:
                # print(word, "invalid")
                invalid += 1
                break

    return total - invalid


print("Part One...", part1())
print("Part Two...", part2())
