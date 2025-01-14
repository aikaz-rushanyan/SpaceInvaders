import pygame, control, asyncio
from player import Player
from pygame.sprite import Group
from stats import Stats
from scores import Scores


pygame.init()
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Space invaders")
bg_color = (0, 0, 0) 
player = Player(screen)
bullets = Group()
enemys = Group()
control.create_army(screen, enemys)
stats = Stats()
score = Scores(screen, stats)

async def main():
    while True:
        control.events(screen, player, bullets)
        if stats.run_game:
            player.update_player()
            bullets.update()
            control.update(bg_color, screen, stats, score, player, enemys, bullets)
            control.update_bullets(screen, stats, score,  enemys, bullets)
            control.update_enemys(stats, screen, score, player, enemys, bullets)
        
        await asyncio.sleep(0)
asyncio.run(main())

