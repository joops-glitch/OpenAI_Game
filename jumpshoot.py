import pygame
import particle

# Initialize the Pygame display
pygame.display.init()

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Set up the player character
player_char = "@"

####Currently unused, come back later and fix that.
# Set up the ASCII tileset
tileset = {
    '.': '.',  # Empty space
    '#': '#',  # Wall
    '@': '@',  # Player
    'O': 'O',  # Platform
    '^': '^',  # Jump power-up
    'V': 'V',  # Dash power-up
    '<': '<',  # Shooting power-up
}

####Later, come back and set up level and adjust player's position. Maybe player's position is in a helper function that changes every level?

# # Create a list to hold the tiles of the level
# level = []

# # Set the player's starting position in the level
# player_x = level[0].index('@')
# player_y = 0
# level[player_y][player_x] = '.'

# Player Rect
player_rect = pygame.Rect(0,0,0,0)
player_rect.centerx = screen.get_width() // 2
player_rect.centery = screen.get_height() // 2

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
bullet_char = "-"

#give the bullet a color
bullet_color = (255, 255, 255)

#helper function for drawing text
def draw_text(surface, text, x, y, color=(255, 255, 255), font_name = "Arial", font_size=16):
    if font_name not in pygame.font.get_fonts():
        font_name = pygame.font.match_font(font_name)
    font = pygame.font.Font(font_name, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

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
                bullets.append(particle.Particle(player_rect.centerx, player_rect.centery, screen, bullets, bullet_color, distance=100, draw_text_fn=draw_text))  # Shoot
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

    # Draw the screen
    screen.fill((0, 0, 0))

    # Draw the player
    draw_text(screen, "@", player_rect.x, player_rect.y, color=(255, 255, 255))
    for platform in platforms:
        for i, row in enumerate(platform.map):
            for j, col in enumerate(row):
                draw_text(screen, col, j*16, i*16)
        for bullet in bullets:
            draw_text(bullet)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)