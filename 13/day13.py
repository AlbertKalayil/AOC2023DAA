import easygui
import time

AOCDAY = "13"



def horizontal(block, diff=0):
    width = len(block[0])
    height = len(block)
    ri_list = []

    for ri in range(1, width):
        count = 0
        for y in range(height):
            for distance in range(1, min(ri, width - ri) + 1):
                if block[y][ri - distance] != block[y][ri + distance - 1]:
                    count += 1
                    if count > diff:
                        break

            if count > diff:
                break
        if count == diff:
            ri_list.append(ri)

    return ri_list

def vertical(block, diff=0):
    width = len(block[0])
    height = len(block)
    ri_list = []

    for ri in range(1, height):
        count = 0
        for x in range(width):
            for distance in range(1, min(ri, height - ri) + 1):
                if block[ri - distance][x] != block[ri + distance - 1][x]:
                    count +=1
                    if count > diff:
                        break

            if count > diff:
                break
        if count == diff:
            ri_list.append(ri)

    return ri_list




def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    blocks = []
    block = []
    for line in lines:
        if line == "":
            blocks.append(block)
            block = []
        else:
            block.append(line)

    blocks.append(block)
    result = 0
    for block in blocks:
        for ri in horizontal(block):
            result += ri
        for ri in vertical(block):
            result += ri * 100


    return(f"Result of Part 1: {result}")

def part2(lines):
    blocks = []
    block = []
    for line in lines:
        if line == "":
            blocks.append(block)
            block = []
        else:
            block.append(line)

    blocks.append(block)
    result = 0
    for block in blocks:
        for ri in horizontal(block, diff=1):
            result += ri
        for ri in vertical(block, diff=1):
            result += ri * 100


    return(f"Result of Part 2: {result}")


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







