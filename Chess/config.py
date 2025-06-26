import pygame as py
path = "Pixel_Art_Chess_DevilsWorkshop_V04/chess/"
FPS = 60
fwidth = 750
fheight = 600
py.init()
py.mixer.init()
screen = py.display.set_mode((fwidth, fheight))
class Unit:
    x = 92
    y = 73

unit = Unit()

def pos():
    var = py.mouse.get_pos()
    x = var[0] / unit.x
    y = var[1] / unit.y
    return int(x), int(y)

def normalize(num):
    if num:
        if num < 0:
            return -1
        else:
            return 1
    else:
        return 0

def opposite(color):
    if color == "black":
        return "white"
    else:
        return "black"

def helper(color):
    if color == "black":
        return 0
    else:
        return 1

def toggle(value):
    return not value