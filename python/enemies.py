import pygame
import numpy as np
import asyncio

async def basic_enemy(screen, basic_enemy_pos, width, height, dt):
    speedX = 500
    speedY = 500

    pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(basic_enemy_pos.x, basic_enemy_pos.y, 25, 25))

    basic_enemy_pos.y += speedY * dt
    basic_enemy_pos.x += speedX * dt

    if basic_enemy_pos.x == width - 51 or basic_enemy_pos.x == 0:
        speedX *= -1
    if basic_enemy_pos.y == height - 51 or basic_enemy_pos.y == 0:
        speedY *= -1

    basic_enemy_pos.x = np.clip(basic_enemy_pos.x, 0, width - 51)
    basic_enemy_pos.y = np.clip(basic_enemy_pos.y, 0, height - 51)

