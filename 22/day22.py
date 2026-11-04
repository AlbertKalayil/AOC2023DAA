import easygui
import time
import heapq

AOCDAY = "22"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines


class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return Coordinate(self.x * other, self.y * other, self.z * other)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __lt__(self, other):
        if self.z < other.z:
            return True
        elif self.z > other.z:
            return False
        elif self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        return self.y < other.y

DOWN = Coordinate(0, 0, -1)

class Brick:
    def __init__(self, a, b):
        if a < b:
            self.a = a
            self.b = b
        else:
            self.a = b
            self.b = a

    def dropped(self):
        return Brick(self.a + DOWN, self.b + DOWN)

    def __repr__(self):
        return f"{self.a}-{self.b}"
    def __lt__(self,other):
        return self.a < other.a

    def overlaps(self,other):
        if not ((other.a.x <= self.a.x and self.a.x <= other.b.x) or (self.a.x <= other.a.x and other.a.x <= self.b.x)):
            return False
        if not ((other.a.y <= self.a.y and self.a.y <= other.b.y) or (self.a.y <= other.a.y and other.a.y <= self.b.y)):
            return False
        return True




def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    blocks = []
    for line in lines: 
        x1,y1,z1 = line.split('~')[0].split(',')
        x2,y2,z2 = line.split('~')[1].split(',')
        blocks.append(Brick(Coordinate(int(x1),int(y1),int(z1)),Coordinate(int(x2),int(y2),int(z2))))
    blocks.sort()
    supporting = [[] for _ in range(len(blocks))]
    supported = [[] for _ in range(len(blocks))]

    for i in range(len(blocks)):
    # i in range(len()):    
        block = blocks[i]
        done = False
        overlaps = []
        for j in range(i):
            if blocks[i].overlaps(blocks[j]):
                overlaps.append(j)
        maxz = 0
        restingOn = []
        for under in overlaps:
            if blocks[under].b.z == maxz:
                restingOn.append(under)
            elif blocks[under].b.z > maxz:
                maxz = blocks[under].b.z
                restingOn = [under]
        height = block.b.z - block.a.z
        block.a.z = maxz + 1
        block.b.z = maxz + 1 + height
        supported[i] = restingOn
        for num in restingOn:
            supporting[num].append(i)

    result = 0
    only = [False]*len(blocks)

    for group in supported: 
        if len(group) == 1:
            only[group[0]]=True
    for i in only:
        if not i:
            result +=1
    return(f"We can disintegrate {result} blocks")


def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    blocks = []
    for line in lines: 
        x1,y1,z1 = line.split('~')[0].split(',')
        x2,y2,z2 = line.split('~')[1].split(',')
        blocks.append(Brick(Coordinate(int(x1),int(y1),int(z1)),Coordinate(int(x2),int(y2),int(z2))))
    blocks.sort()
    supporting = [[] for _ in range(len(blocks))]
    supported = [[] for _ in range(len(blocks))]

    for i in range(len(blocks)):
    # i in range(len()):    
        block = blocks[i]
        done = False
        overlaps = []
        for j in range(i):
            if blocks[i].overlaps(blocks[j]):
                overlaps.append(j)
        maxz = 0
        restingOn = []
        for under in overlaps:
            if blocks[under].b.z == maxz:
                restingOn.append(under)
            elif blocks[under].b.z > maxz:
                maxz = blocks[under].b.z
                restingOn = [under]
        height = block.b.z - block.a.z
        block.a.z = maxz + 1
        block.b.z = maxz + 1 + height
        supported[i] = restingOn
        for num in restingOn:
            supporting[num].append(i)

    result = 0
    i = 0
    for i in range(len(blocks)):
        if len(supporting[i]) == 0:
            pass
        q = []
        fallen = set([i])
        for num in supporting[i]:
            heapq.heappush(q, num)
        while q:
            curr = heapq.heappop(q)
            if curr in fallen:
                continue
            falling = True
            for under in supported[curr]:
                if under not in fallen:
                    falling = False
                    break
            if falling:
                fallen.add(curr)
                result += 1
                for num in supporting[curr]:
                    heapq.heappush(q, num)

    
    return(f"We can disintegrate {result} blocks")

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







