import datetime
from DateParser import DateParser

class TestDateParser:
    def test_tomorrow(self):
        result = DateParser("Tomorrow at 11am", "2023-02-24").extract_date()
        expected = datetime.datetime.fromisoformat("2023-02-25 11:00:00")
        assert result == expected

    def test_today(self):
        result = DateParser("Today at 9 PM", "2023-02-24").extract_date()
        expected = datetime.datetime.fromisoformat("2023-02-24 21:00:00")
        assert result == expected

    def test_yesterday(self):
        result = DateParser("Yesterday at 1 AM", "2023-02-24").extract_date()
        expected = datetime.datetime.fromisoformat("2023-02-23 01:00:00")
        assert result == expected

    def test_coming(self):
        result = DateParser("This coming Tuesday at 9pm", "2024-03-17").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-19 21:00:00")
        assert result == expected

    def test_next_day_of_week(self):
        result = DateParser("Next Tuesday at 9pm", "2024-03-17").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-26 21:00:00")
        assert result == expected

    def test_halfpast(self):
        result = DateParser("half-past noon on the Tuesday after next", "2024-03-17").extract_date()
        expected = datetime.datetime.fromisoformat("2023-04-02 12:30:00")
        assert result == expected

    def test_next_year(self):
        result = DateParser("March nineteenth next year", "2024-03-17").extract_date()
        expected = datetime.datetime.fromisoformat("2025-03-19 00:00:00")
        assert result == expected

    def test_next_month(self):
        result = DateParser("Next March at 12 pm", "2024-03-17").extract_date()
        expected = datetime.datetime.fromisoformat("2025-03-17 12:00:00")
        assert result == expected

    def test_noon(self):
        result = DateParser("tomorrow at noon", "2024-03-17").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-18 12:00:00")
        assert result == expected

    def test_midnight(self):
        result = DateParser("tomorrow at midnight", "2024-03-17").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-19 00:00:00")
        assert result == expected

    def test_exact_year(self):
        result = DateParser("march nineteenth 1984", "2024-03-17").extract_date()
        expected = datetime.datetime.fromisoformat("1984-03-19 00:00:00")
        assert result == expected

    # def test_3_weeks(self):
    #     result = DateParser("Monday at Noon in 3 weeks", "2024-03-17").extract_date()
    #     expected = datetime.datetime.fromisoformat("2025-03-17 12:00:00")
    #     assert result == expected

    # def test_3_weeks_from_now(self):
    #     result = DateParser("Monday at Noon 3 weeks from now", "2024-03-17").extract_date()
    #     expected = datetime.datetime.fromisoformat("2025-03-17 12:00:00")
    #     assert result == expected

    def test_10_minutes_from_now(self):
        result = DateParser("10 Minutes from now", "2024-03-17 12:00:00").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-17 12:10:00")
        assert result == expected

    def test_10_minutes_ago(self):
        result = DateParser("10 Minutes ago", "2024-03-17 12:00:00").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-17 11:50:00")
        assert result == expected

    def test_10_hours_from_now(self):
        result = DateParser("10 Hours from now", "2024-03-17 12:00:00").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-17 22:00:00")
        assert result == expected

    def test_10_hours_ago(self):
        result = DateParser("10 Hours ago", "2024-03-17 12:00:00").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-17 02:00:00")
        assert result == expected

    def test_10_days_from_now(self):
        result = DateParser("10 days from now", "2024-03-17 12:00:00").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-27 12:00:00")
        assert result == expected

    def test_10_days_from_yesterday(self):
        result = DateParser("10 days from yesterday", "2024-03-17 12:00:00").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-26 12:00:00")
        assert result == expected

    def test_10_days_ago(self):
        result = DateParser("10 days ago", "2024-03-17 12:00:00").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-07 12:00:00")
        assert result == expected

    def test_10_minutes_after(self):
        result = DateParser("10 minutes after 3 pm tomorrow", "2024-03-17 12:00:00").extract_date()
        expected = datetime.datetime.fromisoformat("2024-03-18 15:10:00")
        assert result == expected
