def readFile(filename):
    data = open(filename, "r").read().split('\n')
    i = 0
    for option in data:
        data[i] = option.split(' ')
        i += 1

    return data


def rockPaperScissorsPart1(data):
    # create total points
    totalPoints = 0

    for options in data:
        # points for shape
        if options[1] == 'X':
            totalPoints += 1
        elif options[1] == 'Y':
            totalPoints += 2
        elif options[1] == 'Z':
            totalPoints += 3
        # X beats C, Y beats A, Z beats B
        if ((options[0] == 'A' and options[1] == 'Y') or
                (options[0] == 'B' and options[1] == 'Z') or
                (options[0] == 'C' and options[1] == 'X')):
            totalPoints += 6
        # Check if shape is the same for draw
        elif ((options[0] == 'A' and options[1] == 'X') or
              (options[0] == 'B' and options[1] == 'Y') or
              (options[0] == 'C' and options[1] == 'Z')):
            totalPoints += 3

    return totalPoints


def rockPaperScissorsPart2(data):
    # create total points
    # A is Rock it beats Z (Scissors) is beaten by Y (Paper)
    # B is Paper it beats X (Rock) is beaten by Z (Scissors)
    # C is Scissors it beats Y (Paper) is beaten by X (Rock)
    totalPoints = 0

    for options in data:
        chosenShape = ''
        # outcome
        if options[1] == 'X':
            # X means lose
            if options[0] == 'A':
                chosenShape = 'Z'
            elif options[0] == 'B':
                chosenShape = 'X'
            elif options[0] == 'C':
                chosenShape = 'Y'
        elif options[1] == 'Y':
            totalPoints += 3
            # Y means draw
            chosenShape = options[0]
        elif options[1] == 'Z':
            totalPoints += 6
            # Z means win
            if options[0] == 'A':
                chosenShape = 'Y'
            elif options[0] == 'B':
                chosenShape = 'Z'
            elif options[0] == 'C':
                chosenShape = 'X'
        if chosenShape == 'X' or chosenShape == 'A':
            totalPoints += 1
        if chosenShape == 'Y' or chosenShape == 'B':
            totalPoints += 2
        if chosenShape == 'Z' or chosenShape == 'C':
            totalPoints += 3

    return totalPoints


def main():
    # Rock Paper Scissors
    # A and X is Rock worth 1
    # B and Y is Paper worth 2
    # C and Z is Scissors worth 3

    # Game Outcomes
    # 0 Points for Lose
    # 3 Points for Draw
    # 6 Points for Win

    # Total Score = Shape + Outcome

    data = readFile('2/input.txt')

    print(rockPaperScissorsPart1(data))  # print answer

    # NOOOO
    # Part 2, game outcomes are the same but
    # X means lose
    # Y means draw
    # Z means win

    print(rockPaperScissorsPart2(data))


main()
