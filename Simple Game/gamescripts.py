import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Game clock
clock = pygame.time.Clock()
FPS = 60

# Player attributes
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 5

# Enemy attributes
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5

# Collectible attributes
collectible_size = 30
collectible_pos = [random.randint(0, WIDTH - collectible_size), random.randint(0, HEIGHT - 2 * collectible_size)]

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game over function
def game_over():
    screen.fill(BLACK)
    game_over_text = font.render("GAME OVER", True, RED)
    score_text = font.render(f"Your Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed

    # Enemy movement
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > HEIGHT:
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]

    # Collision with enemy
    if (enemy_pos[0] < player_pos[0] < enemy_pos[0] + enemy_size or
        enemy_pos[0] < player_pos[0] + player_size < enemy_pos[0] + enemy_size) and \
       (enemy_pos[1] < player_pos[1] < enemy_pos[1] + enemy_size or
        enemy_pos[1] < player_pos[1] + player_size < enemy_pos[1] + enemy_size):
        game_over()

    # Collect collectible
    if (collectible_pos[0] < player_pos[0] < collectible_pos[0] + collectible_size or
        collectible_pos[0] < player_pos[0] + player_size < collectible_pos[0] + collectible_size) and \
       (collectible_pos[1] < player_pos[1] < collectible_pos[1] + collectible_size or
        collectible_pos[1] < player_pos[1] + player_size < collectible_pos[1] + collectible_size):
        score += 1
        collectible_pos = [random.randint(0, WIDTH - collectible_size), random.randint(0, HEIGHT - 2 * collectible_size)]

    # Draw everything
    pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))
    pygame.draw.rect(screen, RED, (*enemy_pos, enemy_size, enemy_size))
    pygame.draw.rect(screen, GREEN, (*collectible_pos, collectible_size, collectible_size))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
