import pygame, sys
from pygame.locals import *
from shootingtriangle import ShootingTriangle
from projectile import Projectile


def create_projectile(display_surface, shooting_triangle, projectile_list, sound):
    """
    Creates a new projectile and addes it to a list of other projectiles.
    display_surface - The display surface objects are drawing on.
    shooting_triangle - The aggressive triangle that spins and shoots.
    projectile_list - The list of all projectiles on the screen.
    sound - The sound to play when a projectile is launched 
    """
    x, y = shooting_triangle.get_front_location()
    angle = shooting_triangle.get_angle()  # The angle the triangle is pointing in
    
    projectile = Projectile(display_surface, x, y, angle)
    projectile_list.append(projectile)
    
    sound.play()


def draw_projectiles(projectile_list, screen_width, screen_height):
    """
    Draws all projectiles in the list.
    projectile_list - The list of projectiles to be drawn.
    screen_width - The width of the game window.
    screen_height - The height of the game window.
    """

    # Notice the special slicing syntax that you see below:
    # projectile_list[:]
    # This is a small trick that makes a copy of the list to iterate on.
    # We do this because we cannot remove elements from a list while we are
    # iterating on it. Therefore we make a copy of the original list,
    # iterate on the copy of the list and then remove elements from the
    # original list that move off of the screen
    copy_of_list = projectile_list[:]
    
    for projectile in copy_of_list: # Draw each projectile in the list
        projectile.draw()
        x, y = projectile.get_location()

        # Remove projectiles from the list passed in that go off of the screen.
        if (x < 0 or x > screen_width or y < 0 or y > screen_height):
            projectile_list.remove(projectile)


if __name__ == '__main__':

    pygame.init()  # Initialize the Pygame system

    # Window dimensions
    DISPLAY_WIDTH = 600
    DISPLAY_HEIGHT = 500

    # Create the surface to draw on of width 600 x 500 pixels
    DISPLAY_SURFACE = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    # Background color white
    BACKGROUND_COLOR = (255, 255, 255)

    # Display shown at the top of the window
    pygame.display.set_caption('Shooting Rectangle')

    # Generate when a key is held down.
    # See https://www.pygame.org/docs/ref/key.html#pygame.key.set_repeat
    pygame.key.set_repeat(500, 100)

    # Load sound file
    shooting_sound = pygame.mixer.Sound('shoot.wav')

    shooting_triangle = ShootingTriangle(DISPLAY_SURFACE, DISPLAY_WIDTH, DISPLAY_HEIGHT)

    projectile_list = []

    while True: # Main game loop

        # Fill the screen background with white so that previous drawings are erased.
        DISPLAY_SURFACE.fill(BACKGROUND_COLOR)

        shooting_triangle.draw()

        draw_projectiles(projectile_list, DISPLAY_WIDTH, DISPLAY_HEIGHT)
    
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:  # For events where a keyboard button is in the down position
                if event.key == K_LEFT:  # If the event was for the left arrow key
                    shooting_triangle.rotate(ShootingTriangle.CLOCKWISE)
                elif event.key == K_RIGHT: # If the event was for the right arrow key
                    shooting_triangle.rotate(ShootingTriangle.ANTICLOCKWISE)                
                elif event.key == K_SPACE:
                    create_projectile(DISPLAY_SURFACE, shooting_triangle, \
                                      projectile_list, shooting_sound)

            # If the windows is closed then exit pygame
            if event.type == QUIT:
                pygame.quit() # Shutdown Pygame system
                sys.exit() # Exit the program

        pygame.display.update() # Update the screen
