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

dirs = (Coordinate(0,-1), Coordinate(1, 0), Coordinate(0, 1), Coordinate(-1,0))

def dfs_max(map, curr, target, visited):
    while True:
        options = []
        slopes = {'^': 0, '>': 1, 'v': 2, '<':3}
        if curr.char_at(map) in "^v><":
            next = curr + dirs[slopes[curr.char_at(map)]]
            if next not in visited:
                visited.add(next)
                curr = next
            else:
                return 0
        else:
            for dir in dirs:
                next = curr + dir
                if next == target:
                    return len(visited)
                if next.validate(map) and next.char_at(map) != "#" and next not in visited:
                    options.append(next)
            if len(options) == 0:
                return 0
            elif len(options) == 1:
                visited.add(options[0])
                curr = options[0]
            else:
                maxsteps = 0
                for option in options:
                    newvisited = set(visited)
                    newvisited.add(option)
                    maxsteps = max(maxsteps, dfs_max(map, option, target, newvisited))
                return maxsteps

def find_neighbour(map, curr, visited, intersections):
    while True:
        options = []
        for dir in dirs:
            next = curr + dir
            if next in intersections and next not in visited:
                return next, len(visited)
            if next.validate(map) and next.char_at(map) != "#" and next not in visited:
                options.append(next)
        if len(options) == 0:
            return None, None
        elif len(options) == 1:
            visited.add(options[0])
            curr = options[0]

def dfs_max2(curr, target, edges, visited, steps):
    maxsteps = 0
    for next in edges[curr].keys():
        cost = steps + edges[curr][next]
        if next == target:
            return cost
        else:
            if next not in visited:
                visited.add(next)
                maxsteps = max(maxsteps, dfs_max2(next, target, edges, visited, cost))
                visited.remove(next)
    return maxsteps

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
    for i in range(len(lines[0])):
        if lines[0][i] == '.':
            startx = i
        if lines[-1][i] == '.':
            targetx = i

    start = Coordinate(startx, 0)
    target = Coordinate(targetx, len(lines) - 1)

    visited = set([start])
     
    return(f"The longest path for a walk is {dfs_max(lines, start, target, visited)} steps.")

def part2(lines):
    startx = -1
    targetx = -1
    for i in range(len(lines[0])):
        if lines[0][i] == '.':
            startx = i
        if lines[-1][i] == '.':
            targetx = i

    start = Coordinate(startx, 0)
    target = Coordinate(targetx, len(lines) - 1)

    intersections = set([start, target])
    xmax = len(lines[0]) - 1
    ymax = len(lines) - 1
    for x in range(1, xmax):
        for y in range(1, ymax):
            curr = Coordinate(x, y)
            if curr.char_at(lines) == "#":
                continue
            count = 0
            for dir in dirs:
                next = curr + dir
                if next.validate(lines) and next.char_at(lines) != "#":
                    count += 1
            if count > 2:
                intersections.add(curr)

    edges = {}
    for intersection in intersections:
        edges[intersection] = {}
        for dir in dirs:
            next = intersection + dir
            if next.validate(lines) and next.char_at(lines) != '#':
                other, cost = find_neighbour(lines, next, set([intersection, next]), intersections)
                if other is not None:
                    edges[intersection][other] = cost
    return(f"The longest path for a walk is {dfs_max2(start, target, edges, set([start]), 0)} steps.")

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