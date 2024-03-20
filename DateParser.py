import datetime
import re

class DateParser:

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

    years = {
        "year" : 0
    }

    yearMods = {
        "next": 1,
        "this": 0,
        "last": -1
    }

    def __init__(self, inputString, baseDate=None) -> None:
        self.preModInput = inputString
        self.inputString = self.cleanString(inputString)
        self.tokens = self.getTokens(self.inputString)
        if baseDate:
            try:
                datetime.date.fromisoformat(baseDate)
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        else:
            self.baseDate = datetime.datetime.today()
        self.extract_date()
        
    @staticmethod
    def cleanString(inputString):
        # Cleanup any nonalphanumeric and non space characters, as well as any trailing or leading whitespace
        cleanString = re.sub(r'[^A-Za-z0-9 ]+', '', inputString).lower().strip()
        # Remove "the", "a", "an" as they do not impact the date
        cleanString = cleanString.replace(" the ", " ").replace(" a "," ").replace(" an "," ")
        return cleanString
    
        
    @staticmethod        
    def getTokens(inputString):
        tokens = re.findall(r"[^\W\d_]+|\d+", inputString)

        if not tokens:
            print("No data to parse")
        return tokens
    
    def extract_date(self):
        day = None
        dayModifier = None
        month = None
        monthModifier = None
        year = None
        yearModifier = None
        hour = None
        hourModifier = None
        minute = None
        minuteModifier = None
        tokenLen = len(self.tokens)

        for index, token in enumerate(self.tokens):
            # For context grab the tokens before and after our current token, as we can expect values, modifiers, etc.
            wordBefore = None
            wordAfter = None
            if index != 0:
                wordBefore = self.tokens[index-1]
            if index != tokenLen-1:
                wordAfter = self.tokens[index+1]

        
            if token in self.dayRelative:
                dayModifier = self.dayRelative.get(token)
            if token in self.hourIndicator:
                hourModifier = self.hourIndicator.get(token)
                if re.match(r'\d{1,2}', wordBefore) is None:
                    if self.engNums.get(token):
                        hour = self.engNums.get(token)
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
            
        if year == None:
            year = self.baseDate.year                    
        if month == None:
            month = self.baseDate.month        
        if day == None:
            day = self.baseDate.day
        if hour and not minute:
            minute = 0
        if not hour and not minute:
            hour = self.baseDate.hour
            minute = self.baseDate.minute

        returnDate = datetime.datetime(year, month, day, hour, minute)

        if dayModifier:
            returnDate = returnDate + datetime.timedelta(days=dayModifier)
        if hourModifier:
            returnDate = returnDate + datetime.timedelta(hours=hourModifier)

        print(f'Input was: {self.preModInput}, output is :{returnDate}')
        return returnDate