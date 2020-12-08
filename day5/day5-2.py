with open("day5/input", "r") as input:
    inputlist = input.read().splitlines()


numlist = [int(s.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0"), 2) for s in inputlist]

print(set(range(min(numlist), max(numlist))).difference(numlist))
