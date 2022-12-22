import pygame

class SnakeWindow():

    def __init__(self) -> None:
        self.width = 720
        self.height = 480  

        self.colors()  
        self.SMALL_FONT = pygame.font.SysFont('times new roman', 20)
        self.BIG_FONT = pygame.font.SysFont('times new roman', 50)

        pygame.display.set_caption('Alzercode Snake from GeeksforGeeks')
        self.window = pygame.display.set_mode((self.width, self.height)) 
    
    def reset(self):
        self.window.fill(self.BLACK)
    
    def refresh(self):
        pygame.display.update()
    
    def renderBox(self, color, pos):
        pygame.draw.rect(self.window, color, pygame.Rect(
            pos[0], pos[1], 10, 10))

    def show_score(self, color, score_font, score):
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        self.window.blit(score_surface, score_rect)

    def show_final_score(self, score):
        # creating a text surface on which text
        # will be drawn
        game_over_surface = self.BIG_FONT.render('Your Score is : ' + str(score), True, self.RED)
        
        # create a rectangular object for the text
        # surface object
        game_over_rect = game_over_surface.get_rect()
        
        # setting position of the text
        game_over_rect.midtop = (self.width/2, self.height/4)
        
        # blit will draw the text on screen
        self.window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
    
    def colors(self):
        self.BLACK = pygame.Color(0, 0, 0)
        self.WHITE = pygame.Color(255, 255, 255)
        self.RED = pygame.Color(255, 0, 0)
        self.GREEN = pygame.Color(0, 255, 0)
        self.BLUE = pygame.Color(0, 0, 255)