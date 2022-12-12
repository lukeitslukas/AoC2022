import collections

priority = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27,
    'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
    'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}


def readFile(filename):
    data = open(filename, "r").read().split('\n')
    index = 0
    for option in data:
        splitString = [option[slice(0, len(option) // 2)], option[slice(len(option) // 2, len(option))]]
        data[index] = splitString
        index += 1

    return data


def checkForUniqueChar(data):
    totalPriority = 0
    for items in data:
        counters = [collections.Counter(items[0]), collections.Counter(items[1])]
        letter = list((counters[0] & counters[1]).keys())[0]
        totalPriority += priority[letter]

    return totalPriority


def checkForBadges(data):
    totalBadgePriority = 0
    for i in range(0, len(data) - 1, 3):
        counters = [
            (collections.Counter(data[i][0]) + collections.Counter(data[i][1])),
            (collections.Counter(data[i + 1][0]) + collections.Counter(data[i + 1][1])),
            (collections.Counter(data[i + 2][0]) + collections.Counter(data[i + 2][1]))
        ]
        letter = list((counters[0] & counters[1] & counters[2]).keys())[0]
        totalBadgePriority += priority[letter]

    return totalBadgePriority


def main():
    data = readFile('3/input.txt')

    # print(checkForUniqueChar(data))

    print(checkForBadges(data))


main()
