<!-- Parsing Components:
 - Reader
    - In Memory VS Stream:
        - Go with In Memory as we don't expect a datetime format in english to approach an especially large size
 - Lexer
 - Parser
 - "Spellchecker"
 - Error Handler -->

Note:
A full parser is way too large of a task, as would be a trained model from scratch given the coding and time constraints. Aiming for a relatively complete system that works through programattic rules to determine the date instead with an emphasis on displaying thought process and being efficient with time

Outside of scope:

- Stacking modifiers in a non-english way
  - next next next next tuesday (vs tuesday 3 weeks from now)
  - last tuesday after next (as a way to say next tuesday)
- Spelled word conversion to integer form. For now we are assuming all pure numbers (not specific definitions like noon or midnight) come in their integer form
- Plenty of edge cases. Given the time constraints we aren't going to catch every possible phrasing of time

Sample Input Phrases:

- "Tomorrow at 11am"
- "This coming Tuesday at 9pm"
- "Next Tuesday at 9pm"
- "Teuesdey oif Nexx weak att 9 pm"
- "Tuesday next pm 9" -> Should this error?
- "half-past noon on the Tuesday after next"

Output:

- YYYY/MM/DD HH:MM
