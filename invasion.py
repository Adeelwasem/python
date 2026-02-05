import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
ENEMY_SPEED = 2
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chase Game with Scoreboard")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, color, x, y, size=40):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

class Enemy(SpriteObject):
    def update(self, player_pos):
        # Calculate direction vector toward player
        dx = player_pos[0] - self.rect.x
        dy = player_pos[1] - self.rect.y
        dist = math.hypot(dx, dy)
        
        if dist != 0:
            # Move towards player at a fixed speed
            self.rect.x += (dx / dist) * ENEMY_SPEED
            self.rect.y += (dy / dist) * ENEMY_SPEED

# Game setup
player = SpriteObject(BLUE, WIDTH//2, HEIGHT//2)
score_item = SpriteObject(GREEN, random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50), size=20)
enemies = pygame.sprite.Group()

# Add 7 enemies at random positions
for _ in range(7):
    ex = random.randint(0, WIDTH - 40)
    ey = random.randint(0, HEIGHT - 40)
    enemies.add(Enemy(RED, ex, ey))

score = 0
running = True

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.left > 0: player.rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.rect.right < WIDTH: player.rect.x += PLAYER_SPEED
    if keys[pygame.K_UP] and player.rect.top > 0: player.rect.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player.rect.bottom < HEIGHT: player.rect.y += PLAYER_SPEED

    # Enemy Logic: Move towards player
    enemies.update(player.rect.center)

    # Collision Detection: Player hits score item
    if player.rect.colliderect(score_item.rect):
        score += 1
        # Reposition score item after collection
        score_item.rect.topleft = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))

    # Optional: Collision with enemies (Reset or Game Over)
    if pygame.sprite.spritecollideany(player, enemies):
        print(f"Game Over! Final Score: {score}")
        running = False

    # Draw everything
    screen.blit(player.image, player.rect)
    enemies.draw(screen)
    screen.blit(score_item.image, score_item.rect)
    
    # Display Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()