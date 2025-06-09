from numpy import linspace
from EFieldSimulator.cls_point_charge import *

def chargedRod(charge=1.0, start_x=0.0, start_y=0.0, end_x=1.0, end_y=1.0, number_of_points=20):
    """Creates a set of point charges placed along a line"""
    pos_xrange = list(linspace(start_x, end_x, number_of_points))
    pos_yrange = list(linspace(start_y, end_y, number_of_points))
    pos_points = [(x, y) for x, y in zip(pos_xrange, pos_yrange)]
    charge_per_point = charge / number_of_points
    point_charges = []
    for point in pos_points:
        new_charge = point_charge(charge_per_point, point[0], point[1])
        point_charges.append(new_charge)
    return point_charges