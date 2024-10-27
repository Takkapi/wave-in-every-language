import pygame
import asyncio

from enemies import basic_enemy, fast_enemy

from player import health

score = 0
waves = 0

async def waves_fun(screen, basic_enemy_pos, fast_enemy_pos ,width, height, dt):
    global score
    global waves

    score += 1

    if score > 300:
        await basic_enemy(screen, basic_enemy_pos, width, height, dt)
    if score > 1000:
        await basic_enemy(screen, basic_enemy_pos, width, height, dt)
    if score > 1700:
        await basic_enemy(screen, basic_enemy_pos, width, height, dt)
        await basic_enemy(screen, basic_enemy_pos, width, height, dt)

async def inc_waves():
    global score
    global waves
    
    if score == 300: waves += 1
    if score == 1000: waves += 1
    if score == 1700: waves += 1

async def draw_score(screen):
    global score
    pygame.font.init()

    the_font = pygame.font.Font('fonts/PixelifySans-VariableFont_wght.ttf', 25)

    text_surface = the_font.render(f'Score: {score}', 1, (255, 255, 255))

    screen.blit(text_surface, (0, 0))

async def draw_wave(screen):
    global waves
    pygame.font.init()

    the_font = pygame.font.Font('fonts/PixelifySans-VariableFont_wght.ttf', 25)

    text_surface = the_font.render(f'Wave: {waves}', 1, (255, 255, 255))

    screen.blit(text_surface, (0, 25))

async def draw_health(screen):
    global health
    pygame.font.init()

    the_font = pygame.font.Font('fonts/PixelifySans-VariableFont_wght.ttf', 25)

    text_surface = the_font.render(f'Health: {health}', 1, (255, 255, 255))

    screen.blit(text_surface, (0, 50))
