from utilities.api_utilities.base_api import BaseApi
import allure


class BookingApi(BaseApi):
    def __init__(self, env):
        super().__init__(env)
        self.__booking_url = '/booking'

    @allure.step
    def get_booking_by_id(self, booking_id, headers=None):
        response = self.get(f'{self.__booking_url}/{booking_id}', headers=headers)
        return response

    @allure.step
    def get_bookings_by_date_range(self, date_from, date_to):
        params = {
            "from": date_from,
            "to": date_to
        }
        response = self.get(f'{self.__booking_url}', params=params)
        return response

    @allure.step
    def create_booking(self, booking, headers=None):
        response = self.post(self.__booking_url, booking.get_dikt(), headers=headers)
        return response

    @allure.step
    def update_booking(self, booking_id, updated_data, headers=None):
        response = self.put(f'{self.__booking_url}/{booking_id}', updated_data, headers=headers)
        return response

    @allure.step
    def delete_booking(self, booking_id, headers=None):
        response = self.delete(f'{self.__booking_url}/{booking_id}', headers=headers)
        return response

    @allure.step
    def patch_booking(self, booking_id, updated_data, headers=None):
        response = self.patch(f'{self.__booking_url}/{booking_id}', updated_data, headers=headers)
        return response
