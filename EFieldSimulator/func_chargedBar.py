from EFieldSimulator.func_chargedRod import *
from numpy import linspace

def chargedBar(charge=1.0, start_x=0.0, start_y=0.0, end_x=1.0, end_y=1.0, number_of_column_points=20, number_of_row_points=1, aspect_ratio=10.0):
    """Creates an array of point charges (number_of_column_points x number_of_row_points) placed in a bar with a specified aspect ratio"""

    if number_of_row_points == 1:
        point_charges = chargedRod(charge, start_x, start_y, end_x, end_y, number_of_column_points)
        return point_charges

    # Compute the following quantities related to the difference in position between the start and end points
    disp_xdiff = end_x - start_x
    disp_ydiff = end_y - start_y
    bar_length = sqrt(disp_xdiff ** 2 + disp_ydiff ** 2)
    bar_width = bar_length / aspect_ratio

    # Translate the start and end points to get the edges of the bar
    translation_width = bar_width/2
    translation_xdiff = translation_width * disp_ydiff/bar_length
    translation_ydiff = translation_width * (-disp_xdiff)/bar_length

    # Get the starting and ending x and y values for each row of the bar
    start_xvalues = list(linspace(start_x - translation_xdiff, start_x + translation_xdiff, number_of_row_points))
    start_yvalues = list(linspace(start_y - translation_ydiff, start_y + translation_ydiff, number_of_row_points))
    end_xvalues = list(linspace(end_x - translation_xdiff, end_x + translation_xdiff, number_of_row_points))
    end_yvalues = list(linspace(end_y - translation_ydiff, end_y + translation_ydiff, number_of_row_points))

    point_charges = []
    # Generate the point charges along each row by invoking the charged rod function
    charge_per_row = charge / number_of_row_points
    for i in range(number_of_row_points):
        point_charges = point_charges + chargedRod(charge_per_row, start_xvalues[i], start_yvalues[i], end_xvalues[i], end_yvalues[i], number_of_column_points)
    return point_charges