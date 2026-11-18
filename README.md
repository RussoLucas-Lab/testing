# Pytest & GitHub Actions

[![Tests](https://github.com/RussoLucas-Lab/pytest-github-actions/actions/workflows/tests.yml/badge.svg)](https://github.com/RussoLucas-Lab/pytest-github-actions/actions/workflows/tests.yml)

Personal practice repo following **Artem Istranin**'s Udemy course on testing with Pytest and
continuous integration with GitHub Actions. _(add the course link here)_.

Each folder is an independent chapter: a self-contained mini-project demonstrating a specific
pytest concept (fixtures, parametrize, mocking, testing levels, CI/CD, etc.).

## Table of contents

| Chapter | What it demonstrates |
|---|---|
| [document-editor](document-editor/) | Basic unit testing: asserts, `pytest.raises`, `pytest.mark.xfail` to document a known bug. |
| [fixture-scope](fixture-scope/) | `scope="session"` fixtures over a shared FastAPI `TestClient`. |
| [hands-on](hands-on/) | Hands-on testing exercise for a business function (e-commerce order processing). |
| [pftracker](pftracker/) | Comprehensive review: fixtures with different scopes, `parametrize`, `pytest-mock`, `monkeypatch`, `caplog`, `pytest.ini`. |
| [user-analytics-api](user-analytics-api/) | FastAPI API with mocked slow/external dependencies, environment variables, and file uploads. |
| [unit-converter](unit-converter/) | Unit conversion library (CLI with Typer) — base version. |
| [testing-levels](testing-levels/) | The same library, explicitly organized into the three testing levels: unit, integration, system. |
| [CICD Unit Converter](CICD%20Unit%20Converter/) | The same library with its own CI pipeline (GitHub Actions). Continues as an independent repo at [RussoLucas-Lab/CI-CD-unit-converter](https://github.com/RussoLucas-Lab/CI-CD-unit-converter). |
| [more-itertools](more-itertools/README.student.md) | The open-source `more-itertools` library, vendored and used as a sandbox for testing third-party code (`tests/test_custom.py`). |
| [rund-and-debug](rund-and-debug/) | Empty folder — pending. |

## Installation

```bash
git clone https://github.com/RussoLucas-Lab/pytest-github-actions.git
cd pytest-github-actions
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

That `requirements.txt` covers the standalone chapters (document-editor, fixture-scope,
hands-on, pftracker, user-analytics-api). The packaged chapters (unit-converter,
testing-levels, CICD Unit Converter, more-itertools) are installed separately with
`pip install -e .` (or `-e ".[dev]"`) from their own folder — see each one's README.

## Running the tests

Each chapter runs independently, from inside its own folder:

```bash
cd fixture-scope
pytest
```

The GitHub Actions workflow (`.github/workflows/tests.yml`) runs each chapter's suite
separately on every push and pull request.
