from trip import Trip

class Passenger:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def trips(self):
        matches = list(filter(lambda t: t._passenger == self, Trip._all))
        return matches

    def drivers(self):
        matches = list(filter(lambda t: t._passenger == self, Trip._all))
        driver_objs = list(map(lambda t: t._driver, matches))
        return driver_objs

    def trip_count(self):
        matches = list(filter(lambda t: t._passenger == self, Trip._all))
        return len(matches)
