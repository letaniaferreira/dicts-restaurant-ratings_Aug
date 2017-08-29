"""Restaurant rating lister."""

import sys


def import_and_split():

    restaurants = {}

    filename = sys.argv[1]
    for line in open(filename):
        line = line.strip()
        words = line.split(":")
        restaurants[words[0]] = words[1]

    return restaurants


def add_rating(restaurants):

    new_restaurant = raw_input("Please enter a restaurant name! ")
    new_score = raw_input("What rating would you like to give this restaurant? ")
    new_restaurant = new_restaurant.capitalize()
    restaurants[new_restaurant] = new_score


def sorting_restaurants(restaurants):

    for name_of_restaurant in sorted(restaurants):
        print '{} is rated at {}.'.format(name_of_restaurant, restaurants[name_of_restaurant])


restaurant_rating = import_and_split()
add_rating(restaurant_rating)
sorting_restaurants(restaurant_rating)


