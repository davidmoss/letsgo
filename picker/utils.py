import json
from collections import defaultdict

from .models import Rejection, User, Venue


def check_venue(venue, person):
    reason = ""
    matching_foods = venue.food - person.wont_eat
    matching_drinks = person.drinks & venue.drinks
    if not matching_drinks or not matching_foods:
        if not matching_foods:
            foods = sorted(venue.food & person.wont_eat)
            reason = f"doesn't eat {', '.join(foods)}"
        if not matching_drinks:
            reason = f"{reason} or" if reason else "doesn't"
            drinks = sorted(venue.drinks - person.drinks)
            reason += f" drink {', '.join(drinks)}"
    return reason


def filter_venues(venues, people):
    selected = []
    rejects = defaultdict(list)

    for key, venue in enumerate(venues):
        rejected = False
        for person in people:
            reason = check_venue(venue, person)
            if reason:
                # Assuming the venue names are unique
                rejects[venue.name].append(Rejection(person, reason))
                rejected = True

        if not rejected:
            selected.append(venue)

    return selected, rejects


def process_file(filepath, Member):
    instances = []
    with open(filepath) as f:
        objects = json.load(f)
        for object in objects:
            instances.append(Member.load(object))
    return instances


def process_users(filepath):
    return process_file(filepath, User)


def process_venues(filepath):
    return process_file(filepath, Venue)
