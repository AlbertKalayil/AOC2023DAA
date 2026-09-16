import easygui
import time

AOCDAY = "16"

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

    def char_at(self, map):
        return(map[self.y][self.x])

    def validate(self, map):
        return self.x >= 0 and self.y >= 0 and self.x < len(map[0]) and self.y < len(map)

def bounce(c, dir):
    if c == '.':
        return [dir]
    elif c in '/':
        if dir % 2 == 0:
            return [(dir + 1) % 4]
        else:
            return [(dir - 1) % 4]
    elif c == '\\':
        if dir % 2 == 0:
            return [(dir - 1) % 4]
        else:
            return [(dir + 1) % 4]
    elif c == '-':
        if dir % 2 == 0:
            return [1, 3]
        else:
            return [dir]
    elif c == '|':
        if dir % 2 == 0:
            return [dir]
        else:
            return [0,2]
    

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    dirs = (Coordinate(0,-1), Coordinate(1, 0), Coordinate(0, 1), Coordinate(-1,0))
    states = set()
    energized = set()
    q = [(0,0,1)]

    while len(q) > 0:
        curr = q.pop(0)
        x, y, dir = curr
        if curr in states:
            continue
        states.add(curr)
        energized.add((x, y))
        coord = Coordinate(x, y)
        for d in bounce(coord.char_at(lines), dir):
            next = coord + dirs[d]
            if next.validate(lines):
                q.append((next.x, next.y, d))

    return(f"Total number of energzed tiles is {len(energized)}")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    dirs = (Coordinate(0,-1), Coordinate(1, 0), Coordinate(0, 1), Coordinate(-1,0))
    max_energized = 0
    width, height = len(lines[0]), len(lines)
    q2 = []

    for i in range(width):
        q2.append((i,0,2))
        q2.append((i, height - 1, 0))

    for j in range(height):
        q2.append((0, j, 1))
        q2.append((width - 1, j, 3))

    for start in q2:
        q = [start]
        states = set()
        energized = set()

        while len(q) > 0:
            curr = q.pop(0)
            x, y, dir = curr
            if curr in states:
                continue
            states.add(curr)
            energized.add((x, y))
            coord = Coordinate(x, y)
            for d in bounce(coord.char_at(lines), dir):
                next = coord + dirs[d]
                if next.validate(lines):
                    q.append((next.x, next.y, d))
        max_energized = max(max_energized, len(energized))

    return(f"The maximum number of energized tiles is {max_energized}")

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