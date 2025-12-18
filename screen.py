import pygame
import sys
import os


pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CAPTION = "My First Game"
BG_COLOR = (58, 58, 58) 


IMAGE_FILE = 'my_image.png'
IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)


try:
    image_surface = pygame.image.load(IMAGE_FILE).convert_alpha()

    image_surface = pygame.transform.scale(image_surface, (IMAGE_WIDTH, IMAGE_HEIGHT))
    
    
    image_rect = image_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

except pygame.error as e:
    print(f"Error loading image: {e}")
    print(f"Please ensure '{IMAGE_FILE}' is in the same directory.")
    sys.exit()


running = True
clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    

    screen.blit(image_surface, image_rect)
    
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
sys.exit()