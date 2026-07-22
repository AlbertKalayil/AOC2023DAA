import easygui
import time
import math

AOCDAY = "08"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    path = lines[0]

    graph = {}
    for line in lines[2:]:
        graph[line[0:3]] = (line[7:10], line[12:15])

    if 'AAA' not in graph.keys():
        return("Input not valid for part 1 :(")

    steps = 0
    current = 'AAA'

    while current != 'ZZZ':
        step = path[steps % len(path)]

        if step == 'R':
            current = graph[current][1]
        else:
            current = graph[current][0]

        steps += 1


    return(f"We took this many steps: {steps}")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    path = lines[0]
    
    graph = {}
    for line in lines[2:]:
        graph[line[0:3]] = (line[7:10], line[12:15])

    current = []
    for node in graph.keys():
        if node[2] == 'A':
            current.append(node)

    first = [0] * len(current)
    done = False
    steps = 0

    while not done:
        step = path[steps % len(path)]
        done = True
        for i, node in enumerate(current):
            if step == 'R':
                current[i] = graph[node][1]
            else:
                current[i] = graph[node][0]

            if current[i][2] != 'Z' and first[i] == 0:
                done = False
            else:
                if first[i] == 0:
                    first[i] = steps

        steps += 1

    mods = []
    for f in first:
        mods.append(f+1)
    lcm = math.lcm(*mods)

    return(f"We took this many steps: {lcm}")

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