import easygui
import time

AOCDAY = "01"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    total = 0

    for line in lines:
        l = 0
        r = len(line) - 1

        while not line[l].isnumeric():
            l += 1

        while not line[r].isnumeric():
            r -= 1
            
        total += int(line[l] + line[r])

    return(f"The sum of the calibration values is {total}.")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    total = 0

    digits = {'one': 1, 
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight':8,
            'nine':9,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
            }

    for line in lines:
        l = 0
        r = len(line) - 1

        left_digit = 0
        right_digit = 0

        while left_digit == 0:
            for i in range(1,6):
                substring = line[l:l+i]
                
                if substring in digits.keys():
                    left_digit = digits[substring]
                    break
            l += 1

        
        while right_digit == 0:
            for i in range(1,6):
                substring = line[r:r+i]
                
                if substring in digits.keys():
                    right_digit = digits[substring]
                    break
            r -= 1

        total += left_digit*10 + right_digit

    return(f"The sum of the calibration values is {total}.")

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







