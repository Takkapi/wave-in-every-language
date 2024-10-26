import pygame
import numpy as np
import asyncio

async def player(screen, player_pos, width, height, dt):
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(player_pos.x, player_pos.y, 50, 50))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 400 * dt
    if keys[pygame.K_s]:
        player_pos.y += 400 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 400 * dt
    if keys[pygame.K_d]:
        player_pos.x += 400 * dt

    player_pos.x = np.clip(player_pos.x, 0, width - 51)
    player_pos.y = np.clip(player_pos.y, 0, height - 51)