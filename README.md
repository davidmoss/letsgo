# Lets go!
The quick and easy restaurant picker given your teams food and drink requirements!

## Design
Started off with the standard basic Django project rather than the more
complicated production ready cookie cutter, which gives us too much for what we
really need in this situation.

Main objects are People, Restaurants, Food and Drink. This can be modelled in a
relational database (sqllite) and use joins to calculate the intersections of
the requirements.

Again for simplicity it is just as easy to iterate through the restaurants and
check that whether they match the requirements of the chosen participants, and
thus build up a list of rejects and their reasons.

## Setup
Initialise your virtual environment and install dependencies:
```
$ pipenv install
$ pipenv shell
```

## Usage
To run the application on http://localhost:8000:
```
$ ./manage.py runserver
```

## Tests
To run the tests:
```
$ pytest
```

## TODO
- Handle errors in json file, bad input, etc.
- Connect up database models
- Management command to load in JSON data
- Add admin area to manage venues and users
- Pretty up the UI
- Add API and React frontend
- Structure app for production and settings
