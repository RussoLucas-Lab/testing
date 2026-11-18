# Document Editor

## Concept
Introductory chapter on unit testing with pytest: basic asserts, `pytest.raises` for exceptions, and `pytest.mark.xfail` to document a known bug without breaking the suite.

## What the code demonstrates
- `src/main.py`: `DocumentEditor` class with `write`, `clear`, `is_empty`, and `get_last_content`. It has an intentional bug: `history.append(self.content)` runs *before* `content` is updated, so `get_last_content()` always returns the content from before the last `write`.
- `tests/test_main.py`: covers the class's normal cases and uses `@pytest.mark.xfail` on `test_get_last_content` to record the bug without failing the pipeline, plus `pytest.raises` for the empty-history case.

## How to run it
No external dependencies, just pytest:
```
pip install -r requirements.txt
```
Then, from this folder:
```
pytest
```
