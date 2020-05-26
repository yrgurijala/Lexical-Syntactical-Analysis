import sys
from textAnalysis import *

# The Following code takes input from a txt file
argument = sys.argv[1]
filename = ""
lengthOfFile = len(argument)
i1 = 6

while i1 < lengthOfFile:
    filename = filename + argument[i1]
    i1 = i1 + 1

inputFile = open(filename, "r")
finaldisplay = ""

for line in inputFile:
    check = lex(line)

    i = 0
    while i < len(line):
        if line[i] is not '\n' and line[i] is not ' ':
            finaldisplay = finaldisplay + line[i]
        i = i + 1

    if check[0] is not 'i':
        finaldisplay = finaldisplay + '=' + str(int(check))
    else:
        finaldisplay = finaldisplay + '=' + check

    print(finaldisplay)
    finaldisplay = ""
