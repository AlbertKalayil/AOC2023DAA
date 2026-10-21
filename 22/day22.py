import easygui
import time

AOCDAY = "22"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines


class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return Coordinate(self.x * other, self.y * other, self.z * other)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __lt__(self, other):
        if self.z < other.z:
            return True
        elif self.z < other.z:
            return False
        elif self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        return self.y < other.y

DOWN = Coordinate(0, 0, -1)

class Brick:
    def __init__(self, a, b):
        if a < b:
            self.a = a
            self.b = b
        else:
            self.a = b
            self.b = a

    def dropped(self):
        return Brick(self.a + DOWN, self.b + DOWN)


def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string

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







