def findfirstdigit(string):
    digindex = 10000
    for letter in ["0","1","2","3","4","5","6","7","8","9"]:
        index = string.find(letter)
        if index >= 0 and index < digindex:
            digindex = index
    return string[digindex]

def findlastdigit(string):
    digindex = -1
    for letter in ["0","1","2","3","4","5","6","7","8","9"]:
        index = string.rfind(letter)
        if index > digindex:
            digindex = index
    return string[digindex]

def findcalibrationvalue(string):
    first = findfirstdigit(string)
    second = findlastdigit(string)
    return first+second

def sumvalues(input):
    list = input.splitlines()
    value = 0
    for string in list:
        value += (int(findcalibrationvalue(string)))
    return value

print(findfirstdigit("asdfewa1aetwear43253"))
assert findfirstdigit("asdfewa1aetwear43253") == "1"

assert findlastdigit("asdfewa1aetwear43253") == "3"

assert findfirstdigit("five3nine") == "3"
assert findlastdigit("five3nine") == "3"

assert findcalibrationvalue("1abc2") == "12"
assert findcalibrationvalue("pqr3stu8vwx") == "38"
assert findcalibrationvalue("a1b2c3d4e5f") == "15"
assert findcalibrationvalue("treb7uchet") == "77"

assert sumvalues("""1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet""") == 142

with open("day1puzzle1inputdata") as f:
    data = f.read()

print(sumvalues(data))
