import easygui
import time

AOCDAY = "09"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    result = 0
    for line in lines:
        top_row = [int(x) for x in line.split()]
        # print(top_row)
        rows = [top_row]
        done = False

        while not done:
            done = True
            next_row = []
            for i in range(len(rows[-1])-1):
                difference = rows[-1][i+1] - rows[-1][i]
                if difference != 0:
                    done = False
                next_row.append(difference)
            rows.append(next_row)

        new_value = 0

        for j in range(2, len(rows)+1):
            new_value = rows[-j][-1] + new_value


        result += new_value


    return(f"The total ecological score is {result}")

def part2(lines):
    result = 0
    for line in lines:
        top_row = [int(x) for x in line.split()]
        rows = [top_row]
        done = False

        while not done:
            done = True
            next_row = []
            for i in range(len(rows[-1])-1):
                difference = rows[-1][i+1] - rows[-1][i]
                if difference != 0:
                    done = False
                next_row.append(difference)
            rows.append(next_row)

        new_value = 0

        for j in range(2, len(rows)+1):
            new_value = rows[-j][0] - new_value


        result += new_value

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







