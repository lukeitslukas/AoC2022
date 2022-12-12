def readFile(filename):
    # take filename, open file and return split data
    file = open(filename, "r")

    data = file.read().split("\n\n")

    file.close()

    return data


def splitInput(data):
    # starting at 0, split all cals up to each elf
    i = 0
    for elfCals in data:
        data[i] = elfCals.split("\n")
        i += 1

    return data


def calculateTotalCals(splitData):
    # calculate each elfs total calories then sort numerically
    totalCals = []

    for elfCals in splitData:
        tempCals = 0
        for elfCal in elfCals:
            if elfCal:
                tempCals = tempCals + int(elfCal)
        totalCals.append(tempCals)

    totalCals.sort(reverse=True)

    return totalCals


def calculateTopThree(totalCals):
    answer = 0

    for i in range(0, 3):
        answer = answer + totalCals[i]

    return answer


def main():
    filename = '1/input.txt'

    splitDataSet = readFile(filename)

    calculatedDataSet = splitInput(splitDataSet)

    totalCalsSet = calculateTotalCals(calculatedDataSet)

    print(calculateTopThree(totalCalsSet))


main()
