"""Paddle for players"""
# Author: Liam Kelly
# Date: 2020

import pygame
COLOR_BLACK = (0, 0, 0)

# Paddle class derived from pygame sprite class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height, display_h):
        # Constructor of parent class
        super().__init__()

        # Make the paddle a surface with provided width and height
        self.image = pygame.Surface([width, height])

        # Set background color
        self.image.fill(COLOR_BLACK)
        self.image.set_colorkey(COLOR_BLACK)

        # Draw the padde object
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch rectangle object that has dimensions of the image
        self.rect = self.image.get_rect()
        
        # Capture screen height to make sure paddle stays fully on screen
        self.upper_boundary = display_h - height

    def move_up(self, pixels):
        self.rect.y -= pixels
        # Check for boundary
        if self.rect.y < 0:
            self.rect.y = 0
    
    def move_down(self, pixels):
        self.rect.y += pixels
        # Check for boundary
        if self.rect.y > self.upper_boundary:
            self.rect.y = self.upper_boundary
