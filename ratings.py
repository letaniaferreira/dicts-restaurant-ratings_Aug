"""Restaurant rating lister."""

import sys


restaurants = {}


filename = sys.argv[1]
for line in open(filename):
    line = line.strip()
    words = line.split(":")
    restaurants[words[0]] = words[1]


for name_of_restaurant in sorted(restaurants):
    print '{} is rated at {}.'.format(name_of_restaurant, restaurants[name_of_restaurant])







