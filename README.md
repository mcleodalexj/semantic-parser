# semantic-parser

Repository with the Semantic Parser Project

Key Files:

- DateParser.py: The class that parses dates from sentences
- TestDateParser.py: Test suite for easily testing changes
- datewords.txt: words for the spellchecker to weight towards

The class can be invoked using the following:

```
from DateParser import DateParser

DateParser(inputString, baseDateTime).extract_date()

# Optional boolean as third argument for enabling spellcheck
DateParser(inputString, baseDateTime, True).extract_date()

```

Instructions to run:

```
# cd into location of repo
# create venv
python -m venv venv
# activate venv
. venv/bin/activate
# install requirements
pip install -r requirements.txt
# run test suite and confirm tests are passing with no issues
pytest -q TestDateParser.py
```
