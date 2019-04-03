from display import *
from draw import *
from parser import *
from matrix import *
from random import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

#parse_file( 'script', edges, polygons, transform, screen, color )

p = [ "sphere","torus", "box", "scale", "move", "rotate" ]

with open("script0", "w") as f:
    script = ""
    prev = ""
    for i in range(10):
        if i%2 == 0:
            prev = p[randrange(len(p))]
            script += prev + "\n"
        else:
            if prev == "torus":
                script += str(randrange(500)) +" "+ str(randrange(500))  +" "+ str(randrange(500))  +" "+str(randrange(500)) +" "+ str(randrange(250))  + "\n"
            if prev == "circle" or prev == "sphere":
                script += str(randrange(500)) +" "+ str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(250))  + "\n"
            elif prev == "hermite" or prev == "bezier":
                script += str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(500))+ "\n"
            elif prev == "line" or prev == "box":
                script += str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(500)) +" "+ str(randrange(500))  + "\n"
            elif prev == "scale" or prev == "move":
                script += str(randrange(500))  +" "+ str(randrange(500))  +" "+ str(randrange(500))  + "\n"
            elif prev == "rotate":
                 script += "x" +" "+ str(randrange(10))  + "\nrotate\n" +  "y" +" "+ str(randrange(10))  + "\nrotate\n" +  "z" +" "+ str(randrange(10))  + "\n"
    script += "save\nimage.png"
    f.write(script)
    f.close

parse_file("script0", edges, polygons, transform, screen, color)

