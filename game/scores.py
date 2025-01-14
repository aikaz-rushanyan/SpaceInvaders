import pygame.font
from player import Player
from pygame.sprite import Group

class Scores():
    """Вывод игровой информации"""
    def __init__(self, screen, stats):
        """Инициализируем подсчет очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_players()

    def image_score(self):
        """Преобразуем текст счета в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 48
        self.score_rect.top = 20

    def image_high_score(self):
        """Преобразует рекорд в графическое изображение"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_players(self):
        """Колличество жизней"""
        self.players = Group()
        for player_number in range(self.stats.players_left):
            player = Player(self.screen)
            player.rect.x = 15 + player_number * player.rect.width
            player.rect.y = 20
            self.players.add(player)


    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.players.draw(self.screen)
