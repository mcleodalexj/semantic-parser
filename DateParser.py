import datetime
import re

class DateParser:

    days = {
        "monday": 0,
        "tuesday":1,
        "wednesday":2,
        "thursday":3,
        "friday":4,
        "saturday":5,
        "sunday":6,
        "mon":0,
        "tues":1,
        "wed":2,
        "thurs":3,
        "fri": 4,
        "sat": 5,
        "sun": 6
    }

    months = {
        'january': 1,
        'jan': 1,
        'february': 2,
        'feb': 2,
        'march': 3,
        'mar': 3,
        'april': 4,
        'apr': 4,
        'may': 5,
        'june': 6,
        'jun': 6,
        'july': 7,
        'jul': 7,
        'august': 8,
        'aug': 8,
        'september': 9,
        'sep': 9,
        'october': 10,
        'oct': 10,
        'november': 11,
        'nov': 11,
        'december': 12,
        'dec': 12
    }

    monthPreMods = {
        'next': 1,
        'last': -1
    }

    dayRelative = {
        "today": 0,
        "tomorrow": 1,
        "yesterday": -1,
    }

    valueKeyword = [
        "minutes", "days", "weeks", "months", "hours", "years"
    ]

    valueModifier = {
        "from":
            [
                "now",
                "yesterday",
                "tomorrow"
            ],
        "ago": -1
    }

    # Modifications that shift the day by a week, IE next Tuesday is the next Tuesday + a week
    dayWeekPreMods = {
        "next": 7,
        "last": -7,
        "coming": 0
    }

    dayWeekPostMods = {
        "after": {
            "next": 14,
            "this": 7
        }
    }

    # Modifications that only shift the date by a day, IE the day after monday is just Tuesday
    dayDayMods = {
        "after": 1,
        "before": -1,
    }

    hour = {
        "noon": 12,
        "midnight": 0,
    }

    hourIndicator = {
        "am": 0,
        "pm": 12
    }

    minutes = {
        "halfpast": 30,
        "half": {
            "past": 30
        },
        "quarter": {
            "till": 45,
            "before": 45,
            "after": 15
        }
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
        "year" : 0,
        "years": 0,
        "in": 0,
    }

    yearMods = {
        "next": 1,
        "this": 0,
        "last": -1
    }

    def __init__(self, input_string, base_date=None) -> None:
        self.pre_mod_input = input_string
        self.input_string = self.clean_string(input_string)
        self.tokens = self.get_tokens(self.input_string)
        if base_date:
            try:
                self.base_date = datetime.datetime.fromisoformat(base_date)
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        else:
            self.base_date = datetime.datetime.today()

    @staticmethod
    def clean_string(input_string):
        # Cleanup any nonalphanumeric and non space characters + any trailing or leading whitespace
        clean_string = re.sub(r'[^A-Za-z0-9 ]+', '', input_string).lower().strip()
        # Remove "the", "a", "an" as they do not impact the date
        clean_string = clean_string.replace(" the ", " ").replace(" a "," ").replace(" an "," ")
        return clean_string


    @staticmethod
    def get_tokens(input_string):
        tokens = re.findall(r"[^\W\d_]+|\d+", input_string)

        if not tokens:
            print("No data to parse")
        return tokens

    def extract_date(self):
        day = None
        day_modifier = 0
        month = None
        month_modifier = 0
        year = None
        year_modifier = 0
        hour = None
        hour_modifier = 0
        minute = None
        minute_modifier = 0
        token_len = len(self.tokens)
        orig_day_val = self.base_date.weekday()
        orig_month_val = self.base_date.month

        # print(self.tokens)

        for index, token in enumerate(self.tokens):

            print(self.tokens)

            # Set tokens to empty if used to avoid a scenario where 'march after next year'
            # could be doubly interpreted into 'march after next' and 'next year'.
            # Skip those tokens once set as empty
            if token == '':
                continue

            # For context grab the two tokens before and after our current token,
            # as we can expect values, modifiers, etc.
            two_words_before = None
            word_before = None
            word_after = None
            two_words_after = None
            if index != 0:
                word_before = self.tokens[index-1]
            if index != token_len-1:
                word_after = self.tokens[index+1]
            if index > 1:
                two_words_before = self.tokens[index-2]
            if index < token_len-2:
                two_words_after = self.tokens[index+2]


            # if we see a plural form of a unit of time, we want to see
            # what value is before it and what keywords are after it
            if token in self.valueKeyword:
                print(f'Condition hit for {word_before} {token} {word_after}')
                modifier = 0
                if re.match(r'\d+', word_before):
                    modifier = int(word_before)
                    self.tokens[index-1] = ''
                if word_after in self.valueModifier:
                    if word_after == 'ago':
                        modifier = modifier * -1
                        self.tokens[index+1] = ''
                print(f'modifier is {modifier}')
                if token == 'years':
                    year_modifier += modifier
                elif token == 'months':
                    month_modifier += modifier
                elif token == 'weeks':
                    day_modifier += modifier*7
                elif token == 'days':
                    day_modifier += modifier
                elif token == 'hours':
                    hour_modifier += modifier
                elif token == 'minutes':
                    minute_modifier += modifier
                self.tokens[index] = ''



            # Logic for if we see a day of the week
            if token in self.days:
                day_val = self.days.get(token)
                self.tokens[index] = ''
                if orig_day_val < day_val:
                    day_modifier += day_val - orig_day_val
                elif day_val < orig_day_val:
                    day_modifier += day_val + 7 - orig_day_val
                if self.dayWeekPreMods.get(word_before):
                    day_modifier += self.dayWeekPreMods.get(word_before)
                    self.tokens[index-1] = ''
                elif self.dayWeekPostMods.get(word_after):
                    pass

            # logic for if we see year or a year
            if token in self.years:
                if word_before in self.yearMods:
                    year_modifier += self.yearMods.get(word_before)
                    self.tokens[index-1] = ''
                elif re.match(r'\d{4}', word_after):
                    year = int(word_after)
                    self.tokens[index+1] = ''

            # Logic for if we see today/tomorrow/yesterday
            if token in self.dayRelative:
                day_modifier += self.dayRelative.get(token)
                self.tokens[index] = ''

            # Logic for if we see the name of the month
            if token in self.months:
                month_val = self.months.get(token)
                self.tokens[index] = ''
                if orig_month_val < month_val:
                    month_modifier += month_val - orig_month_val
                elif month_val < orig_month_val:
                    month_modifier += month_val + 12 - orig_month_val
                if self.monthPreMods.get(word_before):
                    year_modifier += self.monthPreMods.get(word_before)
                    self.tokens[index-1] = ''

            # Logic for if we see noon/midnight (can be expanded to dawn/dusk/morning/afternoon etc)
            if token in self.hour:
                hour = self.hour.get(token)
                # Weird condition, do we mean midnight tonight? that is technically 00:00 tomorrow?
                # Assuming instead that we mean midnight of what we consider tomorrow night
                # which is 00:00 two days from now
                if token == 'midnight':
                    day_modifier += 1
                self.tokens[index] = ''

            # Logic once we see AM or PM indicating an hour
            if token in self.hourIndicator:
                hour_modifier = self.hourIndicator.get(token)
                self.tokens[index] = ''
                if re.match(r'\d{1,2}', word_before) is None:
                    if self.engNums.get(token):
                        hour = self.engNums.get(token)
                        self.tokens[index-1] = ''
                    else:
                        print("invalid hour found")
                else:
                    temp_hour = int(word_before)
                    if temp_hour >= 0 and temp_hour < 13:
                        hour = temp_hour
                    elif temp_hour >= 13:
                        hour_modifier = 0
                        hour = temp_hour
                    else:
                        print("invalid hour found")

        if year is None:
            year = self.base_date.year
        if month is None:
            month = self.base_date.month
        if day is None:
            day = self.base_date.day
        if hour and not minute:
            minute = 0
        if not hour and not minute:
            hour = self.base_date.hour
            minute = self.base_date.minute

        return_date = datetime.datetime(year, month, day, hour, minute)

        if year_modifier:
            try:
                return return_date.replace(year = return_date.year + year_modifier)
            except ValueError:
                return return_date + (datetime.datetime(return_date.year + year_modifier, 1, 1)
                                      - datetime.datetime(return_date.year, 1, 1))
        if month_modifier:
            return_date = return_date + datetime.timedelta(months=month_modifier)
        if day_modifier:
            return_date = return_date + datetime.timedelta(days=day_modifier)
        if hour_modifier:
            return_date = return_date + datetime.timedelta(hours=hour_modifier)
        if minute_modifier:
            return_date = return_date + datetime.timedelta(minutes=minute_modifier)

        print(f'Input was: {self.pre_mod_input}, output is :{return_date}')
        return return_date
