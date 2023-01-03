import random
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
    def ungrow_body(self):
        self.body.pop()

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
        
    def randomPos(self, window):
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

        offset = len(self.body)*10
        x = random.randint(0+offset, window.width - offset)
        y = random.randint(0+offset, window.height - offset)

        self.head_pos = [x, y]

        x_offset = 0
        y_offset = 0

        if self.direction == 'RIGHT':
            x_offset = -10
        elif self.direction == 'LEFT':
            x_offset = 10
        elif self.direction == 'UP':
            y_offset = 10
        elif self.direction == 'DOWN':
            y_offset = -10
        
        self.body = []
        for i in range(int(offset/10)):
            self.body.append([x + i*x_offset, y + i*y_offset])



    def get_free_space(self, window):
        pos = self.head_pos
        pos_surround = [
                [pos[0]+11, pos[1]],
                [pos[0], pos[1]+11],
                [pos[0]-11, pos[1]],
                [pos[0], pos[1]-11],
                ]

        free_space = []
        for c in pos_surround:
            x = self._isBody(c) or self._isWall(c, window)
            free_space.append(int(not x))
        
        return free_space
    
    def _isBody(self, coordinates):
        for c in self.body:
            
            x = c[0] - 5 < coordinates[0] < c[0] + 5
            y = c[1] - 5 < coordinates[1] < c[1] + 5

            is_c = (x and y)

            if is_c:
                break
        
        return is_c

        

    def _isWall(self, coordinates, window):
        x = 0 > coordinates[0] or coordinates[0] > window.width 
        y = 0 > coordinates[1] or coordinates[1] > window.height 
        return x or y
