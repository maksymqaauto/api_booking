from http import HTTPStatus
import pytest
from api_collections.booking_api import BookingApi
from api_collections.data_classes.booking_data import Booking
import allure


@allure.feature('Get Booking')
@pytest.mark.smoke
@pytest.mark.regression
def test_get_api(env, create_mock_booking):
    booking_api = BookingApi(env)
    response = booking_api.get_booking_by_id(booking_id=1)
    actual_booking = Booking(**response.json())
    assert response.status_code == HTTPStatus.OK
    assert create_mock_booking.get_dikt() == actual_booking.get_dikt()


@allure.feature('IDs range')
@pytest.mark.regression
def test_get_ids_by_date_range(env, get_full_booking_range):
    date_from, date_to = get_full_booking_range
    booking_api = BookingApi(env)
    response = booking_api.get_bookings_by_date_range(date_from, date_to)
    assert response.status_code == HTTPStatus.OK
    dates_range = response.json()
    assert len(dates_range) > 100


@allure.feature('Create Booking')
@pytest.mark.smoke
@pytest.mark.regression
def test_create_booking(env, create_mock_booking):
    booking_api = BookingApi(env)
    response = booking_api.create_booking(create_mock_booking)
    assert response.status_code == HTTPStatus.OK


@allure.feature('Update Booking')
@pytest.mark.smoke
@pytest.mark.regression
def test_update_booking(env, create_mock_booking):
    booking_api = BookingApi(env)
    updated_booking_data = {"totalprice": 600}
    response = booking_api.update_booking(create_mock_booking.bookingid, updated_booking_data)
    assert response.status_code in [HTTPStatus.OK, HTTPStatus.FORBIDDEN]
    if response.status_code != HTTPStatus.OK:
        pytest.skip(f"Update not allowed, status code: {response.status_code}")
    updated_booking_response = booking_api.get_booking_by_id(create_mock_booking.bookingid)
    assert updated_booking_response.status_code == HTTPStatus.OK, \
        f"Failed to fetch updated booking. Status: {updated_booking_response.status_code}"
    updated_booking = Booking(**updated_booking_response.json())
    assert updated_booking.totalprice == updated_booking_data["totalprice"]


@allure.feature('Delete Booking')
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_booking(env, create_mock_booking):
    booking_api = BookingApi(env)
    booking_id = create_mock_booking.bookingid
    response = booking_api.delete_booking(booking_id)
    assert response.status_code == HTTPStatus.NO_CONTENT or HTTPStatus.FORBIDDEN
    deleted_booking_response = booking_api.get_booking_by_id(booking_id)
    assert deleted_booking_response.status_code == HTTPStatus.NOT_FOUND


@allure.feature('Patch Booking')
@pytest.mark.smoke
@pytest.mark.regression
def test_patch_booking(env, create_mock_booking):
    booking_api = BookingApi(env)
    updated_booking_data = {"totalprice": 600}
    response = booking_api.patch_booking(create_mock_booking.bookingid, updated_booking_data)
    if response.status_code == HTTPStatus.FORBIDDEN:
        pytest.skip(f"Patch not allowed, status code: {response.status_code}")
    else:
        assert response.status_code == HTTPStatus.OK
    updated_booking_response = booking_api.get_booking_by_id(create_mock_booking.bookingid)
    updated_booking = Booking(**updated_booking_response.json())
    assert updated_booking.totalprice == updated_booking_data["totalprice"]


@allure.feature('Custom Deletion')
@pytest.mark.regression
def test_delete_non_existent_booking(env):
    booking_api = BookingApi(env)
    non_existent_booking_id = 99999
    response = booking_api.delete_booking(non_existent_booking_id)
    assert response.status_code == HTTPStatus.NOT_FOUND or HTTPStatus.FORBIDDEN


@allure.feature('Change Incorrect ID')
@pytest.mark.regression
def test_patch_booking_invalid_id(env):
    booking_api = BookingApi(env)
    invalid_booking_id = "invalid_id"
    updated_booking_data = {"totalprice": 700}
    response = booking_api.patch_booking(invalid_booking_id, updated_booking_data)
    assert response.status_code == HTTPStatus.NOT_FOUND or HTTPStatus.FORBIDDEN


@allure.feature('Update Incorrect ID')
@pytest.mark.regression
def test_update_booking_invalid_id(env):
    booking_api = BookingApi(env)
    invalid_booking_id = "invalid_id"
    updated_booking_data = {"totalprice": 700}
    response = booking_api.update_booking(invalid_booking_id, updated_booking_data)
    assert response.status_code == HTTPStatus.NOT_FOUND or HTTPStatus.FORBIDDEN


@allure.feature('Get Incorrect ID')
@pytest.mark.regression
def test_get_booking_invalid_id(env):
    booking_api = BookingApi(env)
    invalid_booking_id = "invalid_id"
    response = booking_api.get_booking_by_id(invalid_booking_id)
    assert response.status_code == HTTPStatus.NOT_FOUND


@allure.feature('Get All Bookings')
@pytest.mark.smoke
@pytest.mark.regression
def test_get_all_bookings(env):
    booking_api = BookingApi(env)
    response = booking_api.get('/booking')
    assert response.status_code == HTTPStatus.OK
    bookings = response.json()
    assert len(bookings) >= 1
