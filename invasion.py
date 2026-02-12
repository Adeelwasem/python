import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


player = pygame.Rect(375, 550, 50, 30)
bullets = []
enemies = [pygame.Rect(x * 60 + 50, y * 50 + 50, 40, 30) for x in range(10) for y in range(5)]
enemy_direction = 1
enemy_speed = 2

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(pygame.Rect(player.centerx - 2, player.top, 5, 10))
            laser_sound.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0: player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < 800: player.x += 5

    hit_edge = False
    for e in enemies:
        e.x += enemy_speed * enemy_direction
        if e.right >= 800 or e.left <= 0: hit_edge = True
    
    if hit_edge:
        enemy_direction *= -1
        for e in enemies: e.y += 10

    for b in bullets[:]:
        b.y -= 7
        if b.bottom < 0: bullets.remove(b)
        for e in enemies[:]:
            if b.colliderect(e):
                bullets.remove(b)
                enemies.remove(e)
                break

    pygame.draw.rect(screen, (0, 255, 0), player)
    for e in enemies: pygame.draw.rect(screen, (255, 0, 0), e)
    for b in bullets: pygame.draw.rect(screen, (255, 255, 255), b)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()