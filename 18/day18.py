import easygui
import time

AOCDAY = "18"

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

    def __mul__(self, other):
        return Coordinate(self.x * other, self.y * other)

    def cross(self,other):
        return self.x * other.y - self.y * other.x

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    current = Coordinate(0,0)
    corners = []
    dirs = {"U": Coordinate(0,-1), 
            "R": Coordinate(1, 0), 
            "D": Coordinate(0, 1), 
            "L": Coordinate(-1,0)
            }

    for line in lines:
        dir, steps, colour = line.split(" ")
        current = current + dirs[dir] * (int(steps))
        corners.append(current)

    area = 0


    for i in range(len(corners)):
        area += corners[i].cross(corners[(i+1)%len(corners)])
        print((corners[i], corners[i+1]))
        print(area)
    return(f"The total area of the lagoon is {area}")

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
