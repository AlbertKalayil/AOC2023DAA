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
       
        if rulename == "A":
            result += sum(part.values())
    
    return (f"Total value of accepted parts is: {result}")

def valid_range(current):
    for c in 'xmas':
        a,b = current[c]
        if a>b:
            return False
    return True
        

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    rules = {}
    ranges = [{'x':(1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000), 'rule': 'in'}]
    result = 0
    
    for line in lines:
        if line == "":
            break
        else : 
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
    while len(ranges)>0:

        current = ranges.pop()
    
        if current['rule']== 'A':
            result += (current['x'][1]- current['x'][0]+1)* (current['a'][1]- current['a'][0]+1)* (current['m'][1]- current['m'][0]+1)* (current['s'][1]- current['s'][0]+1)
            continue
        elif current['rule']=='R':
            continue

        rule = rules[current["rule"]]
        for check in rule[:-1]:
            new_range = {'x':current['x'], 
                        'm': current['m'], 
                        'a': current['a'], 
                        's': current['s'],
                        'rule': check[3] } 
            if check[1] == '>':
                new_range[check[0]]=(max(check[2]+1,current[check[0]][0]), current[check[0]][1])
                current[check[0]]=(current[check[0]][0], min(check[2], current[check[0]][1]))
            else: 
                new_range[check[0]]= (current[check[0]][0], min(check[2]-1, current[check[0]][1]))
                current[check[0]]= (max(check[2],current[check[0]][0]), current[check[0]][1])
            if valid_range(new_range):
                ranges.append(new_range)
        current['rule']=rule[-1]
        if valid_range(new_range):
            ranges.append(current)
    

    
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







