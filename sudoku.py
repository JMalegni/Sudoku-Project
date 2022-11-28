"""Sudoku: entry point for project"""
import sys
import pygame
from pygame import mouse 

# import files from ./UI
sys.path.insert(0, "./UI")
from welcome_screen import welcome_screen

#  if __name__ == "__main__":
    # start UI, run program, etc etc

if __name__ == "__main__": 
    # start UI, run program, etc etc

    pygame.init()

    WIDTH = 500 
    HEIGHT = 500 
    colors = {
        "black": (0,0,0),
        "white": (255,255,255),
        "bg_color": (234, 212, 252),
        "LINE_COLOR": (255, 255, 255),
    }

    diff = None
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    difficulty_level = welcome_screen(screen, diff, WIDTH, HEIGHT, colors)

    print(difficulty_level)
