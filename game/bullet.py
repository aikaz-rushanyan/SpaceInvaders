import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, player):
        """Создаем пули в пушке"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 7, 18)
        self.color = 139, 195, 74
        self.speed = 3
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули по y"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисуем пулю"""
        pygame.draw.rect(self.screen, self.color, self.rect)
