import easygui
import time

AOCDAY = "11"

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def char_at(self, map):
        return(map[self.y][self.x])

    def manhattan(self,other):
        return abs(other.x - self.x) + abs(other.y - self.y)

    def __mul__(self, other):
        return Coordinate(self.x * other, self.y * other)

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    emptyRows = []

    for line in lines:
        if '#' not in line:
            emptyRows.append(True)
        else:
            emptyRows.append(False)
    emptyCols = []
    for x in range(len(lines[0])):
        emptyCols.append(True)
        for y in range(len(lines)):
            if Coordinate(x,y).char_at(lines) == '#':
                emptyCols[-1] = False
                break

    galaxies = []
    yoff = 0
    for y in range(len(lines)):
        xoff = 0
        if emptyRows[y]:
            yoff += 1
            continue
        for x in range(len(lines[0])):
            if emptyCols[x]:
                xoff += 1
                continue
            coord = Coordinate(x, y)
            if coord.char_at(lines) == '#':
                galaxies.append(coord + Coordinate(xoff, yoff))

    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            result += galaxies[i].manhattan(galaxies[j])


            

    return(f"The total distances of the shortest paths is {result}")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    emptyRows = []
    
    for line in lines:
        if '#' not in line:
            emptyRows.append(True)
        else:
            emptyRows.append(False)
    emptyCols = []
    for x in range(len(lines[0])):
        emptyCols.append(True)
        for y in range(len(lines)):
            if Coordinate(x,y).char_at(lines) == '#':
                emptyCols[-1] = False
                break

    galaxies = []
    yoff = 0
    for y in range(len(lines)):
        xoff = 0
        if emptyRows[y]:
            yoff += 1
            continue
        for x in range(len(lines[0])):
            if emptyCols[x]:
                xoff += 1
                continue
            coord = Coordinate(x, y)
            if coord.char_at(lines) == '#':
                galaxies.append(coord + Coordinate(xoff, yoff) * 999999)

    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            result += galaxies[i].manhattan(galaxies[j])

    return(f"The total distances of the expanded shortest paths is {result}")

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
