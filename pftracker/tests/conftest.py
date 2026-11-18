from decimal import Decimal

import pytest

from pftracker import JsonFileStorage, PersonalFinanceTracker


@pytest.fixture
def json_storage_path(tmp_path):
    storage_path = tmp_path / "finance.json"
    return storage_path


@pytest.fixture
def storage(json_storage_path):
    s = JsonFileStorage(json_storage_path)
    yield s
    s.close()


@pytest.fixture
def tracker(storage, mocker):
    exchange = mocker.Mock()
    exchange.get_rate.return_value = Decimal("0.9")

    with PersonalFinanceTracker(
        storage=storage,
        exchange_provider=exchange,
    ) as t:
        yield t


@pytest.fixture
def clean_db():
    """Placeholder fixture required by pytest.ini's `usefixtures`; no-op for now."""