import pygame
import random

class SnakeFruit():

    def __init__(self, window) -> None:

        self.spawn = True
        self.window = window
        self.respawn()
        
    def respawn(self):
        self.pos = [random.randrange(1, (self.window.width//10) * 10),
                    random.randrange(1, (self.window.height//10) * 10)
                    ]