import pygame
from pygame.sprite import Sprite

class Player(Sprite):

    def __init__(self, screen):
        """инициализация пушки"""
        super(Player, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r'Images/player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """Отображение пушки"""
        self.screen.blit(self.image, self.rect)

    def update_player(self):
        """Обновление пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 2
        if self.mleft and self.rect.left > 0:
            self.center -= 2

        self.rect.centerx = self.center

    def create_player(self):
        """Возрождает пушку, возврощая ее в центр"""
        self.center = self.screen_rect.centerx