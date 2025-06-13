import json


class Booking:
    def __init__(self, **kwargs):
        self.bookingid = None
        self.firstname = 'Mary' if 'firstname' not in kwargs.keys() else kwargs['firstname']
        self.lastname = 'Smith' if 'lastname' not in kwargs.keys() else kwargs['lastname']
        self.totalprice = 937 if 'totalprice' not in kwargs.keys() else kwargs['totalprice']
        self.depositpaid = False if 'depositpaid' not in kwargs.keys() else kwargs['depositpaid']
        self.bookingdates = {"checkin": "2022-10-13", "checkout": "2023-04-10"} if 'bookingdates' not in kwargs.keys() \
            else kwargs['bookingdates']

    def update_data(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_json(self):
        return json.dumps(self.__dict__)

    def get_dikt(self):
        return self.__dict__
