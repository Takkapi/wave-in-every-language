import pygame
import asyncio
import numpy as np

# from window import screen, dt

class Entity():
    async def player(screen, dt):
        health = 100
        speed = 700

        pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        
        # Draw player if the health is greater or equal to 1
        if health >= 1:
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(pos.x, pos.y, 50, 50))

        # Clamp the position so the player will not go offscreen
        pos.x = np.clip(pos.x, 0, screen.get_width() - 51)
        pos.y = np.clip(pos.y, 0, screen.get_height() - 51)

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            pos.y -= speed * dt
        if keys[pygame.K_s]:
            pos.y += speed * dt
        if keys[pygame.K_a]:
            pos.x -= speed * dt
        if keys[pygame.K_d]:
            pos.x += speed * dt