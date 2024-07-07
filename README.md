# Introduction

This is a test framework using pytest and SeleniumBase.
The version of Python used is 3.10.

# Setup

All instructions below assume a working Python3 environment with pip installed. The project is currently using Python version 3.10.

1. Create the virtual environment by running `python -m venv venv`
2. Activate the virtual environment by running `source venv/bin/activate`
3. Install required packages by running `pip install -r requirements.txt`

# Running

Use the following command to run the test:

```bash
pytest tests/first_test.py --mobile --headed --demo --uc
```
