import json
import os
from pathlib import Path
import pytest
from api_collections.booking_api import BookingApi
from api_collections.data_classes.booking_data import Booking
from utilities.config_obj import ConfigObject
from datetime import date


@pytest.fixture(scope='session', autouse=True)
def env():
    config_path = Path(__file__).parent / 'configurations' / 'env1.json'
    if not config_path.exists():
        raise FileNotFoundError(f"env1.json not found at: {config_path}")

    with config_path.open(encoding='utf-8') as file:
        data = json.load(file)

    return ConfigObject(**data)




@pytest.fixture()
def create_mock_booking(env):
    mock_data = BookingApi(env).get_booking_by_id(1)
    booking = Booking(**mock_data.json())
    return booking


@pytest.fixture()
def get_full_booking_range():
    return "2016-01-01", date.today().isoformat()
