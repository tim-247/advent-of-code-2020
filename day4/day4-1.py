with open('day4/input', 'r') as input:
    inputlines = input.read().splitlines()
inputlines.append('')


def lineToDict(line):
    return dict(p.split(":") for p in line.split())


def verifyDict(d):
    if len(d.keys()) not in [7, 8]:
        return False
    elif len(d.keys()) == 8:
        return True
    elif len(d.keys()) == 7:
        if optional_fields[0] in d.keys():
            return False
        else:
            return True


def processLine(line):
    d = lineToDict(line)
    return d


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]

passports = []
rejected_passports = []
passport = {}

for line in inputlines:
    if len(line) > 0:
        passport.update(processLine(line))
    else:
        if verifyDict(passport) is True:
            passports.append(passport)
        else:
            rejected_passports.append(passport)
        passport = {}
print(len(passports))
