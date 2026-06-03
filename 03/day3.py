import easygui
import time


AOCDAY = "03"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):

    dirs = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,0), (1,-1),(1,1))

    result = 0
    for ycoord, line in enumerate(lines):
        number = ''
        part= False
        for xcoord, c in enumerate(line):
            if c.isnumeric():
                number += c
                #check for symbol
                for dir in dirs:
                    xtarget = xcoord + dir[0]
                    ytarget = ycoord + dir[1]
                    if xtarget >= 0 and xtarget < len(line) and \
                        ytarget >= 0 and ytarget < len(lines):
                        target = lines[ytarget][xtarget]
                        if not target.isnumeric() and target != ".":
                            part=True

            else:
                if part:
                    result += int(number)
                number = ''
                part = False
        if part:
            result += int(number)
        number = ''
        part = False

    # Code the solution to part 1 here, returning the answer as a string

    return(f"Total of part numbers is {result}")

def part2(lines):

    dirs = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,0), (1,-1),(1,1))
    gearcoords = {}
    result = 0
    for ycoord, line in enumerate(lines):
        number = ''
        gears= []
        for xcoord, c in enumerate(line):
            if c.isnumeric():
                number += c
                #check for symbol
                for dir in dirs:
                    xtarget = xcoord + dir[0]
                    ytarget = ycoord + dir[1]
                    if xtarget >= 0 and xtarget < len(line) and \
                        ytarget >= 0 and ytarget < len(lines):
                        target = lines[ytarget][xtarget]
                        if target == '*' :
                            gearcoord = f"{xtarget},{ytarget}"
                            if not gearcoord in gears:
                                gears.append(gearcoord)

            else:
                if len(gears) > 0:
                    for gear in gears:
                        if gear not in gearcoords.keys():
                            gearcoords[gear]=[int(number)]
                        else:
                            gearcoords[gear].append(int(number))
                number = ''
                gears = []
        if len(gears) > 0:
            for gear in gears:
                if gear not in gearcoords.keys():
                    gearcoords[gear]=[int(number)]
                else:
                    gearcoords[gear].append(int(number))
        number = ''
        gears = []
        
    for gearcoord in gearcoords.values():
        if len(gearcoord) == 2:
           result += gearcoord[0]*gearcoord[1]


    return(f"Total of part numbers is {result}")

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







