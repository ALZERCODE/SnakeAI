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

        
    
    def main(self, direction = None, render=True):
        # Main Function

        if not direction:
            direction = self.get_key()
        self.snake.move_snake(direction, 10)

        self.snake.grow_body()

        if self.fruit.isEatingFruit(self.snake.head_pos):
            self.score += 100
            self.fruit.spawn = False
        else:
            self.snake.ungrow_body()

        if not self.fruit.spawn:
                self.fruit.respawn()

        self.fruit.spawn = True
        
    
        # Game Over conditions
        if self.snake.head_pos[0] < 0 or self.snake.head_pos[0] > self.window.width-10:
            if not render:
                self.score -= 500
                return self.score, True
            self.game_over()

            
        if self.snake.head_pos[1] < 0 or self.snake.head_pos[1] > self.window.width-10:
            if not render:
                self.score -= 500
                return self.score, True
            self.game_over()
        
        # Touching the snake body
        for block in self.snake.body[1:]:
            if self.snake.head_pos[0] == block[0] and self.snake.head_pos[1] == block[1]:
                if not render:
                    self.score -= 500
                    return self.score, True
                self.game_over()
        
        if render:
            self.render()
    
        # Frame Per Second /Refresh Rate
        self.fps.tick(self.snake.speed)

        self.score += 1
        return self.score, False
    
    def render(self):
        self.window.reset()
        
        self.snake.render(self.window)
        self.window.renderBox(self.window.WHITE, self.fruit.pos)

        # displaying score countinuously
        self.window.show_score(self.window.WHITE, self.window.SMALL_FONT, self.score)
        
        self.window.refresh()



    # game over function
    def game_over(self):
        self.window.show_final_score(self.score)
        
        time.sleep(2)
        pygame.quit()
        quit()

    def get_key(self):

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
        if self.change_to == 'UP' and self.snake.direction != 'DOWN':
            self.snake.direction = 'UP'
        if self.change_to == 'DOWN' and self.snake.direction != 'UP':
            self.snake.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.snake.direction != 'RIGHT':
            self.snake.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.snake.direction != 'LEFT':
            self.snake.direction = 'RIGHT'

        return self.snake.direction

    
if __name__ == "__main__":
    game = SnakeGame()
    while True:
        game.main()