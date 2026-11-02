# api-testing-pytest

Automated API tests for the JSONPlaceholderAPI, written with pytest and requests.

## What's covered

<A short list of the endpoints and behaviours tested so far. Keep it honest.>

- `GET /posts/1` returns 200
- add each new test here

## Tech stack

- Python 3.15.0
- pytest
- requests
- python-dotenv

## Getting started

1. Clone the repo:
   ```bash
   git clone https://github.com/laurenaitken/api-testing-pytest.git
   cd api-testing-pytest
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment file:
   ```bash
   cp .env.example .env
   ```
   BASE_URL is the JSON Placeholder API URL.

## Running the tests

```bash
pytest -v
```

How to run a single file or test:
e.g. `pytest tests/test_posts.py -v`

## Project structure

```
api-testing-pytest/
├── tests/             # Where all test modules live
├── config.py          # Configures the environment variables
├── .env.example       # Examples of environment variables
├── requirements.txt   # Dependencies and installations for project
└── README.md
```

## Roadmap

Planned next steps:

- [ ] Response body assertions
- [ ] POST/PUT/DELETE tests
- [ ] Fixtures
- [ ] GitHub Actions CI

## About the API

JSONPlaceholder: a free, public fake REST API for testing. 
Link: https://jsonplaceholder.typicode.com