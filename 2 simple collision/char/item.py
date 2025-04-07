import pygame
import random 

class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15,15),2)
        max_x, max_y = pygame.display.get_window_size()
        self.rect = self.image.get_rect(topleft=(int(random.randint(0, max_x)), int(random.randint(55, max_y))))
    
    def make_new(self):
        max_x, max_y = pygame.display.get_window_size()
        self.rect = self.image.get_rect(topleft=(int(random.randint(0, max_x)), int(random.randint(55, max_y))))

