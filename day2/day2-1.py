# imports

# functions

def checkPassword (line):
    # split by space
    passwordToCheck = line.split()
    # remove the colon in [1]
    passwordToCheck[1] = passwordToCheck[1][0]
    # convert the min/max values to tuple
    passwordToCheck[0] = tuple(passwordToCheck[0].split('-'))
    if int(passwordToCheck[0][0]) <= passwordToCheck[2].count(passwordToCheck[1]) <= int(passwordToCheck[0][1]):
        return 1
    else:
        return 0

# open input file for use

with open("day2/input", "r") as input:
    inputlist = input.read().splitlines()

# do the counting

countValidPasswords = 0

for line in inputlist:
    countValidPasswords += checkPassword(line)

print(countValidPasswords)
