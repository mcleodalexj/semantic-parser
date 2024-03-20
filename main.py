import re

testStrings = [
    "Tomorrow at 11am",
    "This coming Tuesday at 9pm",
    "Next Tuesday at 9pm",
    "Teuesdey oif Nexx weak att 9 pm",
    "Tuesday next pm 9",
    "half-past noon on the Tuesday after next"
]
testNow = '2023-02-24'


# For what we are building a full Reader/Lexer feels overkill. Lets split on whitespace and alphabetical vs numeric
for testString in testStrings:
    lexenes = re.findall(r"[^\W\d_]+|\d+", testString)
    print(lexenes)
