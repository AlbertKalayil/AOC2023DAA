import easygui
import time

AOCDAY = "23"

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Coordinate(self.x * other, self.y * other)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def char_at(self, map):
        return(map[self.y][self.x])

    def validate(self, map):
        return self.x >= 0 and self.y >= 0 and self.x < len(map[0]) and self.y < len(map)

    def __lt__(self, other):
        return 1
    
    def __hash__(self):
        return self.x * 1000 + self.y

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    startx = -1
    targetx = -1
    dirs = (Coordinate(0,-1), Coordinate(1, 0), Coordinate(0, 1), Coordinate(-1,0))
    for i in range(len(lines[0])):
        if lines[0][i] == '.':
            startx = i
        if lines[-1][i] == '.':
            targetx = i

    start = Coordinate(startx, 0)
    target = Coordinate(targetx, len(lines) - 1)

    visited = set()
    stack = [start]

    while stack:
        curr = stack.pop(0)
        for dir in dirs:
            next = curr + dir
            

    return(f"Result of Part 1.")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string

    return(f"Result of Part 2.")

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