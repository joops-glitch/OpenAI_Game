import pygame

# Initialize the Pygame display
pygame.display.init()

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Load the sprite sheet
sprite_sheet = pygame.image.load("images/player.png").convert()

# Create a list to hold the frames of the animation
frames = []

# Define the dimensions of each frame
frame_width = 200
frame_height = 200

# Extract the frames from the sprite sheet and add them to the list
for i in range(0, sprite_sheet.get_width(), frame_width):
    frame = sprite_sheet.subsurface(pygame.Rect(i, 0, frame_width, frame_height))
    frames.append(frame)

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

# Set up the particles
particles = []

# Set up the player's velocity and gravity
x_velocity = 0
y_velocity = 0
gravity = 0.5

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:  # A button
                y_velocity = -10  # Jump
            elif event.button == 1:  # B button
                pass  # Dash
            elif event.button == 2:  # X button
                pass  # Open menu
            elif event.button == 3:  # Y button
                particles.append(Particle(player_rect.centerx, player_rect.centery))  # Shoot

    # Update the player's velocity and position
    x_velocity = joystick.get_axis(0) * 5
    y_velocity += gravity
    player_rect.x += x_velocity
    player_rect.y += y_velocity

    # Update the platforms
    for platform in platforms:
        platform.update()

    # Update the particles
    for particle in particles:
        particle.update()

    # Draw the screen
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_rect)
    for platform in platforms:
        screen.blit(platform.image, platform.rect)
    for particle in particles:
        screen.blit(particle.image, particle.rect)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)