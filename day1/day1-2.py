# imports

# create array of input numbers

with open("day1/input", "r") as input:
    inputlist = [int(i) for i in input.read().splitlines()]

while len(inputlist) > 1:
    firstvalue = inputlist.pop(0)
    target = 2020 - firstvalue
    searchlist = inputlist[:] # the [:] is so that python copies the list rather than creating a new reference to it
    while len(searchlist) > 1:
        secondvalue = searchlist.pop(0)
        for thirdvalue in searchlist:
            if secondvalue + thirdvalue == target:
                print(firstvalue)
                print(secondvalue)
                print(thirdvalue)
                print(firstvalue + secondvalue + thirdvalue)
                print(firstvalue * secondvalue * thirdvalue)
                break
            else:
                pass
