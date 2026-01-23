import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(random_color)

sprite1 = Box(300, 300)
sprite2 = Box(500, 300)
all_sprites = pygame.sprite.Group(sprite1, sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for sprite in all_sprites:
                    sprite.change_color()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()