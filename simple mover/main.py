import pygame
from char import character

bg_color = (0,0,0)
screen = pygame.display.set_mode((500,600))
screen.fill(bg_color)
pygame.display.set_caption('Hawa Game ko demo')
clock = pygame.time.Clock()

player = character.Player()        
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

run = True
while run:
    clock.tick(20)
    for event in pygame.event.get():
        pygame.display.flip()
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)  # Pass keys to your sprite's update

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
