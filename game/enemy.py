import pygame

class Enemy(pygame.sprite.Sprite):
    """Клас пришельца"""

    def __init__(self, screen):
        """Инициализируем и задаем начальную позицию"""
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r'Images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещение пришельцев"""
        self.y += 0.24
        self.rect.y = self.y