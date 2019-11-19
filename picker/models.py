from collections import namedtuple

Rejection = namedtuple('Rejection', ['person', 'reason'])


class Venue:
    def __init__(self, name, food, drinks):
        self.name = name
        self.food = set(food)
        self.drinks = set(drinks)

    @classmethod
    def load(cls, venue):
        return cls(**venue)


class User:
    def __init__(self, name, wont_eat, drinks):
        self.name = name
        self.wont_eat = set(wont_eat)
        self.drinks = set(drinks)

    @classmethod
    def load(cls, user):
        return cls(**user)
