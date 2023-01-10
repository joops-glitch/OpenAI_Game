#JumpShoot.py

import pygame
import particle
import blocks


# Initialize the Pygame display
pygame.display.init()

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Load the tileset image
tileset_image = pygame.image.load("images/tiles-tech-steel-gold-alpha.png").convert()

# Set the tile size (assume all tiles in the tileset are the same size)
tile_size = 16

# Create a 2D array to represent the level layout
level = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15],
]

# Load the sprite sheet
sprite_sheet = pygame.image.load("images/player.png").convert()

# Create a list to hold the frames of the animation
frames = []

# Define the dimensions of each frame
frame_width = 32
frame_height = 32

# Extract the frames from the sprite sheet and add them to the list
for i in range(0, sprite_sheet.get_width(), frame_width):
    frame = sprite_sheet.subsurface(pygame.Rect(i, 0, frame_width, frame_height))
    frames.append(frame)


# Set up the player
player_image = frames[0]
player_rect = player_image.get_rect()
player_rect.bottom = screen.get_height()  # Position the player at the bottom of the screen
# Set up the player character
player_image = frames[0]
player_rect = player_image.get_rect()

# Set up the clock
clock = pygame.time.Clock()

# Set up the controller
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Set up the platforms
platforms = []

# Set up the bullet particles
bullets = []

# Set up the player's velocity and gravity
x_velocity = 0
y_velocity = 0
gravity = 0#.5

# Load the particle image
bullet_image = pygame.image.load("images/bullet.png").convert()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #sys.exit()
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0:  # A button
                y_velocity = -10  # Jump
            elif event.button == 1:  # B button
                pass  # Dash
            if event.button == 2:  # X button
                bullets.append(particle.Particle(player_rect.centerx, player_rect.centery, bullet_image, screen, bullets, distance=100))  # Shoot
            elif event.button == 3:  # Y button
                pass  # Open menu

    # Update the player's velocity and position
    x_velocity = joystick.get_axis(0) * 5
    y_velocity += gravity
    player_rect.x += x_velocity
    player_rect.y += y_velocity

    # Update the platforms
    for platform in platforms:
        platform.update()

    # Update the particles
    for bullet in bullets:
        bullet.update()

    # Draw the level
    for row in range(len(level)):
        for column in range(len(level[row])):
            tile = level[row][column]
            x = column * tile_size
            y = row * tile_size
            screen.blit(tileset_image, (x, y), (tile * tile_size, 0, tile_size, tile_size))

    # Draw the screen
    #screen.fill((0, 0, 0))
    screen.blit(player_image, player_rect)
    for platform in platforms:
        screen.blit(platform.image, platform.rect)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)