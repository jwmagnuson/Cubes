#!/usr/bin/python3
#==============================================================================
#
# cubes.py
#
# Jacob Magnuson <jmagnus4@stumail.jccc.edu>
# 2015-20-11, version 0.0.0
#
# This script uses the textbook's graphics.py module to draw three dimensional
# cubes using arguments given by the user. This script currently accepts three
# arguments that it uses to determine the size of the cube. Arguments should
# be passed in the order Width (x) Height (y) Depth(z) ie: cubes.py 200 300
# 400 would create a cube with a width of 200 pixels, a height of 300 pixels,
# and a depth of 400 pixels.
#
#==============================================================================


"""
cubes.py
========

Utilizes the textbook's graphic.py module to render three dimensional cubes
based on user input.
"""


import sys
import math

import graphics


__version__ = '0.0.0'


#==============================================================================
# MODULE CONSTANTS
#==============================================================================
# Width of the window
WINDOW_X = 600

# Height of the window
WINDOW_Y = 600

# Middle X coordinate of the window
MIDDLE_X = WINDOW_X / 2

# Middle Y coordinate of the window
MIDDLE_Y = WINDOW_Y / 2


#==============================================================================
def project_cube( dimensions ):
    """
    Builds a list of lines needed to draw a cube with the given dimensions

    @param dimensions A list containing the script name followed by the desired
                      x, y, and z dimensions in pixels.

    @return           A list containing 9 tuples in the format (x1, y1, x2, y2)
                      to be used by drawLine function of the textbook's
                      graphics module
    """

    # Seperate the parameter list into dimension variables
    x = int( dimensions[ 1 ] )
    y = int( dimensions[ 2 ] )
    z = int( dimensions[ 3 ] )

    # Create a list that will hold our points
    points = []

    # With the default rotation, both x and z dimensions will be diagonal
    # We need break the diagonal lengths into horizontal and vertical lengths
    # using the pythagorean theorem ( a ** 2 + b ** 2 = c ** 2 ).
    # Being that this is a rectangular cuboid, all angles are 90 degrees
    # So we can use the formula leg = sqrt ( ( diag ** 2 ) / 2 ).
    x_leg = math.sqrt( ( x ** 2 ) / 2 )
    z_leg = math.sqrt( ( z ** 2 ) / 2 )


    #==========================================================================
    # Draw right face
    #==========================================================================
    # This line starts from the origin (middle of the window) and travels up
    # and to the right for x pixels
    points.append( ( MIDDLE_X, MIDDLE_Y,
                     MIDDLE_X + x_leg, MIDDLE_Y - x_leg ) )

    # This line starts from the origin and travels down y pixels
    points.append( ( MIDDLE_X, MIDDLE_Y,
                     MIDDLE_X, MIDDLE_Y + y ) )

    # This line starts at the end of the last line and travels up and to the
    # right for x pixels
    points.append( ( MIDDLE_X, MIDDLE_Y + y,
                     MIDDLE_X + x_leg, MIDDLE_Y + y - x_leg ) )

    # This line starts at the end of the last line and travels up y pixels
    points.append( ( MIDDLE_X + x_leg, MIDDLE_Y - x_leg,
                     MIDDLE_X + x_leg, MIDDLE_Y + y - x_leg ) )


    #==========================================================================
    # Draw left face
    #==========================================================================
    # This line starts from the origin (middle of the window) and travels up
    # and to the left for z pixels
    points.append( ( MIDDLE_X, MIDDLE_Y,
                     MIDDLE_X - z_leg, MIDDLE_Y - z_leg ) )

    # This line starts at the end of the last line and travels down y pixels
    points.append( ( MIDDLE_X - z_leg, MIDDLE_Y - z_leg,
                     MIDDLE_X - z_leg, MIDDLE_Y + y - z_leg ) )

    # This line starts y pixels down from the origin and travels up and to the
    # left for z pixels
    points.append( ( MIDDLE_X, MIDDLE_Y + y,
                     MIDDLE_X - z_leg, MIDDLE_Y + y - z_leg ) )


    #==========================================================================
    # Finish top face
    #==========================================================================
    # This line starts at the top right corner of the right face and travels
    # up and to the left for z pixels
    points.append( ( MIDDLE_X + x_leg, MIDDLE_Y - x_leg,
                     MIDDLE_X + x_leg - z_leg, MIDDLE_Y - x_leg - z_leg ) )

    # This line starts at the top left corner of the left face and travels up
    # and to the right for x pixels
    points.append( ( MIDDLE_X + x_leg - z_leg, MIDDLE_Y - x_leg - z_leg,
                     MIDDLE_X - z_leg, MIDDLE_Y - z_leg ) )

    return points


#==============================================================================
def main( args ):
    """
    Script execution entry point

    @param args List of arguments passed to the script

                The second, third, and fourth items in the list should be the
                desired x, y, and z dimensions of the cube respectively

    @return Shell exit code (0 = success)
    """

    # Get the needed points from the project cube function
    cube = project_cube( args )

    # Initialize a window and canvas from the textbook's graphics module
    win = graphics.GraphicsWindow( WINDOW_X, WINDOW_Y )
    canvas = win.canvas()

    # Loop through each line and draw them using the graphics module
    for line in cube:
        canvas.drawLine( line[ 0 ], line[ 1 ], line[ 2 ], line[ 3 ] )

    # Prevent the created window from closing until the user pushes enter
    input()

    # Return success
    return 0


#==============================================================================
if __name__ == '__main__':
    # Check that the correct number of arguments has been given to the script
    # (The first argument is the name of the script)
    if len( sys.argv ) != 4:
        print( 'Usage: cubes.py [x] [y] [z]' )
    else:
        sys.exit( main( sys.argv ) )

