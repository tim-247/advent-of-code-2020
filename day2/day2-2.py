# imports

# functions

def checkPassword (line):
    # split by space
    passwordToCheck = line.split()
    # remove the colon in [1]
    passwordToCheck[1] = passwordToCheck[1][0]
    # convert the position values to tuple
    passwordToCheck[0] = tuple(passwordToCheck[0].split('-'))
    # boolean XOR check returns 1 if either statement is true
    return int(
        (passwordToCheck[1] == passwordToCheck[2][int(passwordToCheck[0][0]) - 1]) !=
        (passwordToCheck[1] == passwordToCheck[2][int(passwordToCheck[0][1]) - 1])
        )

# open input file for use

with open("day2/input", "r") as input:
    inputlist = input.read().splitlines()

# do the counting

countValidPasswords = 0

for line in inputlist:
    countValidPasswords += checkPassword(line)

print(countValidPasswords)
