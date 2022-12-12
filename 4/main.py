def readFile(filename):
    data = open(filename, "r").read().split('\n')
    index = 0
    for option in data:
        splitString = option.split(',')
        splitString = [splitString[0].split('-'), splitString[1].split('-')]
        data[index] = splitString
        index += 1

    return data


def checkEntireContainment(data):
    i = 0
    for line in data:
        ranges = [range(int(line[0][0]), int(line[0][1]) + 1), range(int(line[1][0]), int(line[1][1]) + 1)]
        if all(item in ranges[0] for item in ranges[1]) or all(item in ranges[1] for item in ranges[0]):
            i += 1

    return i


def checkSlightContainment(data):
    i = 0
    for line in data:
        ranges = [range(int(line[0][0]), int(line[0][1]) + 1), range(int(line[1][0]), int(line[1][1]) + 1)]
        if any(item in ranges[0] for item in ranges[1]) or any(item in ranges[1] for item in ranges[0]):
            i += 1

    return i


def main():
    splitData = readFile('4/input.txt')

    print(checkEntireContainment(splitData))

    print(checkSlightContainment(splitData))


main()
