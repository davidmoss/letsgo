import json
from collections import defaultdict

from .models import Rejection, User, Venue


def check_venue(venue, user):
    """
    Check whether any of the venues food or drink matches the
    users requirements

    Paramters:
    venue (Venue): The Venue to check
    user (User): The User to check the criteria of

    Returns:
    str: The reason why the user can't go to the venue if applicable. The
         string is empty if the user matches the criteria.
    """
    reason = ""
    # Assumption is that they don't have to eat everything that a venue serves
    # - check venue has something they can eat
    # - check venue has seemthing they can drink
    matching_foods = venue.food - user.wont_eat
    matching_drinks = user.drinks & venue.drinks

    if not matching_drinks or not matching_foods:
        # Work out what food the user didn't like
        if not matching_foods:
            foods = sorted(venue.food & user.wont_eat)
            reason = f"doesn't eat {', '.join(foods)}"
        # Work out what drinks the user didn't like
        if not matching_drinks:
            reason = f"{reason} or" if reason else "doesn't"
            drinks = sorted(venue.drinks - user.drinks)
            reason += f" drink {', '.join(drinks)}"
    return reason


def filter_venues(venues, users):
    """
    Checks what venues match the users eating and drinking criteria

    Paramters:
    venues (list): The list of Venue objects
    users (list): The list of User objects to check

    Returns:
    tuple: Containing a list of the applicable Venues and a dict of venue name
           and a list of users who don't fit the criteria with their reasons
    """
    selected = []
    rejects = defaultdict(list)

    for venue in venues:
        rejected = False
        for user in users:
            reason = check_venue(venue, user)
            if reason:
                # Assuming the venue names are unique
                rejects[venue.name].append(Rejection(user, reason))
                rejected = True

        if not rejected:
            selected.append(venue)

    return selected, rejects


def process_file(filepath, Member):
    """
    Reads in a json file and populates the member instances

    Parameters:
    filepath (str): The path to the json file
    Member (object): The type of object to instaniate

    Returns:
    list: Of objects populated from the json file
    """
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
