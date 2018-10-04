# Author: Nour Benmohamed
# 11/05/2017
# program to sort cities according to 3 different criterion

from quicksort import*
from City import City

in_file = open("world_cities.txt", "r")
list_cities = []

# This loop will first strip every line in the file, split it turning it into a list, then it will convert the
# 3rd, 4th and 5th element into the appropriate variables, and finally it will append each element into a bigger
# list of lists of cities

for line in in_file:
    line = line.strip()
    line = line.split(",")
    line[3] = int(line[3])
    line[4] = float(line[4])
    line[5] = float(line[5])
    line = City(line[0], line[1], line[2], line[3], line[4], line[5])
    list_cities.append(line)


def compare_name(a, b):
    return a.name.lower() <= b.name.lower()


def compare_population(a, b):
    return a.population >= b.population


def compare_latitude(a, b):
    return a.latitude <= b.latitude


sort(list_cities, compare_name)
out_file = open("cities_alpha.txt", "w")
for line in list_cities:
    string = line.__str__()
    out_file.write(string+"\n")
in_file.close()

sort(list_cities, compare_population)
out_file = open("cities_population.txt", "w")
for line in list_cities:
    string = line.__str__()
    out_file.write(string+"\n")
in_file.close()

sort(list_cities, compare_latitude)
out_file = open("cities_latitude.txt", "w")
for line in list_cities:
    string = line.__str__()
    out_file.write(string+"\n")
in_file.close()
