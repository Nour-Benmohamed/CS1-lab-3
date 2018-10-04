# Author: Nour Benmohamed
# 11/5/2017


class City:
    def __init__(self, code, name, region, population, latitude, longitude):
        self.country_code = code
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude

# This method will return the string with the name, population, latitude and longitude of each object

    def __str__(self):
        return str(self.name)+","+str(self.population)+","+str(self.latitude)+","+str(self.longitude)
