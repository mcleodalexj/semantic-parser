<!-- Parsing Components:
 - Reader
    - In Memory VS Stream:
        - Go with In Memory as we don't expect a datetime format in english to approach an especially large size
 - Lexer
 - Parser
 - "Spellchecker"
 - Error Handler -->

Note:
 A full parser is way too large a scope for this task, as would be a trained model given the time constraints.  Aiming for a relatively complete system that works through programattic rules to determine the date instead. 

Outside of scope:
 - Stacking modifiers in a non-enlish way
    - next next next next tuesday (vs tuesday 3 weeks from now)
    - last tuesday after next (as a way to say next tuesday)
 - Spelled word conversion to integer form.  For now we are assuming all pure numbers (not specific definitions like noon or midnight) come in their integer form

Sample Input Phrases:
 - "Tomorrow at 11am"
 - "This coming Tuesday at 9pm"
 - "Next Tuesday at 9pm"
 - "Teuesdey oif Nexx weak att 9 pm"
 - "Tuesday next pm 9" -> Should this error?
 - "half-past noon on the Tuesday after next"

Output:
 - YYYY/MM/DD HH:MM

Quick Time Term List:
 - Early (adv)
 - Late (adv)
 - Now
 - Soon, Immediately
 - Day
 - Night
 - Dawn
 - Morning
 - Noon
 - Evening
 - Today
 - Tomorrow
 - Yesterday
 - Hour
 - Minute, Second
 - Week
 - Sunday
 - Monday
 - Tuesday
 - Wednesday
 - Thursday
 - Friday
 - Saturday
 - Month
 - Names of the Months
 - Year