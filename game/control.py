import pygame
import sys
from bullet import Bullet
from enemy import Enemy
import time

def events(screen, player, bullets):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            # Вправо на "стрелочку"
            if event.key == pygame.K_RIGHT:
                player.mright = True
            # Влево на "стрелочку"
            elif event.key == pygame.K_LEFT:
                player.mleft = True
            # Вправо на "d"
            if event.key == pygame.K_d:
                player.mright = True
            # Влево на "a"
            elif event.key == pygame.K_a:
                player.mleft = True
            # Стрельба на "пробел"
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, player)
                bullets.add(new_bullet)

            # Зажимание кнопок
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.mright = False
            elif event.key == pygame.K_LEFT:
                player.mleft = False
            if event.key == pygame.K_d:
                player.mright = False
            elif event.key == pygame.K_a:
                player.mleft = False

def update(bg_color, screen, stats, score, player, enemys, bullets):
    """Обновление экрана"""
    screen.fill(bg_color)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    player.output()
    enemys.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, score, enemys, bullets):
    """Обновляем позицию пули"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)
    if collisions:
        for enemys in collisions.values():
            stats.score += 100 * len(enemys)
        score.image_score()
        check_high_score(stats, score)
        score.image_players()
    if len(enemys) == 0:
        bullets.empty()
        create_army(screen, enemys)

def player_death(stats, screen, score, player, enemys, bullets):
    """Столкновение игрока с пришнльцами"""
    if stats.players_left > 0:
        stats.players_left -= 1
        score.image_players()
        enemys.empty()
        bullets.empty()
        create_army(screen, enemys)
        player.create_player()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()

def update_enemys(stats, screen, score, player, enemys, bullets):
    """Обновляет позицию пришельцев"""
    enemys.update()
    if pygame.sprite.spritecollideany(player, enemys):
       player_death(stats, screen, score, player, enemys, bullets)
    enemys_check(stats, screen, score, player, enemys, bullets)

def enemys_check(stats, screen, score, player, enemys, bullets):
    """проигрыш,когда пришельци добрадись до края экрана"""
    screen_rect = screen.get_rect()
    for enemy in enemys.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            player_death(stats, screen, score, player, enemys, bullets)
            break
def create_army(screen, enemys):
    """Создание армии пришельцев"""
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((1200 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((900 - 100 - 2 * enemy_height) / enemy_height)

    for row_number in range(number_enemy_y - 1):
        for enemy_number in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + (enemy_width * enemy_number)
            enemy.y = enemy_height + (enemy_height * row_number)
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + (enemy.rect.height * row_number)
            enemys.add(enemy)

def check_high_score(stats, score):
    """Проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.image_high_score()
        with open('record.txt', 'w') as f:
            f.write(str(stats.high_score))