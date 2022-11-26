import sys
import pygame
from pygame import mouse 

# some values still have to be defined: colors and item locations 
def welcome_screen(screen, diff): 
    #initialize fonts 
    title_font = pygame.font.Font('freesansbold.ttf', 32)
    sub_title_font = pygame.font.Font('freesansbold.ttf', 16)  
    button_font = pygame.font.Font('freesansbold.ttf', 16)
    
    # fill screen, unfinished have to define screen
    screen.fill(bg_color)   

    # create title
    title = title_font.render('Welcome to Sudoku', True, black, bg_color)  
    title_rectangle = title.get_rect(center=(WIDTH // 2, (HEIGHT/2) // 2 - 50)) 
    screen.blit(title, title_rectangle)
    
    # create subtitle
    sub_title = sub_title_font.render('Please select a difficulty', True, black, bg_color) 
    sub_title_rectangle = sub_title.get_rect(center = (WIDTH // 2, (HEIGHT/2) // 2)) 
    screen.blit(sub_title, sub_title_rectangle)  

    # difficulty texts
    easy_mode_text = button_font.render('Easy', True, black, white) 
    medium_mode_text = button_font.render('Medium', True, black, white) 
    hard_mode_text = button_font.render('Hard', True, black, white) 

    # easy mode rectangle size
    easy_mode_surface = pygame.Surface((easy_mode_text.get_size()[0]+20, easy_mode_text.get_size()[1]+20)) 
    easy_mode_surface.fill(LINE_COLOR) 
    easy_mode_surface.blit(easy_mode_text,(10,10))  

    # medium mode rectangle size
    medium_mode_surface = pygame.Surface((medium_mode_text.get_size()[0]+20, medium_mode_text.get_size()[1]+20)) 
    medium_mode_surface.fill(LINE_COLOR) 
    medium_mode_surface.blit(medium_mode_text,(10,10))  

    # hard mode rectangle size
    hard_mode_surface = pygame.Surface((hard_mode_text.get_size()[0]+20, hard_mode_text.get_size()[1]+20)) 
    hard_mode_surface.fill(LINE_COLOR) 
    hard_mode_surface.blit(hard_mode_text,(10,10)) 

    # button rectangles
    easy_rectangle = easy_mode_surface.get_rect(center = (WIDTH // 2, ((HEIGHT/2)+100) // 2)) 
    medium_rectangle = medium_mode_surface.get_rect(center = (WIDTH // 2, ((HEIGHT/2)+200) // 2)) 
    hard_rectangle = hard_mode_surface.get_rect(center = (WIDTH // 2, ((HEIGHT/2)+300) // 2)) 

    # draws difficulty buttons 
    screen.blit(easy_mode_surface, easy_rectangle) 
    screen.blit(medium_mode_surface, medium_rectangle) 
    screen.blit(hard_mode_surface, hard_rectangle) 

    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if easy_rectangle.collidepoint(event.pos): 
                    diff = "easy"
                    return diff
                elif medium_rectangle.collidepoint(event.pos): 
                    diff = "medium"
                    return diff
                elif hard_rectangle.collidepoint(event.pos): 
                    diff = "hard"
                    return diff
        pygame.display.update()     

if __name__ == "__main__": 
    pygame.init() 
    WIDTH = 500 
    HEIGHT = 500 
    black = (0,0,0)  
    white = (255,255,255)
    bg_color = (234, 212, 252) 
    LINE_COLOR = (255, 255, 255)  
    diff = None
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("Sudoku") 
    difficulty_level = welcome_screen(screen, diff) 
    






