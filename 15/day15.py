import easygui
import time

AOCDAY = "15"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def hash(s):
    curr = 0
    for char in s:
        curr = (curr + ord(char)) * 17 % 256
    return curr


def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    #print(hash("rn=1"))
    result = 0
    for s in lines[0].split(','):
        result += hash(s)
    
    return(f"The total hash value is {result}")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    boxes = [[] for _ in range(256)]
    for s in lines[0].split(','):
        if "=" in s:
            label, focal = s.split('=')
            box = hash(label)
            found = False
            for i, lens in enumerate(boxes[box]):
                if lens[0] == label:
                    boxes[box][i] = (label, focal)
                    found = True
                    break
            if not found:
                boxes[box].append((label, focal))
        else:
            label = s[:-1]
            box = hash(label)
            for i, lens in enumerate(boxes[box]):
                if lens[0] == label:
                    boxes[box].pop(i)
                    break

    result = 0
    
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            result += (i+1) * (j+1) * int(lens[1])

    return(f"Total focal length of the lens array is {result}")

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