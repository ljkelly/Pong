"""Class for pong ball"""
# Author: Liam Kelly
# Date: 2020

import pygame
from random import randint

# Color constants
COLOR_BLACK = (0, 0, 0)

# Velocity constants
X_VEL_MIN = 4
X_VEL_MAX = 8
Y_VEL_MIN = -8
Y_VEL_MAX = 8

# Class to represent the ball used for playing pong derived from pygame sprite
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Constructor of parent class
        super().__init__()

        # Make the paddle a surface with provided width and height
        self.image = pygame.Surface([width, height])

        # Set background color
        self.image.fill(COLOR_BLACK)
        self.image.set_colorkey(COLOR_BLACK)

        # Draw the ball object
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Instantiate a random velocity vector
        self.velocity = [randint(X_VEL_MIN, X_VEL_MAX), randint(Y_VEL_MIN, Y_VEL_MAX)]

        # Fetch rectangle object that has dimensions of the image
        self.rect = self.image.get_rect()
    
    # Update the position vector based on the velocity vector
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # Bounce method for when the ball collides with paddles
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(Y_VEL_MIN, Y_VEL_MAX)
