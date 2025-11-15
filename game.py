#pip install pygame

import pygame, sys, random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐤 Flappy Bird")
clock = pygame.time.Clock()

# Colors
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)

# Load bird image
bird_img = pygame.image.load("bird.jpg")
bird_img = pygame.transform.scale(bird_img, (40, 30))

# Bird variables
bird_x = 50
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.5
flap_strength = -8

# Pipe variables
pipe_width = 70
pipe_gap = 150
pipe_velocity = 4
pipes = []

# Game state
score = 0
font = pygame.font.SysFont("arial", 28)
game_over = False

def create_pipe():
    """Creates a new pipe pair with a random gap position."""
    y_top = random.randint(100, HEIGHT - 200)
    return {"x": WIDTH, "y_top": y_top, "y_bottom": y_top + pipe_gap}

def draw_pipes():
    """Draws all pipes."""
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe["x"], 0, pipe_width, pipe["y_top"]))
        pygame.draw.rect(screen, GREEN, (pipe["x"], pipe["y_bottom"], pipe_width, HEIGHT - pipe["y_bottom"]))

def check_collision():
    """Check for collision with pipes or boundaries."""
    global bird_y
    if bird_y <= 0 or bird_y >= HEIGHT - 20:
        return True
    for pipe in pipes:
        if bird_x + 30 > pipe["x"] and bird_x < pipe["x"] + pipe_width:
            if bird_y < pipe["y_top"] or bird_y + 20 > pipe["y_bottom"]:
                return True
    return False

def reset_game():
    """Resets game state."""
    global bird_y, bird_velocity, pipes, score, game_over
    bird_y = HEIGHT // 2
    bird_velocity = 0
    pipes = [create_pipe()]
    score = 0
    game_over = False

# Start with one pipe
pipes = [create_pipe()]

# Main loop
while True:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_over:
                reset_game()
            else:
                bird_velocity = flap_strength

    if not game_over:
        # Bird movement
        bird_velocity += gravity
        bird_y += bird_velocity

        # Pipe movement
        for pipe in pipes:
            pipe["x"] -= pipe_velocity

        # Add new pipes
        if pipes[-1]["x"] < WIDTH - 250:
            pipes.append(create_pipe())

        # Remove off-screen pipes and update score
        if pipes[0]["x"] + pipe_width < 0:
            pipes.pop(0)
            score += 1

        # Check collision
        if check_collision():
            game_over = True

    # Draw everything
    draw_pipes()
    screen.blit(bird_img, (bird_x, bird_y))
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render("Game Over! Press SPACE", True, WHITE)
        screen.blit(game_over_text, (50, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)
