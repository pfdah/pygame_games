import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25,25))
        self.image.fill((20,40,155))
        self.rect = self.image.get_rect(topleft=(55,55))
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
            if self.rect.y == 35:
                return 0
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            if self.rect.y == y_size-15:
                return 0
            self.rect.y += self.speed
