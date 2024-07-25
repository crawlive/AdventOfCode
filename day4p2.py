import re;
import os;
from pathlib import Path;

#read_file = open("./input/day4Test.txt", 'r')
read_file = open("./input/day4Input.txt", 'r')

def findNumMatches(line):
    winningNums = (list(map(int, re.search('(?<=\:).*(?=\|)', line).group(0).strip().split())))
    scratchedNums = (list(map(int, re.search('(?<=\|).*', line).group(0).strip().split())))
    matchSet = set(winningNums) & set(scratchedNums)
    return len(matchSet)
    
numLines = len(read_file.readlines())
scratchCards = [1 for x in range(numLines)]
read_file.seek(0)
lineNum = 0
while read_file:
    line = read_file.readline()
    if line == "":
        break
    numMatches = findNumMatches(line)
    if numMatches > 0:
        for copy in range(scratchCards[lineNum]):
            for card in range(lineNum+1, lineNum+numMatches+1):
                scratchCards[card] += 1
    lineNum += 1 
          
print(scratchCards)      
print("Total: ", sum(scratchCards))