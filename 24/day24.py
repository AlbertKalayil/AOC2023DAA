import easygui
import time
import re
from fractions import Fraction

AOCDAY = "24"

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

class Hailstone:
    def __init__(self,x,y,z,vx,vy,vz):
        self.p= Coordinate(x,y,z)
        self.v= Coordinate(vx,vy,vz)
    def __repr__(self):
        return f'{self.p} > {self.v} '

    def intersect(self,other):
        det = self.v.x * other.v.y - self.v.y * other.v.x
        if det == 0:
            return (-1,-1)
        t = (other.v.y * (other.p.x - self.p.x) - other.v.x * (other.p.y - self.p.y)) / det
        s = (self.p.x + t * self.v.x - other.p.x) / other.v.x

        if s < 0 or t < 0: 
            return (-1,-1)
        
        return (self.p.x + self.v.x * t, self.p.y + self.v.y * t )  
    

def part1(lines):
    stones = []
    for line in lines:
        nums = [int(a) for a in line.replace(' @ ',', ').split(', ')]
        stones.append( Hailstone(*nums))

    result = 0
    low = 200000000000000
    high = 400000000000000

    if len(lines) < 10:
        low = 7
        high = 27
    



    for i in range(len(stones)-1):
        for j in range(i+1, len(stones)):
            x,y = stones[i].intersect(stones[j])
            if x >= low and x <= high and y >= low and y <= high:
                result +=1


    return f" {result} pairs of hailstones collide inside the given area" 


def part2(lines):

    def cross(a, b):
        return (
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        )
    
    
    def sub(a, b):
        return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
    
    
    def add_equations(matrix, p0, v0, p1, v1):
        """Builds 3 linear rows for: (p1 - p0) x V + (v0 - v1) x P = p1 x v1 - p0 x v0"""
        dp = sub(p1, p0)
        dv = sub(v0, v1)
        rhs = sub(cross(p1, v1), cross(p0, v0))
    
        # Unknowns order: [Px, Py, Pz, Vx, Vy, Vz]
        # Note: a x X = [a_y*X_z - a_z*X_y, a_z*X_x - a_x*X_z, a_x*X_y - a_y*X_x]
        rows = [
            [0, -dv[2], dv[1], 0, -dp[2], dp[1], rhs[0]],
            [dv[2], 0, -dv[0], dp[2], 0, -dp[0], rhs[1]],
            [-dv[1], dv[0], 0, -dp[1], dp[0], 0, rhs[2]],
        ]
        for row in rows:
            matrix.append([Fraction(x) for x in row])
    
    
    def gaussian_elimination(matrix):
        n = len(matrix)
        for i in range(n):
            # Find pivot
            pivot = next(r for r in range(i, n) if matrix[r][i] != 0)
            matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
    
            # Normalize pivot row
            div = matrix[i][i]
            matrix[i] = [val / div for val in matrix[i]]
    
            # Eliminate column
            for r in range(n):
                if r != i and matrix[r][i] != 0:
                    factor = matrix[r][i]
                    matrix[r] = [
                        matrix[r][c] - factor * matrix[i][c] for c in range(n + 1)
                    ]
    
        return [int(row[n]) for row in matrix]
    
    
    
    stones = []
    for line in lines:
        x,y,z,vx,vy,vz = [int(a) for a in line.replace(' @ ',', ').split(', ')]
        stones.append( ((x,y,z), (vx,vy,vz))) 
    
    # Build 6x6 augmented matrix using the first 3 hailstones
    matrix = []
    p0, v0 = stones[0]
    add_equations(matrix, p0, v0, *stones[1])
    add_equations(matrix, p0, v0, *stones[2])
    
    px, py, pz, vx, vy, vz = gaussian_elimination(matrix)
    result = px + py + pz
    

    return f"The sum of the position coordinates is {result}"  
 
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







