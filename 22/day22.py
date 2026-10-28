import easygui
import time

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

    def intersects(self,other):
        if not ((other.a.x <= self.a.x and self.a.x <= other.b.x) or (self.a.x <= other.a.x and other.a.x <= self.b.x)\
            or (self.a.x == self.b.x and self.b.x == other.a.x and other.a.x == other.b.x)):
            return False
        if not ((other.a.y <= self.a.y and self.a.y <= other.b.y) or (self.a.y <= other.a.y and other.a.y <= self.b.y)\
            or (self.a.y == self.b.y and self.b.y == other.a.y and other.a.y == other.b.y)):
            return False
        if not ((other.a.z <= self.a.z and self.a.z <= other.b.z) or (self.a.z <= other.a.z and other.a.z <= self.b.z)\
            or (self.a.z == self.b.z and self.b.z == other.a.z and other.a.z == other.b.z)):
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
        while not done:
            
            if block.a.z == 1:
                done = True
            else:
                block = block.dropped()
                for j in range(i):
                    if block.intersects(blocks[j]):
                        done = True
                        supporting[j].append(i)
                        supported[i].append(j)
                if not done:
                    blocks[i]= block
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
        while not done:
            
            if block.a.z == 1:
                done = True
            else:
                block = block.dropped()
                for j in range(i):
                    if block.intersects(blocks[j]):
                        done = True
                        supporting[j].append(i)
                        supported[i].append(j)
                if not done:
                    blocks[i]= block
    result = 0
    only = [False]*len(blocks)

    for group in supported: 
        if len(group) == 1:
            only[group[0]]=True
    for i in range(len(only)):
        if  only[i]:
            result += len(blocks)-i-1
    print (only)
    return(f"total {result} blocks will fall")
    
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







