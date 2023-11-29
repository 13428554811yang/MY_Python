import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """代表舰队中单个外星人的类。"""

    def __init__(self, ai_settings, screen):
        """初始化外星人，并设置其起始位置。"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星图像，并设置其 rect 属性。
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 在屏幕左上角附近启动每个新的外星人。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的确切位置。
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外星人位于屏幕边缘，则返回 True。"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右或向左移动外星人。"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        """在当前位置绘制外星人。"""
        self.screen.blit(self.image, self.rect)
