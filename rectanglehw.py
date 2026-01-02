import pygame
import sys

pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CAPTION = "my first game"



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RECT_COLOR = BLACK
TEXT_COLOR = BLACK
RECT_WIDTH = 50
RECT_HEIGHT = 50


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)



font = pygame.font.SysFont(None, 40)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    
    screen.fill(WHITE)

    
    
    rect_x = (SCREEN_WIDTH // 2) - (RECT_WIDTH // 2)
    rect_y = (SCREEN_HEIGHT // 2) - (RECT_HEIGHT // 2)
    
    
    pygame.draw.rect(screen, RECT_COLOR, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))

    
    
    text_surface = font.render("My First Game Screen", True, TEXT_COLOR)

    text_rect = text_surface.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, 50)
    
    screen.blit(text_surface, text_rect)


    pygame.display.flip()


pygame.quit()
sys.exit()