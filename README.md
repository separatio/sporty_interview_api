# Introduction

This is an API test framework using pytest.
The version of Python used is 3.10.

# Setup

All instructions below assume a working Python3 environment with pip installed. The project is currently using Python version 3.10.

1. Create the virtual environment by running `python -m venv venv`
2. Activate the virtual environment by running `source venv/bin/activate`
3. Install required packages by running `pip install -r requirements.txt`

# Docker

To use the dockerized version build and run the image:

```bash
docker build . -t sporty_interview
docker run -it sporty_interview
```
