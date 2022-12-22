from snakeFruit import SnakeFruit
from snakeWindow import SnakeWindow
from snakeSnake import Snake

import pygame
import time

class SnakeGame():

    def __init__(self) -> None:
        pygame.init()

        self.window = SnakeWindow()
        self.fruit = SnakeFruit(self.window)
        self.snake = Snake()

        self.fps = pygame.time.Clock()
        self.score = 0

        self.change_to = self.snake.direction

        
    
    def main(self):
        # Main Function
        while True:
        
            direction = self.get_key()
            self.snake.move_snake(direction, 10)

            if self.snake.head_pos[0] == self.fruit.pos[0] and self.snake.head_pos[1] == self.fruit.pos[1]:
                self.score += 10
                self.fruit.spawn = False
                self.snake.grow_body()

            if not self.fruit.spawn:
                    self.fruit.respawn()

            self.fruit.spawn = True
                
            self.window.reset()
            
            self.snake.render(self.window)

            self.window.renderBox(self.window.WHITE, self.fruit.pos)
        
            # Game Over conditions
            if self.snake.head_pos[0] < 0 or self.snake.head_pos[0] > self.window.width-10:
                self.game_over()
            if self.snake.head_pos[1] < 0 or self.snake.head_pos[1] > self.window.width-10:
                self.game_over()
            
            # Touching the snake body
            for block in self.snake.body[1:]:
                if self.snake.head_pos[0] == block[0] and self.snake.head_pos[1] == block[1]:
                    self.game_over()
            
            # displaying score countinuously
            self.window.show_score(self.window.WHITE, self.window.SMALL_FONT, self.score)
            
            self.window.refresh()
        
            # Frame Per Second /Refresh Rate
            self.fps.tick(self.snake.speed)

    # game over function
    def game_over(self):
        self.window.show_final_score(self.score)
        
        time.sleep(2)
        pygame.quit()
        quit()

    def get_key(self):
        direction = self.snake.direction

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    self.change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    self.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    self.change_to = 'RIGHT'
    
        # If two keys pressed simultaneously
        # we don't want snake to move into two directions
        # simultaneously
        if self.change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if self.change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if self.change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if self.change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
    
        return direction

    
if __name__ == "__main__":
    game = SnakeGame()
    game.main()