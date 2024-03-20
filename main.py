import re
import datetime

days = {
    "monday": 1,
    "tuesday":2,
    "wednesday":3,
    "thursday":4,
    "friday":5,
    "saturday":6,
    "sunday":7,
    "mon":1,
    "tues":2,
    "wed":3,
    "thurs":4,
    "fri": 5,
    "sat": 6,
    "sun": 7
}
dayRelative = {
    "today": 0,
    "tomorrow": 1,
    "yesterday": -1,
    "days": None
}

dayPreMods = {
    "next": 7,
    "after": 1,
    "before": -1,
    "last":-7
}

hourIndicator = {
    "am": 0,
    "pm": 12
}

engNums = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30
}

testStrings = [
    "Tomorrow at 11am",
    "Today at 9 PM",
    "Yesterday at 1 AM"
    # "This coming Tuesday at 9pm",
    # "Next Tuesday at 9pm",
    # "Teuesdey oif Nexx weak att 9 o'clock pm",
    # "Tuesday next pm 9",
    # "half-past noon on the Tuesday after next",
    # ""
]
testNow = '2023-02-24'

def extract_date(inputString, baseDate=None):
    preModInput = inputString
    if not baseDate:
        baseDate = datetime.datetime.today()

    # Cleanup any nonalphanumeric and non space characters, as well as any trailing or leading whitespace
    inputString = re.sub(r'[^A-Za-z0-9 ]+', '', inputString).lower().strip()
    # Remove "the", "a", "an" as they do not impact the date
    inputString = inputString.replace(" the ", " ").replace(" a "," ").replace(" an "," ")
    tokens = re.findall(r"[^\W\d_]+|\d+", inputString)

    if not tokens:
        print("No data to parse")
    # else:
    #     print(tokens)

    day = None
    dayModifier = None
    # weekday = baseDate.isoweekday()
    month = None
    monthModifier = None
    year = None
    yearModifier = None
    hour = None
    hourModifier = None
    minute = None
    minuteModifier = None
    tokenLen = len(tokens)

    for index, token in enumerate(tokens):
        # print(token)
        # For context grab the tokens before and after our current token, as we can expect values, modifiers, etc.
        wordBefore = None
        wordAfter = None
        if index != 0:
            wordBefore = tokens[index-1]
        if index != tokenLen-1:
            wordAfter = tokens[index+1]



        # if token in days:
        #     day = token
        #     if tokens[index-1] in dayPreMods:
        
        if token in dayRelative:
            dayModifier = dayRelative.get(token)
        if token in hourIndicator:
            hourModifier = hourIndicator.get(token)
            if re.match(r'\d{1,2}', wordBefore) is None:
                if engNums.get(token):
                    hour = engNums.get(token)
                else:
                    print("invalid hour found")
            else:
                tempHour = int(wordBefore)
                if tempHour >= 0 and tempHour < 13:
                    hour = tempHour
                elif tempHour >= 13:
                    hourModifier = 0
                    hour = tempHour
                else:
                    print("invalid hour found")




        # Build our output using our variables we populated
    if year == None:
        year = baseDate.year                    
    if month == None:
        month = baseDate.month        
    if day == None:
        day = baseDate.day
    if hour and not minute:
        minute = 0
    if not hour and not minute:
        hour = baseDate.hour
        minute = baseDate.minute

    # print(f'Year:{year} \n YearMod: {yearModifier} \n Month{month} \n MonthMod {monthModifier} \n Hour{hour} \n HourMod{hourModifier} \n Minute{minute} \n MinuteMod {minuteModifier}')

    returnDate = datetime.datetime(year, month, day, hour, minute)

    if dayModifier:
        returnDate = returnDate + datetime.timedelta(days=dayModifier)
    if hourModifier:
        returnDate = returnDate + datetime.timedelta(hours=hourModifier)

    print(f'Input was: {preModInput}, output is :{returnDate}')


# For what we are building a full Reader/Lexer feels overkill. Lets split on whitespace and alphabetical vs numeric
for testString in testStrings:
    extract_date(testString)



