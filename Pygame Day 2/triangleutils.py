from math import pi, cos, sin


def degrees_to_radians(degrees):
    """
    Translates degrees to radians.
    degrees - The degrees to translate to radians.
    returns the radian value for the degrees passed.
    """

    # Enter your code for calculating radians below.
    # You may find the constant "pi" in the standard library useful: from math import pi
    
    # Your code here:
    return 0
    

def create_triangle(center_x, center_y):
    """
    Creates a triangle as a list of tuples (list of size three for points of triangle,
    each element of the list a tuple of x and y coordinates for a point of the triangle). 
    The first point in the tuple is 50 pixels above the center points provided. 
    The second point is 20 pixels to the right and 10 pixels down from the center. 
    The last point is 20 pixels to the left and 10 pixels down from the center.
    All references are in screen coordinates.
    center_x - The x coordinate of the center of the triangle.
    center_y - The y coordinate of the center of the triangle.
    returns a list of tuples containing the points of the triangle in following order: 
    [(top x, top y), (right x, right y), (left x, left y)]
    """

    ##################
    # Your code here:
    # [top center, bottom right, bottom left]
    return [(0, 0), (0, 0), (0, 0)]


def rotate_a_point(point, degrees, center_x, center_y):
    """
    Rotates a single point around a given center by a specified number of degrees.
    point - the point to rotate.
    degrees - the number of degrees to rotate the point (may be positive or negative).
    center_x - the x coordinate of the center around which to rotate.
    center_y - the y coordinate of the center around which to rotate.
    returns the new value for the rotated point as a tuple (new x, new y)
    """

    # See the following for the rotation formula http://www.sunshine2k.de/articles/RotationDerivation.pdf
    # Please note that the rotation formula works for rotations about the origin (0, 0).
    # Therefore the following steps are required:
    # Translate the point to be relative to the origin from its original center.
    # Rotate the point about the new center now at the origin.
    # Translate the rotated point back to a position relative to original center.
    # The following import may be of help to you: from math import cos, sin

    #######################
    # Your code here:
    #######################
    return (0, 0, 0)
    

def rotate_polygon(polygon, degrees, center_x, center_y):
    """
    Rotates the points in a polygon about a provided center.
    polygon - the polygon to rotate.
    degrees - the degrees to rotate the polygon by.
    center_x - the x coordinate of the center of the polygon around which to rotate.
    center_y - the y coordinate of the center of the polygon around which to rotate.
    returns the new rotated polygon as a list of tuples.
    """

    # This method should be generic in that it should be able to iterate through 
    # any list of tuples and transform them into a new list of tuples with rotated points.
    rotated_polygon = []

    #############################################################################
    # Use the rotate_a_point function above to populate rotated_polygon with new
    # coordinates representing the rotated points for the polygon
    # Your code here
    #############################################################################
    
    return rotated_polygon
