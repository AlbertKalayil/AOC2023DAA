import easygui
import time
import functools

AOCDAY = "12"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

@functools.cache
def count_valid(pipes, groups, i,j):
    if i >= len(pipes):
        if j >= len(groups):
            return 1
        else:
            return 0
    if j >= len(groups):
        if "#" in pipes[i:]: 
            return 0
        else:
            return 1
     
    total = 0
    if pipes[i] == "." or pipes[i]=="?":
        total += count_valid(pipes,groups,i+1,j)
    if pipes[i] == "#" or pipes[i]== "?":
        target = groups[j]
        valid = True
        for k in range(target):
            if i+k >= len(pipes) or pipes[i+k] == ".":
                valid = False
                break
    
        if i+target < len(pipes) and pipes[i+ target] == "#":
            valid = False
        if valid:
            total += count_valid(pipes,groups,i+target+1, j+1)
    
    return total
                            

    


def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    result = 0
    for line in lines:

        pipes = line.split()[0]
        groups = [int(x) for x in line.split()[1].split(",")]
        result+= count_valid(pipes,tuple(groups),0,0)

    return(f"Total pipe permutations is {result}")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    result = 0
    for line in lines:

        pipes = "?".join([line.split()[0]] * 5)
        groups = [int(x) for x in line.split()[1].split(",")]*5
        result+= count_valid(pipes,tuple(groups),0,0)

    return(f"Total pipe permutations is {result}")


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