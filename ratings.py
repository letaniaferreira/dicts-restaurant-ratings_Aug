"""Restaurant rating lister."""

import sys


restaurants = {}


filename = sys.argv[1]
for line in open(filename):
    line = line.strip()
    words = line.split(":")
    restaurants[words[0]] = words[1]


for k in sorted(restaurants):
    restaurant_name = k
    restaurant_rating = restaurants[k]
    # print restaurant_name
    # print restaurant_rating
    print '{} is rated at {}'.format(restaurant_name, restaurant_rating)







