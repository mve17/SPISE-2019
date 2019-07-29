import pygame
from math import cos, sin
from triangleutils import degrees_to_radians


class Projectile:
    """
    A projectile in the application
    """

    RED = (255, 0, 0)

    VELOCITY_MAGNITUDE = 5 # The magnitude of the velocity of this projectile


    def __init__(self, display_surface, x_start, y_start, angle_degrees):
        """
        Creates a the starting location for the projectile
        All references are in screen coordinates.
        display_surface - The Pygame display surface on which to draw.
        x_start - The x coordinate of the starting point of the projectile.
        x_start - The y coordinate of the starting point of the projectile.
        angle_degrees - The angle in degrees that the projectile points.
        """

        # This part is done for you. We create a rectangle because the draw
        # function needs it.
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.centerx = x_start
        self.rect.centery = y_start

        # Your task is to capture other revelent variables that you will need
        # for the other methods of this class
        
        #################
        # YOUR CODE HERE
        #################
        

    def draw(self):
        """
        Draws the projectile on the screen
        """

        ######################################################################
        # Draw a red elipse to represent the projectile
        # Treat the projectile as a vector and use what you know about vectors
        # to make the projectile move at an angle. Any vector has a magnitude,
        # an x component and a y component.
        # Hint: You may find the following Pyton statement useful in this file:
        # from math import cos, sin
        #######################################################################

        #################
        # YOUR CODE HERE
        #################
        pass


    def get_location(self):
        """
        Gets the current location of the projectile on the screen
        returns - An (x,y) tuple with the coordinates of the projectile 
        """
        
        #################
        # YOUR CODE HERE
        #################
        return (0, 0)

