# remeber to import the Trip class here
from trip import Trip

class Driver:

    def __init__(self, name, driving_style):
        self._name = name
        self._driving_style = driving_style

    @property
    def name(self):
        return self._name

    # @property.setter
    # def set_name(self, name):
    #     self._name = name

    @property
    def driving_style(self):
        return self._driving_style

    # @property.setter
    # def set_driving_style(self, driving_style):
    #     self._driving_style = driving_style

    def trips(self):
        matches = list(filter(lambda t: t._driver == self, Trip._all))
        return matches

    def passengers(self):
        matches = list(filter(lambda t: t._driver == self, Trip._all))
        passenger_objs = list(map(lambda t: t._passenger, matches))
        return passenger_objs

    def trip_count(self):
        matches = list(filter(lambda t: t._driver == self, Trip._all))
        return len(matches)
