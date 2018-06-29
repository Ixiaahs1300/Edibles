import pygame
from pygame import Rect

# A class representing an "Entity" within the game. It is represented by an x and y value representing position in the
# 2D space of the game window, a width and height value representing the size of the entity, and a color tuple value
# representing the color of the Entity.

class Entity:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    # Returns a Rect object created from the Entity's properties
    def rect(self):
        return Rect(self.x, self.y, self.width, self.height)

    # Draws the Entity to the screen. Takes in a Surface/screen to draw to as a parameter
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect())

# Rounds the number to a multiple of the base
def myround(x, base=5):
    return int(base * round(float(x)/base))
