import easygui
import time

AOCDAY = "06"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    times = lines[0].split(': ')[1].strip().split(' ')
    times_updated = [int(x.strip()) for x in times if x != '']

    distances = lines[1].split(': ')[1].strip().split(' ')
    distances_updated = [int(x.strip()) for x in distances if x != '']

    num_races_won = []
    for index, time in enumerate(times_updated):
        count = 0
        print("This is column ", index)
        for i in range(time):
            travelled = i * (time - i)
            if travelled > distances_updated[index]:
                count += 1
        num_races_won.append(count)
    
    result = 1
    for races_won in num_races_won:
        result *= races_won

    print(result)
        

            

        

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







