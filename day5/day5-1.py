with open("day5/input", "r") as input:
    inputlist = input.read().splitlines()


numlist = [[int(l[-3:].replace('L', '0').replace('R', '1'), 2), int(l[:-3].replace('F', '0').replace('B', '1'), 2) * 8] for l in inputlist]
numlist.sort(reverse=True, key=sum)

print(sum(numlist[0]))
