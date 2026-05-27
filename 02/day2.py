import easygui
import time

AOCDAY = "02"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    result = 0
    limits = {'red': 12,
                'blue': 14,
                'green': 13}
    for line in lines:
        gameName, cubes = line.split(': ')
        gameNumber = int(gameName.split(' ')[1])
        myDict = {'red': 0,
                  'blue': 0,
                  'green': 0}
        draws = cubes.split('; ')
        for draw in draws:
            colours = draw.split(', ')
            for colour in colours:
                countStr, colourName = colour.split(' ')
                count = int(countStr)
                myDict[colourName] = max(count, myDict[colourName])
        valid = True
        for colourName in myDict.keys():
            if myDict[colourName] > limits[colourName]:
                valid = False
        if valid:
            result += gameNumber

    return(f"The sum of valid Game IDs is: {result}")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    result = 0
    for line in lines:
        gameName, cubes = line.split(': ')
        gameNumber = int(gameName.split(' ')[1])
        myDict = {'red': 0,
                  'blue': 0,
                  'green': 0}
        draws = cubes.split('; ')
        for draw in draws:
            colours = draw.split(', ')
            for colour in colours:
                countStr, colourName = colour.split(' ')
                count = int(countStr)
                myDict[colourName] = max(count, myDict[colourName])
        power = 1
        for colourName in myDict.keys():
            power *= myDict[colourName]

        result += power
    return(f"The power of these games is {result}")

def main ():
    # Opens a dialog to select the input file
    # Times and runs both solutions
    # Prints the results
    fileName = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    if fileName == None:
        print("ERROR: No file selected.")
        return
    lines = readFile(fileName)
    p1StartTime = time.perf_counter()
    p1Result = part1(lines)
    p1EndTime = time.perf_counter()
    p2StartTime = time.perf_counter()
    p2Result = part2(lines)
    p2EndTime = time.perf_counter()
    print("Advent of Code 2023 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()







