import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Rectangles")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

rect1_width, rect1_height = 50, 50
rect1_x = (WIDTH // 2) - (rect1_width // 2)
rect1_y = (HEIGHT // 2) - (rect1_height // 2)
rect1_speed = 5

rect2_width, rect2_height = 50, 100
rect2_x = 100
rect2_y = 100

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect1_x > 0:
        rect1_x -= rect1_speed
    if keys[pygame.K_RIGHT] and rect1_x < WIDTH - rect1_width:
        rect1_x += rect1_speed
    if keys[pygame.K_UP] and rect1_y > 0:
        rect1_y -= rect1_speed
    if keys[pygame.K_DOWN] and rect1_y < HEIGHT - rect1_height:
        rect1_y += rect1_speed

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (rect1_x, rect1_y, rect1_width, rect1_height))
    pygame.draw.rect(screen, RED, (rect2_x, rect2_y, rect2_width, rect2_height))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()