book = {"0":"0",
        "1":"1",
        "2":"2",
        "3":"3",
        "4":"4",
        "5":"5",
        "6":"6",
        "7":"7",
        "8":"8",
        "9":"9",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"}

def findfirstdigit(string):
    digindex = 10000
    output = None
    for letter in book.keys():
        index = string.find(letter)
        if index >= 0 and index < digindex:
            digindex = index
            output = book[letter]
    return output

def findlastdigit(string):
    digindex = -1
    output = None
    for letter in book.keys():
        index = string.rfind(letter)
        if index > digindex:
            digindex = index
            output = book[letter]
    return output

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

assert findfirstdigit("five3nine") == "5"
assert findlastdigit("five3nine") == "9"

assert findcalibrationvalue("1abc2") == "12"
assert findcalibrationvalue("pqr3stu8vwx") == "38"
assert findcalibrationvalue("a1b2c3d4e5f") == "15"
assert findcalibrationvalue("treb7uchet") == "77"

assert sumvalues("""1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet""") == 142

assert sumvalues("""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""") == 281


with open("day1.txt") as f:
   data = f.read()#

print(sumvalues(data))
