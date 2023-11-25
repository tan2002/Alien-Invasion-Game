import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
SPACESHIP_SPEED = 5
BULLET_SPEED = 7

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dual Bullet Spaceship Shoot")
clock = pygame.time.Clock()

# Load spaceship image
spaceship_img = pygame.image.load("Images\player.png")
spaceship_rect = spaceship_img.get_rect()
spaceship_rect.center = (WIDTH // 2, HEIGHT - 50)

# Load bullet image
bullet_img = pygame.Surface((0, 5))
bullet_img.fill(WHITE)

# Lists to hold bullets
bullets = []

def draw_spaceship():
    screen.blit(spaceship_img, spaceship_rect)

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

def move_bullets():
    for bullet in bullets:
        bullet.y -= BULLET_SPEED

def main():
    global spaceship_rect, bullets

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and spaceship_rect.x > 0:
            spaceship_rect.x -= SPACESHIP_SPEED
        if keys[pygame.K_RIGHT] and spaceship_rect.x < WIDTH - spaceship_rect.width:
            spaceship_rect.x += SPACESHIP_SPEED

        # Shoot bullets
        if keys[pygame.K_SPACE]:
            bullet1 = pygame.Rect(spaceship_rect.x, spaceship_rect.y, 5, 5)
            bullet2 = pygame.Rect(spaceship_rect.x + spaceship_rect.width - 5, spaceship_rect.y, 5, 5)
            bullets.extend([bullet1, bullet2])

        # Move bullets
        move_bullets()

        # Remove bullets that are out of the screen
        bullets = [bullet for bullet in bullets if bullet.y > 0]

        # Clear the screen
        screen.fill(BLACK)

        # Draw the spaceship and bullets
        draw_spaceship()
        draw_bullets()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
