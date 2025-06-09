from EFieldSimulator.func_chargedRing import *
from numpy import linspace

def chargedDisk(charge=1.0, center_x=0.0, center_y=0.0, ring_diameter=1.0, tuple_number_of_points = (6, 10)):

    # Create the central point charge
    number_of_points = sum(tuple_number_of_points) + 1
    charge_per_point = charge / number_of_points
    point_charges = []
    point_charges.append(point_charge(charge_per_point, center_x, center_y))

    # Create rings of charge around the central point charge
    number_of_rings = len(tuple_number_of_points)
    ring_radii = list(linspace(0, ring_diameter/2, number_of_rings + 1))
    ring_radii.pop(0)
    for i in range(number_of_rings):
        ring_radius, ring_points = ring_radii[i], tuple_number_of_points[i]
        point_charges = point_charges + chargedRing(charge*ring_points/number_of_points, center_x, center_y, ring_radius*2, ring_points)
    return point_charges