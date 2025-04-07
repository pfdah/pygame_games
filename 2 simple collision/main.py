import pygame 
from char import character, item

bg_color = (255,255,255)
screen = pygame.display.set_mode((500,500))
screen.fill(bg_color)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

player = character.Player()
item = item.Item()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(item)


score = 0
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 20)

def dist(x_1,y_1,x_2,y_2):
    distance = (abs(x_2 - x_1)**2 + abs(y_2 - y_1)**2)**(0.5)
    return distance

run =True
while run:
    clock.tick(20)
    for event in pygame.event.get():
        pygame.display.flip()
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    all_sprites.update(keys)
    d = dist(player.rect.x, player.rect.y, item.rect.x, item.rect.y)
    if  d <= 20:
        item.make_new()
        score += 1
    screen.fill(bg_color)
    text_surface = my_font.render(f'Score is {score}', False, (0,0,0))
    screen.blit(text_surface, (10,10))
    all_sprites.draw(screen)
    pygame.display.flip()
