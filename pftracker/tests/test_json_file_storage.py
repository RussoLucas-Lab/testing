from pathlib import Path

import pytest

from pftracker import JsonFileStorage


@pytest.fixture
def fixed_pid(mocker):
    mocker.patch("os.getpid", return_value=12345)


@pytest.mark.usefixtures("fixed_pid")
def test_lockfile_contains_pid(tmp_path):
    storage_path = tmp_path / "state.json"
    with JsonFileStorage(storage_path):
        pid = Path(str(storage_path) + ".lock").read_text().strip()
        assert pid == "12345"
