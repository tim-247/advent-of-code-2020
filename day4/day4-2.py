import re


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]

pid = re.compile(r"^[0-9]{9}$")
hcl = re.compile(r"^#[0-9a-f]{6}$")
hgt = re.compile(r"([0-9]+)(.*)$")

passports = []
current_passport = {}

with open('day4/input', 'r') as input:
    inputlines = input.read().splitlines()
inputlines.append('')


def lineToDict(line):
    return dict(p.split(":") for p in line.split())


def verifyPassport(passport):
    if len(passport.keys()) not in [7, 8]:
        return False
    elif len(passport.keys()) == 8:
        return all([verifyFields(field) for field in passport.items()])
    elif len(passport.keys()) == 7:
        if optional_fields[0] in passport.keys():
            return False
        else:
            return all([verifyFields(field) for field in passport.items()])


def processLine(line):
    d = lineToDict(line)
    return d


def verifyFields(passport):
    if passport[0] == "byr":
        return 1920 <= int(passport[1]) <= 2002
    elif passport[0] == "iyr":
        return 2010 <= int(passport[1]) <= 2020
    elif passport[0] == "eyr":
        return 2020 <= int(passport[1]) <= 2030
    elif passport[0] == "ecl":
        return passport[1] in ["amb", "blu", "brn",
                                "grn", "gry", "hzl", "oth"]
    elif passport[0] == "pid":
        return bool(pid.match(passport[1]))
    elif passport[0] == "hcl":
        return bool(hcl.match(passport[1]))
    elif passport[0] == "hgt":
        if hgt.match(passport[1]).group(2) == "cm" and \
            150 <= int(hgt.match(passport[1]).group(1)) <= 193:
            return True
        elif hgt.match(passport[1]).group(2) == "in" and \
            59 <= int(hgt.match(passport[1]).group(1)) <= 76:
            return True
        else:
            return False
    elif passport[0] == "cid":
        return True
    else:
        raise ValueError("Invalid field")


for line in inputlines:
    if len(line) > 0:
        current_passport.update(processLine(line))
    else:
        if verifyPassport(current_passport) is True:
            passports.append(current_passport)
        current_passport = {}
print(len(passports))
