"""Restaurant rating lister."""

import sys


restaurants = {}

def import_and_split():

    restaurants = {}

    filename = sys.argv[1]
    for line in open(filename):
        line = line.strip()
        words = line.split(":")
        restaurants[words[0]] = words[1]

    return restaurants


def sorting_restaurants(dict):

    for name_of_restaurant in sorted(restaurants):
        return '{} is rated at {}.'.format(name_of_restaurant, restaurants[name_of_restaurant])


sorting_restaurants(restaurants)


