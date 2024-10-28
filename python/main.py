import pygame
import asyncio

from player import player
from enemies import basic_enemy, fast_enemy

import window
import entity

async def main():
    # pygame.init()
    # screen = pygame.display.set_mode((1280, 720))
    # clock = pygame.time.Clock()
    

    # basic_enemy_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    # fast_enemy_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    # width = screen.get_width()
    # height = screen.get_height()

    # while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False
        # await entity.Entity.player()
    await window.init_window()

        # await draw_score(screen)
        # await draw_wave(screen)
        # await draw_health(screen)

        # await collisions(screen, player_pos, basic_enemy_pos, fast_enemy_pos, width, height)

        # await waves_fun(screen, basic_enemy_pos, fast_enemy_pos ,width, height, dt)
        
<<<<<<< Updated upstream
        screen.fill("black")

        await player(screen, player_pos, width, height, dt)
        await basic_enemy(screen, basic_enemy_pos, width, height, dt)
        await fast_enemy(screen, fast_enemy_pos, width, height, dt)
=======
        # await inc_waves()
        
        # await player(screen, player_pos, width, height, dt)
        

        # await basic_enemy(screen, basic_enemy_pos, width, height, dt)
        # await fast_enemy(screen, fast_enemy_pos, width, height, dt)
>>>>>>> Stashed changes

        # pygame.display.flip()


    # pygame.quit()

asyncio.run(main())

