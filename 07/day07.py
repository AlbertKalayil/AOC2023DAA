import easygui
import time
from collections import Counter 

AOCDAY = "07"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
    
    def handtype(self):
        freq = Counter(self.cards)
        values = list(freq.values())
        values.sort(reverse=True)
        val1 = values[0]

        if val1 != 5 and values[1] == 2:
            val2 = 1
        
        else:
            val2 = 0
        
        return val1 * 2 + val2
    
    def cardvalue(self):
        val_dict = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
        result = 0

        for i in range(5):
            digit = self.cards[4-i]
            result += pow(13, i) * val_dict[digit]

        return result
    
    def handscore(self):
        return self.cardvalue() + (self.handtype() * pow(13, 5))
    
    def __lt__(self, other):
        return self.handscore() < other.handscore()
        
        
class Hand_Part2:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
    
    def handtype(self):
        freq = Counter(self.cards)
        jacks = freq['J']
        values = list(freq.values())
        values.sort(reverse=True)
        val1 = values[0]
        
        if val1 == 5:
            return 10
        
        val2 = values[1]

        score = val1 * 2 + (1 if val2 == 2 else 0)

        if jacks == 0:
            return val1 * 2 + (1 if val2 == 2 else 0)

        if val1 != 5 and values[1] == 2:
            val2 = 1
        
        else:
            val2 = 0
        
        return val1 * 2 + val2
    
    def cardvalue(self):
        val_dict = {'J':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'Q':11, 'K':12, 'A':13}
        result = 0

        for i in range(5):
            digit = self.cards[4-i]
            result += pow(13, i) * val_dict[digit]

        return result
    
    def handscore(self):
        return self.cardvalue() + (self.handtype() * pow(13, 5))
    
    def __lt__(self, other):
        return self.handscore() < other.handscore()




def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    hands = []
    for line in lines:
        cards = line.split()[0]
        bid = int(line.split()[1])
        hands.append(Hand(cards,bid))

    hands.sort()
    result = 0

    for i, hand in enumerate(hands):
        result += (i + 1) * hand.bid

    return(f"The total winnings are {result}")

def part2(lines):
        # Code the solution to part 1 here, returning the answer as a string
    hands = []
    for line in lines:
        cards = line.split()[0]
        bid = int(line.split()[1])
        hands.append(Hand_Part2(cards, bid))

    for hand in hands:
        hand.handtype()
    # hands.sort()
    # result = 0

    # for i, hand in enumerate(hands):
    #     result += (i + 1) * hand.bid


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







