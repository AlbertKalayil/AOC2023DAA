import easygui
import time

AOCDAY = "19"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    rules = {}
    parts = []
    inrules = True
    for line in lines:
        if line == "":
            inrules = False
        elif inrules: 
            rulename = line.split("{")[0]
            ruletext = line.split("{")[1][:-1]
            checks = []
            for check in ruletext.split(",")[:-1]:
                par = check[0]
                operator = check[1]
                value = int(check.split(":")[0][2:])
                target = check.split(":")[1]
                checks.append((par,operator,value,target))
            checks.append(ruletext.split(",")[-1])
            rules[rulename]=checks
        else:
            part = {}
            for par in line[1:-1].split(","):
                p, val = par.split("=")
                part[p]=int(val)
            
            parts.append(part)
    result = 0 
    for part in parts:
        rulesseen = ["in"]
        rulename = "in"
        while rulename != "A" and rulename != "R":
            branched = False
            for check in rules[rulename][:-1]:
                id, op, value, target = check
                if op == "<":
                    if part[id]<value:
                        rulename = target
                        branched = True
                        break
                else: 
                    if part[id]> value:
                        rulename = target
                        branched = True
                        break
            if not branched:
                rulename = rules[rulename][-1]
            rulesseen.append(rulename)
        print(part)
        print(rulesseen)
        if rulename == "A":
            result += sum(part.values())
    
    return (f"Total value of accepted parts is: {result}")

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







