
class User:
    def __init__(self, name):
        self.name = name
        self.phone = None

class Service:
    def __init__(self, name):
        self.name = name
        self.price = None

class Schedule:
    def __init__(self, name):
        self.worker_name = name
        self.date = None
        #
        #self.price = None

class Apointment:
    def __init__(self, user):
        self.user = user
        self.service = None
        self.service_name = None
        self.comments = None
        self.app_date = None
        self.app_time = None
        self.app_id = None

user_dict = {}
services_dict = {}
apps_dict = {}