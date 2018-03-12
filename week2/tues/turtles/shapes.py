from turtle import *
def circle(size, fill, color):
    boo = fill
    if boo is True:
        fill(True)
        fillcolor(color)
    color(color)
    circle(size)

def square(size, fill, color):
    boo = fill
    if boo is True:
        fill(True)
        fillcolor(color)
    color(color)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)

def star(size, fill, color):
    boo = fill
    if boo is True:
        fill(True)
        fillcolor(color)
    color(color)
    forward(size)
    left(160)
    forward(size)
    left(160)
    forward(size)
    left(160)
    forward(size)
    left(160)
    forward(size)
    left(160)
    forward(size)
    left(160)
    forward(size)
    left(160)
    forward(size)
    left(160)
    forward(size)
    
def hexagon(size, fill, color):
    boo = fill
    if boo is True:
        fill(True)
        fillcolor(color)
    color(color)
    forward(size)
    left(60)
    forward(size)
    left(60)
    forward(size)
    left(60)
    forward(size)
    left(60)
    forward(size)
    left(60)
    forward(size)
    
def octogon(size, fill, color):
    boo = fill
    if boo is True:
        fill(True)
        fillcolor(color)
    color(color)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    left(45)
    forward(size)
    
def pentagon(size, fill, color):
    boo = fill
    if boo is True:
        fill(True)
        fillcolor(color)
    color(color)
    forward(size)
    left(72)
    forward(size)
    left(72)
    forward(size)
    left(72)
    forward(size)
    left(72)
    forward(size)

def triangle(size, fill, color):
    boo = fill
    if boo is True:
        fill(True)
        fillcolor(color)
    color(color)
    forward(size)
    left(120)
    forward(size)
    left(120)
    forward(size)