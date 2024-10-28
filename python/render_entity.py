import asyncio

import entity

class RenderEntity():
    async def render(screen, dt):
        await entity.Entity.player(screen, dt)