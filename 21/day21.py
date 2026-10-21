import easygui
import time
import heapq

AOCDAY = "21"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

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

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    dirs = (Coordinate(0,-1), Coordinate(1, 0), Coordinate(0, 1), Coordinate(-1,0))
    coord = Coordinate(0, 0)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            c = Coordinate(x, y)
            if c.char_at(lines) == "S":
                coord = c 
    steps = 6
    if len(lines) > 20:
        steps = 64
    q = []
    visited = set()
    distances = {}

    q.append((0, coord))

    while q:
        cost, current = q.pop(0)
        distances[current] = cost
        if current in visited:
            continue
        visited.add(current)
        for dir in dirs:
            next = current + dir
            if next not in visited and next.validate(lines) and next.char_at(lines) != '#' and cost < steps:
                q.append((cost + 1, next))
    result = 0
    for value in distances.values():
        if value % 2 == 0:
            result += 1


    return(f"By taking {steps} steps, the elf can reach {result} garden plots")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    dirs = (Coordinate(0,-1), Coordinate(1, 0), Coordinate(0, 1), Coordinate(-1,0))
    coord = Coordinate(0, 0)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            c = Coordinate(x, y)
            if c.char_at(lines) == "S":
                coord = c

    if len(lines) <= 20:
        return "I can't do this"
    q = []
    visited = set()
    distances = {}

    q.append((0, coord))

    while q:
        cost, current = q.pop(0)
        distances[current] = cost
        if current in visited:
            continue
        visited.add(current)
        for dir in dirs:
            next = current + dir
            if next not in visited and next.validate(lines) and next.char_at(lines) != '#':
                q.append((cost + 1, next))
    evens = 0
    odds = 0
    evencorners = 0
    oddcorners = 0
    for value in distances.values():
        if value % 2 == 0:
            evens += 1
            if value > 65:
                evencorners += 1
        else:
            odds += 1
            if value > 65:
                oddcorners += 1

    n = 202300

    result = ((n+1)*(n+1)) * odds + (n*n) * evens - (n+1) * oddcorners + n * evencorners
    return(f"By taking 26501365 steps, the elf can reach {result} garden plots")

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