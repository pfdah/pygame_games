import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./src/char.png')
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect(topleft=(30, 40))
        self.speed = 5

    def update(self, keys):
        x_size, y_size = pygame.display.get_window_size()
        if keys[pygame.K_LEFT]:
            if self.rect.x == 0:
                return 0
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            if self.rect.x == x_size-15:
                return 0
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            if self.rect.y == 0:
                return 0
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            if self.rect.y == y_size-15:
                return 0
            self.rect.y += self.speed
