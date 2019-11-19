from picker.models import User, Venue
from picker.utils import (check_venue, filter_venues, process_users,
                          process_venues)


def test_check_full_venue():
    reason = check_venue(
        venue=Venue('Venue2', ['chips'], ['wine']),
        person=User('User1', ['chips'], ['water']),
    )
    assert reason == "doesn't eat chips or drink wine"


def test_check_drinks_venue():
    reason = check_venue(
        venue=Venue('Venue2', ['chinese'], ['wine', 'coke']),
        person=User('User1', ['chips'], ['water']),
    )
    assert reason == "doesn't drink coke, wine"


def test_check_food_venue():
    reason = check_venue(
        venue=Venue('Venue2', ['chips'], ['water', 'wine']),
        person=User('User1', ['chips'], ['water']),
    )
    assert reason == "doesn't eat chips"


def test_filter_venues():
    venues = [
        Venue('Venue1', ['steak'], ['water']),
        Venue('Venue2', ['chinese'], ['wine']),
    ]
    people = [
        User('User1', ['chips'], ['water']),
        User('User2', ['chips'], ['wine', 'water']),
    ]
    selected, rejected = filter_venues(venues, people)
    assert selected[0].name == 'Venue1'
    assert 'Venue2' in rejected
    assert rejected['Venue2'][0].person.name == 'User1'


def test_process_venues():
    venues = process_venues('./data/venues.json')
    assert venues and len(venues) > 1
    assert venues[0].name and venues[0].food and venues[0].drinks


def test_process_users():
    users = process_users('./data/users.json')
    assert users and len(users) > 1
    assert users[0].name and users[0].wont_eat and users[0].drinks


def test_load_user():
    json_user = {
        'name': 'Test User',
        'wont_eat': ['lemons'],
        'drinks': ['milk'],
    }
    user = User.load(json_user)
    assert user.name == 'Test User'
    assert 'lemons' in user.wont_eat
    assert 'milk' in user.drinks


def test_load_venue():
    json_venue = {
        'name': 'Test Venue',
        'food': ['hummous'],
        'drinks': ['milk'],
    }
    venue = Venue.load(json_venue)
    assert venue.name == 'Test Venue'
    assert 'hummous' in venue.food
    assert 'milk' in venue.drinks
