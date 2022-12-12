def readFile(filename):
    data = open(filename, "r").read().split('\n')
    index = 0

    for line in data:
        data[index] = [line.split(' ')[1], line.split(' ')[3], line.split(' ')[5]]
        index += 1

    return data


def moveCrates(data):
    crate = [
        ['S', 'C', 'V', 'N'],
        ['Z', 'M', 'J', 'H', 'N', 'S'],
        ['M', 'C', 'T', 'G', 'J', 'N', 'D'],
        ['T', 'D', 'F', 'J', 'W', 'R', 'M'],
        ['P', 'F', 'H'],
        ['C', 'T', 'Z', 'H', 'J'],
        ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'],
        ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'],
        ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']
    ]

    topCrates = ''
    for line in data:
        for i in range(0, int(line[0])):
            tempCrate = crate[int(line[1]) - 1].pop(len(crate[int(line[1]) - 1]) - 1)
            crate[int(line[2]) - 1].extend(tempCrate)

    for temp in crate:
        topCrates += temp[len(temp) - 1]

    print(topCrates)


def moveMultipleCrates(data):
    crate = [
        ['S', 'C', 'V', 'N'],
        ['Z', 'M', 'J', 'H', 'N', 'S'],
        ['M', 'C', 'T', 'G', 'J', 'N', 'D'],
        ['T', 'D', 'F', 'J', 'W', 'R', 'M'],
        ['P', 'F', 'H'],
        ['C', 'T', 'Z', 'H', 'J'],
        ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'],
        ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'],
        ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']
    ]

    topCrates = ''
    for line in data:
        tempCrates = []
        for i in range(0, int(line[0])):
            tempCrates.insert(0, crate[int(line[1]) - 1].pop(len(crate[int(line[1]) - 1]) - 1))
        crate[int(line[2]) - 1].extend(tempCrates)

    for temp in crate:
        topCrates += temp[len(temp) - 1]

    print(topCrates)


def main():
    data = readFile('5/input.txt')

    moveCrates(data)

    moveMultipleCrates(data)


main()
