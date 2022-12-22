import pygame

class Snake():

    def __init__(self) -> None:
        self.speed = 15
        self.head_pos = [100, 50]
        self.body = [  [100, 50],
                        [90, 50],
                        [80, 50],
                        [70, 50],
                        ]

        self.direction = 'RIGHT'
    
    def grow_body(self):
        self.body.insert(0, list(self.head_pos))

    def move_snake(self, direction, speed):
        # Moving the snake
        if direction == 'UP':
            self.head_pos[1] -= speed
        if direction == 'DOWN':
            self.head_pos[1] += speed
        if direction == 'LEFT':
            self.head_pos[0] -= speed
        if direction == 'RIGHT':
            self.head_pos[0] += speed
    
    def render(self, window):
        for pos in self.body:
            window.renderBox(window.GREEN, pos)