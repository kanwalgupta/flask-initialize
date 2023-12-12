class Passenger:
    attrs = ['id', 'first_name', 'last_name', 'gender', 'age' ]
    def __init__(self, values):
        self.__dict__ = dict(zip(self.attrs, values))