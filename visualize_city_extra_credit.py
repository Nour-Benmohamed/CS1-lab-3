# Author: Nour Benmohamed
# 11/05/2017
# program to visualize the 50 most populous cities in the world
# This visualization will draw a circle in the location of each city with a diameter proportional to its population
# in random colors


from sort_cities import*
from cs1lib import*
from quicksort import*
from random import*

WIDTH = 720
HEIGHT = 360
img = load_image("world.png")
sort(list_cities, compare_population)
i = 0
test = False
in_file.close()


def draw():
    global i, test
    img = load_image("world.png")
    if not test:
        draw_image(img, 0, 0)
        test = True
    set_fill_color(uniform(0,1), uniform(0,1), uniform(0,1))
    if i < 51:
        x= list_cities[i].longitude*2+WIDTH/2
        y= -list_cities[i].latitude*2+HEIGHT/2
        draw_circle(x, y, list_cities[i].population / 1000000)
        i += 1


start_graphics(draw, width=720, height=360, framerate=5)