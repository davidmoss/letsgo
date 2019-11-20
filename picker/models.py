from collections import namedtuple

Rejection = namedtuple('Rejection', ['person', 'reason'])


def clean_values(values):
    return set(map(lambda v: v.lower(), values))


class Venue:
    def __init__(self, name, food, drinks):
        self.name = name
        self.food = clean_values(food)
        self.drinks = clean_values(drinks)

    @classmethod
    def load(cls, venue):
        return cls(**venue)


class User:
    def __init__(self, name, wont_eat, drinks):
        self.name = name
        self.wont_eat = clean_values(wont_eat)
        self.drinks = clean_values(drinks)

    @classmethod
    def load(cls, user):
        return cls(**user)
