import pygame
import asyncio

import render_entity

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


async def init_window():
    global running 
    global screen
    global dt

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        await render_entity.RenderEntity.render(screen, dt)

        dt = clock.tick(60) / 1000

        pygame.display.flip()
    
    pygame.quit()
