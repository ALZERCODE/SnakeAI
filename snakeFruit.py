import random

class SnakeFruit():

    def __init__(self, window) -> None:

        self.spawn = True
        self.window = window
        self.respawn()
        self.tolerance = 10
        
    def respawn(self):
        self.pos = [random.randrange(1, (self.window.width//10) * 10),
                    random.randrange(1, (self.window.height//10) * 10)
                    ]

    def isEatingFruit(self, head_pos):

        isX = self.pos[0] - self.tolerance < head_pos[0] < self.pos[0] + self.tolerance
        isY = self.pos[1] - self.tolerance < head_pos[1] < self.pos[1] + self.tolerance
        return isX and isY

