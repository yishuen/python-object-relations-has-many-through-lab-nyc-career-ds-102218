from driver import Driver
daniel = Driver("Daniel", "fast and furious")
alice = Driver("Alice", "faster and furiouser")
jeff = Driver("Jeff", "defensive")

from passenger import Passenger
jake = Passenger("Jake", 29)
anna = Passenger("Anna", 25)
katie = Passenger("Katie", 20)

from trip import Trip
trip_one = Trip(daniel, jake)
trip_two = Trip(alice, anna)
trip_three = Trip(jeff, katie)
trip_four = Trip(daniel, katie)

print(daniel.trips())
print(katie.trips())
print(daniel.passengers())
print(katie.drivers())
print(daniel.trip_count())
print(katie.trip_count())
