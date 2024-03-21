import re
import datetime
from DateParser import DateParser


testStrings = [
    "Tomorrow at 11am",
    "Today at 9 PM",
    "Yesterday at 1 AM",
    "This coming Tuesday at 9pm",
    "Next Tuesday at 9pm",
    # "Teuesdey oif Nexx weak att 9 o'clock pm",
    "half-past noon on the Tuesday after next",
    # ""
]
testNow = '2023-02-24'

# For what we are building a full Reader/Lexer feels overkill. Lets split on whitespace and alphabetical vs numeric
for testString in testStrings:
    DateParser(testString, "2024-03-18")



