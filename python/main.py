import pygame
import asyncio

from player import player
from enemies import *

from game_manager import *

async def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    basic_enemy_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    fast_enemy_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    width = screen.get_width()
    height = screen.get_height()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")

        await draw_score(screen)
        await draw_wave(screen)
        await draw_health(screen)

        await collisions(screen, player_pos, basic_enemy_pos, fast_enemy_pos, width, height)

        await waves_fun(screen, basic_enemy_pos, fast_enemy_pos ,width, height, dt)
        
        await inc_waves()
        
        await player(screen, player_pos, width, height, dt)

        # await basic_enemy(screen, basic_enemy_pos, width, height, dt)
        # await fast_enemy(screen, fast_enemy_pos, width, height, dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

asyncio.run(main())
