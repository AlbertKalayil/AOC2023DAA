import easygui
import time

AOCDAY = "10"

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

    def cross(self,other):
        return self.x * other.y - self.y * other.x


def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    
    dirs = [Coordinate(0,-1), Coordinate(1, 0), Coordinate(0, 1), Coordinate(-1,0)]
    symbols = {
        '|' : [0,-1,2,-1],
        '-' : [-1,1,-1,3],
        'L' : [-1,-1,1,0],
        'F' : [1,-1,-1,2],
        '7' : [3,2,-1,-1],
        'J' : [-1,0,3,-1],
        'S' : [0,1,2,3] 
    }

    

    for y, line in enumerate(lines):
        if "S" in line:
            current = Coordinate(line.find("S"), y)
    dir = 0
    steps = 0
    look = current+dirs[dir]
    # print(look)
    while symbols[look.char_at(lines)][dir] == -1:
        dir+=1
        look = current+dirs[dir] 

 
    while current.char_at(lines)!='S' or steps == 0:

        current = current+dirs[dir]
        dir = symbols[current.char_at(lines)][dir]
        steps+=1 


    print(steps)
    return(f"The mid point is {steps//2} steps away")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
        
    dirs = [Coordinate(0,-1), Coordinate(1, 0), Coordinate(0, 1), Coordinate(-1,0)]
    symbols = {
        '|' : [0,-1,2,-1],
        '-' : [-1,1,-1,3],
        'L' : [-1,-1,1,0],
        'F' : [1,-1,-1,2],
        '7' : [3,2,-1,-1],
        'J' : [-1,0,3,-1],
        'S' : [0,1,2,3] 
    }

    

    for y, line in enumerate(lines):
        if "S" in line:
            current = Coordinate(line.find("S"), y)
    dir = 0
    steps = 0
    look = current+dirs[dir]
    # print(look)
    while symbols[look.char_at(lines)][dir] == -1:
        dir+=1
        look = current+dirs[dir] 

    area = 0
    corners = []

    while current.char_at(lines)!='S' or steps == 0:
        if current.char_at(lines) in "JFL7S":
            corners.append(current)
        current = current+dirs[dir]
        dir = symbols[current.char_at(lines)][dir]
        steps+=1 

    for i in range(len(corners)):
        area += corners[i].cross(corners[(i+1)%len(corners)])


    
    return(f"The inside area is {abs(area//2)-steps//2 +1} ")

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







