from numpy import linspace
from math import cos, sin, pi
from EFieldSimulator.cls_point_charge import *

def chargedArc(charge=1.0, center_x=0.0, center_y=0.0, arc_radius=1.0, start_angle_deg = 0.0, width_angle_deg = 90.0, number_of_points=10):
    """Creates an array of point charges distributed radially within a charged arc with angle "width_angle_deg" degrees."""
    start_angle_rad = start_angle_deg * pi/180
    end_angle_rad = (start_angle_deg + width_angle_deg) * pi/180
    angles = list(linspace(start_angle_rad, end_angle_rad, number_of_points+1))

    point_charges = []
    charge_per_point = charge / number_of_points
    for angle in angles:
        pos_x = center_x + arc_radius*cos(angle)
        pos_y = center_y + arc_radius*sin(angle)
        point_charges.append(point_charge(charge_per_point, pos_x, pos_y))
    return point_charges