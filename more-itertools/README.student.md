# more-itertools — course notes

This folder is the open-source [`more-itertools`](https://github.com/more-itertools/more-itertools) library, vendored as-is and used as a "sandbox" to practice writing tests against a real third-party library. The original `README.rst` and the rest of the code **are not course material** and should not be modified.

The only file authored for the course is `tests/test_custom.py`.

## What `tests/test_custom.py` demonstrates
- `test_partition*`: tests `more_itertools.partition`, which splits an iterable into two lists based on a predicate (including the `None`-predicate case and an empty iterable).
- `test_interleave*`: tests `more_itertools.interleave`, which combines several iterables by interleaving their elements (including lists of different lengths).

## How to run it
```
pip install -e .
pip install pytest
```
Then, from this folder:
```
pytest tests/test_custom.py
```
