import pygame
from pygame import mouse

pygame.init()
bg_color = (234, 212, 252)

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Sudoku")

pygame.display.flip()

white = (255, 255, 255)
black = (0, 0, 0)

X = 500
Y = 500

title_font = pygame.font.Font('freesansbold.ttf', 32)
title = title_font.render('Welcome to Sudoku', True, black, bg_color)

sub_title_font = pygame.font.Font('freesansbold.ttf', 16)
sub_title = sub_title_font.render('Please select a difficulty', True, black, bg_color)

title_Rect = title.get_rect()
sub_title_Rect = sub_title.get_rect()

title_Rect.center = (X // 2, (Y/2) // 2)
sub_title_Rect.center = (X // 2, ((Y/2)+100) // 2)

color_light = (170, 170, 170)
color_dark = (100, 100, 100)

option_font = pygame.font.SysFont('freesansbold.ttf', 24)

easy = option_font.render('Easy', True, black)
medium = option_font.render('Medium', True, black)
hard = option_font.render('Hard', True, black)

easy_Rect = easy.get_rect()
medium_Rect = medium.get_rect()
hard_Rect = hard.get_rect()

easy_Rect.center = (X // 2 - 150, Y // 2)
medium_Rect.center = (X // 2, Y // 2)
hard_Rect.center = (X // 2 + 150, Y // 2)

running = True

while running:
    height = screen.get_height()
    width = screen.get_width()
    difficulty = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if width / 2 - 40 <= mouse[0] <= width / 2 + 40 and height / 2 - 15 <= mouse[1] <= height / 2 + 15:
                 difficulty = "medium"

            if width / 2 - 150 - 30 <= mouse[0] <= width / 2 - 150 + 30 and height / 2 - 15 <= mouse[1] <= height / 2 + 15:
                 difficulty = "easy"

            if width / 2 + 150 - 30 <= mouse[0] <= width / 2 + 150 + 30 and height / 2 - 15 <= mouse[1] <= height / 2 + 15:
                 difficulty = "hard"

    if not running:
        pygame.quit()
        break
    screen.fill(bg_color)
    screen.blit(title, title_Rect)
    screen.blit(sub_title, sub_title_Rect)
    mouse = pygame.mouse.get_pos()

    if width / 2 - 40 <= mouse[0] <= width / 2 + 40 and height / 2 - 15 <= mouse[1] <= height / 2 + 15:
        pygame.draw.rect(screen, color_light, [X / 3 + 45, Y / 2 - 15, 80, 30])
    else:
        pygame.draw.rect(screen, color_dark, [X / 3 + 45, Y / 2 - 15, 80, 30])

    if width / 2 - 150 - 30 <= mouse[0] <= width / 2 - 150 + 30 and height / 2 - 15 <= mouse[1] <= height / 2 + 15:
        pygame.draw.rect(screen, color_light, [X / 7, Y / 2 - 15, 60, 30])
    else:
        pygame.draw.rect(screen, color_dark, [X / 7, Y / 2 - 15, 60, 30])

    if width / 2 + 150 - 35 <= mouse[0] <= width / 2 + 150 + 35 and height / 2 - 15 <= mouse[1] <= height / 2 + 15:
        pygame.draw.rect(screen, color_light, [X / 3 + 200, Y / 2 - 15, 70, 30])
    else:
        pygame.draw.rect(screen, color_dark, [X / 3 + 200, Y / 2 - 15, 70, 30])

    screen.blit(easy, easy_Rect)
    screen.blit(medium, medium_Rect)
    screen.blit(hard, hard_Rect)

    pygame.display.update()