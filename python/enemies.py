import pygame
import numpy as np
import asyncio

from player import health

speedX = 550
speedY = 550

basic_enemy_power = 15

async def basic_enemy(screen, basic_enemy_pos, width, height, dt):
    global speedX
    global speedY
    
    offset = 25.5

    pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(basic_enemy_pos.x, basic_enemy_pos.y, 25, 25))

    if basic_enemy_pos.x >= width - offset or basic_enemy_pos.x <= 0:
        speedX = speedX * -1
    if basic_enemy_pos.y >= height - offset or basic_enemy_pos.y <= 1:
        speedY = speedY * -1

    basic_enemy_pos.y += speedY * dt
    basic_enemy_pos.x += speedX * dt

    basic_enemy_pos.x = np.clip(basic_enemy_pos.x, 0, width - offset)
    basic_enemy_pos.y = np.clip(basic_enemy_pos.y, 0, height - offset)

fast_speedX = 350
fast_speedY = 900

async def fast_enemy(screen, pos, width, height, dt):
    global fast_speedX
    global fast_speedY
    
    offset = 25.5

    pygame.draw.rect(screen, pygame.Color(0, 255, 255), pygame.Rect(pos.x, pos.y, 25, 25))

    if pos.x == width - offset or pos.x == 0:
        fast_speedX *= -1
    if pos.y == height - offset or pos.y == 0:
        fast_speedY *= -1

    pos.y += fast_speedY * dt
    pos.x += fast_speedX * dt

    pos.x = np.clip(pos.x, 0, width - offset)
    pos.y = np.clip(pos.y, 0, height - offset)

async def basic_enemy_damage():
    global health

    health -= basic_enemy_power

async def collisions(screen, player_pos, basic_enemy_pos, fast_enemy_pos, width, height):
    player = pygame.Rect(player_pos.x, player_pos.y, width, height)
    basic_enemy = pygame.Rect(basic_enemy_pos.x, basic_enemy_pos.y, width, height)

    collide = player.colliderect(basic_enemy)

    if collide:
        await basic_enemy_damage()
