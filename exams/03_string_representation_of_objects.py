"""
Implement two vehicle classes:
    - Car and Boat
"""


class Car:
    def __init__(self, maximum_speed, notation_units):
        self.maximum_speed = maximum_speed
        self.notation_units = notation_units

    def __str__(self):
        return (
            f"Car with the maximum speed of {self.maximum_speed} {self.notation_units}"
        )


class Boat:
    def __init__(self, maximum_speed):
        self.maximum_speed = maximum_speed

    def __str__(self):
        return f"Boat with the maximum speed of {self.maximum_speed} knots"


if __name__ == "__main__":
    my_bot = Boat(82)
    print(my_bot)

    my_car = Car(122, "mhp")
    print(my_car)
