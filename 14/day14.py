import easygui
import time

AOCDAY = "14"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def tiltnorth(map):
    height = len(map)
    width = len(map[0])
    for x in range(width):
        p = 0
        for y in range(height):
            c = map[y][x]
            if c == 'O':
                map[y][x] = '.'
                map[p][x] = 'O'
                p += 1 
            elif c == '#':
                p = y + 1

def tiltsouth(map):
    height = len(map)
    width = len(map[0])
    for x in range(width):
        p = height - 1
        for y in range(height-1, -1, -1):
            c = map[y][x]
            if c == 'O':
                map[y][x] = '.'
                map[p][x] = 'O'
                p -= 1 
            elif c == '#':
                p = y - 1

def tiltwest(map):
    height = len(map)
    width = len(map[0])
    for y in range(height):
        p = 0
        for x in range(width):
            c = map[y][x]
            if c == 'O':
                map[y][x] = '.'
                map[y][p] = 'O'
                p += 1 
            elif c == '#':
                p = x + 1

def tilteast(map):
    height = len(map)
    width = len(map[0])
    for y in range(height):
        p = width - 1
        for x in range(width-1, -1, -1):
            c = map[y][x]
            if c == 'O':
                map[y][x] = '.'
                map[y][p] = 'O'
                p -= 1 
            elif c == '#':
                p = x - 1

def cycle(map):
    tiltnorth(map)
    tiltwest(map)
    tiltsouth(map)
    tilteast(map)

def printMap(map):
    for line in map:
        print("".join(line))

def scoreMap(map):
    height = len(map)
    width = len(map[0])
    score = 0

    for y in range(height):
        for x in range(width):
            c = map[y][x]
            if c == 'O':
                score += (height - y)
    return score

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    map = []
    for line in lines:
        map.append(list(line))
    tiltnorth(map)
    score = scoreMap(map)
    return(f"The total lead of this dish is {score}")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    map = []
    states = {}

    for line in lines:
        map.append(list(line))
    i = 0
    while True:
        cycle(map)
        i += 1
        h = "".join(item for line in map for item in line)
        if h in states.keys():
            start = states[h]
            cycleLen = i - start
            offset = (1000000000 - start) % cycleLen
            for _ in range(offset):
                cycle(map)
            break
        else:
            states[h] = i

    #printMap(map)
    return(f"The load after all the cycles is {scoreMap(map)}")

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







