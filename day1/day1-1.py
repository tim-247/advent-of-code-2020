# imports

# create array of input numbers

with open("day1/input", "r") as input:
    inputlist = [int(i) for i in input.read().splitlines()]

while len(inputlist) > 1:
    firstvalue = inputlist.pop(0)
    for i in inputlist:
        if firstvalue + i == 2020:
            print(firstvalue)
            print(i)
            print(firstvalue + i)
            print(firstvalue * i)
            break
        else:
            pass
