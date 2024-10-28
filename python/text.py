import pygame
import asyncio

from main import screen

class Text(text, size, position, color,location):
    global screen
    
    pygame.font.init()

    screen.blit(pygame.font.Font('fonts/PixelifySans-VariableFont_wght.ttf', size).render(text, 1, color), position)
