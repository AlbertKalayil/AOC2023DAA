import easygui
import time

AOCDAY = "04"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    result = 0

    for line in lines:
        winning_string = line.split(" | ")[0].split(": ")[1]
        winning = []
        for number in winning_string.split(" "):
            if number != "":
                winning.append (int(number))
        ticket_string = line.split(" | ")[1]
        ticket = []
        for number in ticket_string.split(" "):
            if number != "":
                ticket.append (int(number))
        
        match = 0
        for number in ticket:
            if number in winning:
                match = match +1
        
        if match == 0:
            score = 0
        else:
            score = 2**(match-1)

        result = result + score
  
    return(f"Total score of the winning tickets is {result}.")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    cards = [1]*len(lines)

    for i, line in enumerate(lines):
        winning_string = line.split(" | ")[0].split(": ")[1]
        winning = []
        for number in winning_string.split(" "):
            if number != "":
                winning.append (int(number))
        ticket_string = line.split(" | ")[1]
        ticket = []
        for number in ticket_string.split(" "):
            if number != "":
                ticket.append (int(number))
        
        match = 0
        for number in ticket:
            if number in winning:
                match = match +1
        for j in range(1, match +1):
            cards [i+j] += cards[i]
    
    result = 0
    for card in cards:
        result += card

    return(f"You have a total of {result} tickets.")

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







