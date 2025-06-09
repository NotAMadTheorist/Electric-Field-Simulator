from numpy import linspace
from math import cos, sin
from EFieldSimulator.cls_point_charge import *

def chargedRing(charge=1.0, center_x=0.0, center_y=0.0, ring_diameter=1.0, number_of_points=10):
    """Creates an array of point charges distributed radially within a charged ring."""
    ring_radius = ring_diameter / 2
    angles = list(linspace(0, 2*pi, number_of_points+1))
    angles.pop()

    point_charges = []
    charge_per_point = charge / number_of_points
    for angle in angles:
        pos_x = center_x + ring_radius*cos(angle)
        pos_y = center_y + ring_radius*sin(angle)
        point_charges.append(point_charge(charge_per_point, pos_x, pos_y))
    return point_charges