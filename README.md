# Introduction

This is an API test framework using pytest.
The version of Python used is 3.10.

# Setup

All instructions below assume a working Python3 environment with pip installed. The project is currently using Python version 3.10.

1. Create the virtual environment by running `python -m venv venv`
2. Activate the virtual environment by running `source venv/bin/activate`
3. Install required packages by running `pip install -r requirements.txt`

# Running the tests

After following the Setup step above, just run

```bash
pytest
```

This will detect the test and run it.

# Test cases

| Test Case              | Animal Type | Amount |
| ---------------------- | ----------- | ------ |
| Minimum facts amount   | cat         | 1      |
| Maximum facts amount   | cat         | 500    |
| Boundary above maximum | cat         | 501    |
| Boundary below minimum | cat         | 0      |

# Validation

I used simple assertions on the responses.
For this exercise, overcomplicating was not worth the time.

I considered adding expected results in the parametrized function as well.
Example:

```python
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
```

# CI

A Github Action was implemented and can be run from the Actions tab in Github.
It will run the current test.
