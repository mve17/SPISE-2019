import pygame
from triangleutils import rotate_a_point


class ShootingTriangle:
    """
    A triangle that rotates and shoots projectiles.
    """

    # Constants to indicate direction of rotation
    CLOCKWISE = None       # Set a value to indicate clockwise direction
    ANTICLOCKWISE = None  # Set a value to indicate anticlockwise direction

    ROTATION_AMOUNT = 5.0 # The amount to rotate the triangle


    def __init__(self, display_surface, display_width, display_height):
        """
        Creates a triangle where the center of the triangle is the center of the display.
        The first point in the tuple is 15 pixels right of the center points provided. 
        The second point is 10 pixels to the left and 10 pixels down from the center. 
        The last point is 10 pixels to the left and 10 pixels up from the center.
        The triangle therefore points to the right.
        All references are in screen coordinates.
        display_surface - The Pygame display surface on which to draw.
        display_width - The width of the display.
        display_height - The height of the display.
        """

        ############################################################################################
        # 1. Make the center of the triangle the center of the screen.
        # 2. Keep a reference to the display surface so that it can be used in other methods.
        # 3. Keep a reference for the current rotation angle.
        ############################################################################################

        #################
        # Your code here
        #################


    def draw(self):
        """
        Draws the rectangle on the screen
        """

        #################
        # Your code here
        #################
        pass
        

    def rotate(self, direction):
        """
        Rotates this triangle in the direction indicated i.e. either clockwise or
        anticlockwise.
        """
        #################
        # Your code here
        #################
        pass


    def get_front_location(self):
        """
        Gets the front of the triangle.
        returns the x and y coordinate of the current front of the triangle as a tuple (x,y)
        """
        #################
        # Your code here
        #################
        return (0,0)


    def get_angle(self):
        """
        Gets the angle the triangle is pointing in.
        """
        return 0
