import easygui
import time
import math

AOCDAY = "20"

LOW = 0
HIGH = 1
class Broadcaster:
    def __init__(self,name,outputs):
        self.outputs = outputs
        self.name = name
    def process(self,message):
        result = []
        for output in self.outputs:
            result.append((self.name,LOW,output))
        return result

class Flipflop:
    def __init__(self,name,outputs):
        self.outputs = outputs
        self.name = name
        self.state = LOW
    def process(self,message):
        result = []
        if message[1] == LOW:
            if self.state == HIGH:
                self.state = LOW
            else:
                self.state = HIGH
            for output in self.outputs:
                result.append((self.name,self.state,output))
        return result
class Conjunction:
    def __init__(self,name,outputs):
        self.outputs = outputs
        self.name = name
        self.inputs =  {}
    def process(self,message):
        result = []
        self.inputs[message[0]] = message[1]
        signal = LOW
        for input in self.inputs.values():
            if input == LOW:
                signal = HIGH
        for output in self.outputs:
            result.append((self.name,signal,output))  
        return result

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    nodes = {}
    for line in lines:
        name, outputstring = line.split(' -> ')
        outputs = outputstring.split(', ')
        if name[0] == '%':
            name = name[1:]
            nodes[name] = Flipflop(name,outputs)
        elif name[0] == '&':
            name= name[1:]
            nodes[name]= Conjunction(name, outputs)
        else:
            nodes[name] = Broadcaster(name, outputs)
    for node in nodes.values():
        outputs = node.outputs
        for output in outputs:

            if output in nodes and type(nodes[output]).__name__ == 'Conjunction':
                nodes[output].inputs[node.name]= LOW
    
    lowcount = 0
    highcount = 0

    
    for _ in range(1000):

        q = [('button',LOW, 'broadcaster')]
        while q : 
            message = q.pop(0)
            if message[1]== LOW:
                lowcount += 1
            else:
                highcount += 1
            if message[2] in nodes:

                q.extend(nodes[message[2]].process(message))


    return(f"The product is {lowcount*highcount}")

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a 
    nodes = {}
    for line in lines:
        name, outputstring = line.split(' -> ')
        outputs = outputstring.split(', ')
        if name[0] == '%':
            name = name[1:]
            nodes[name] = Flipflop(name,outputs)
        elif name[0] == '&':
            name= name[1:]
            nodes[name]= Conjunction(name, outputs)
        else:
            nodes[name] = Broadcaster(name, outputs)
    for node in nodes.values():
        outputs = node.outputs
        for output in outputs:

            if output in nodes and type(nodes[output]).__name__ == 'Conjunction':
                nodes[output].inputs[node.name]= LOW
    rx_parent = next(node.name for node in nodes.values() if 'rx' in node.outputs)
    
    pushes = 0
    cycles = {}
    while True:


        q = [('button',LOW, 'broadcaster')]
        pushes += 1
        while q : 
            message = q.pop(0)
            if (
                message[2] == rx_parent
                and message[1] == HIGH
                and message[0] not in cycles
            ):
                cycles[message[0]] = pushes

            if len(cycles) == len(nodes[rx_parent].inputs):
                return f'Number of button presses {math.lcm(*cycles.values())}'
           
            if message[2] in nodes:

                q.extend(nodes[message[2]].process(message))


    return(f"This is unreachable")
   

  

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







