import pygame, sys
from pygame.locals import *
from triangleutils import *


def rotate_polygon_on_arrow_keys(event, degrees, polygon, center_x, center_y):
    """
    Rotates a polygon around a given center by a specified number of degrees
    event - the system event generated by pygame.
    degrees - the number of degrees to rotate by.
    polygon - the polygon to rotate.
    center_x - x coordinate of the center position
    center_y - y coordinate of the center position
    """

    # Please see the following for possible key values: https://www.pygame.org/docs/ref/key.html
    if event.type == KEYDOWN:  # For events where a keyboard button is in the down position
        if event.key == K_LEFT:  # If the event was for the left arrow key
            return rotate_polygon(polygon, -degrees, center_x, center_y)
        elif event.key == K_RIGHT: # If the event was for the right arrow key
            return rotate_polygon(polygon, degrees, center_x, center_y)

    return polygon


if __name__ == '__main__':

    pygame.init()  # Initialize the Pygame system

    # Create the surface to draw on of width 600 x 500 pixels
    DISPLAY_SURFACE = pygame.display.set_mode((600, 500))

    # RGB values for the color white
    WHITE = (255, 255, 255)
    # RGB values for color red.
    RED = (255, 0, 0)

    # The number of degrees to rotate polygon by each time the arrow key is pressed
    ROTATION_DEGREES = 30

    # The location of the center of the triangle
    TRIANGLE_CENTER_X = 300
    TRIANGLE_CENTER_Y = 250

    # Remove this commented code if you want multiple pygame.KEYDOWN events to be generate when a key is held down.
    # See https://www.pygame.org/docs/ref/key.html#pygame.key.set_repeat
    # pygame.key.set_repeat(500, 100)

    # Create the triangle (imported from rotate_triangle_utils module)
    triangle = create_triangle(TRIANGLE_CENTER_X, TRIANGLE_CENTER_Y)

    while True: # Main game loop

        # Fill the screen background with white so that previous drawings are erased.
        DISPLAY_SURFACE.fill(WHITE)

	# Use pygame draw polygon function to draw a red triangle of line width 1.
        ###############
        # Your code here for drawing polygon:
        ###############
    
        for event in pygame.event.get():
            triangle = rotate_polygon_on_arrow_keys(event, ROTATION_DEGREES, triangle, TRIANGLE_CENTER_X, TRIANGLE_CENTER_Y)

            # If the windows is closed then exit pygame
            if event.type == QUIT:
                pygame.quit() # Shutdown Pygame system
                sys.exit() # Exit the program

        pygame.display.update() # Update the screen