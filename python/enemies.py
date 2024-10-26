import pygame
import numpy as np
import asyncio

async def basic_enemy(screen, basic_enemy_pos, width, height, dt):
    speedX = -600
    speedY = -600
    
    offset = 25.5

    pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(basic_enemy_pos.x, basic_enemy_pos.y, 25, 25))

    basic_enemy_pos.y += speedY * dt
    basic_enemy_pos.x += speedX * dt

    basic_enemy_pos.x = np.clip(basic_enemy_pos.x, 0, width - offset)
    basic_enemy_pos.y = np.clip(basic_enemy_pos.y, 0, height - offset)

    if basic_enemy_pos.x >= width - offset or basic_enemy_pos.x <= 1:
        speedX *= -1
    if basic_enemy_pos.y >= height - offset or basic_enemy_pos.y <= 1:
        speedY *= -1

async def fast_enemy(screen, basic_enemy_pos, width, height, dt):
    speedX = 600
    speedY = 900
    
    offset = 25.5

    pygame.draw.rect(screen, pygame.Color(0, 255, 255), pygame.Rect(basic_enemy_pos.x, basic_enemy_pos.y, 25, 25))

    basic_enemy_pos.y += speedY * dt
    basic_enemy_pos.x += speedX * dt

    basic_enemy_pos.x = np.clip(basic_enemy_pos.x, 0, width - offset)
    basic_enemy_pos.y = np.clip(basic_enemy_pos.y, 0, height - offset)

    if basic_enemy_pos.x >= width - offset or basic_enemy_pos.x <= 1:
        speedX *= -1
    if basic_enemy_pos.y >= height - offset or basic_enemy_pos.y <= 1:
        speedY *= -1