from EFieldSimulator import *

# ----------------------------------------
# CASE #1 - Two Circles


# Declare first the electric charges
point_charge.clear()
e = point_charge.const_electronic_charge
conductorCharge = 1.65*e*(10**10)

chargedDisk(charge=conductorCharge,
            center_x = 8.0,
            center_y= 0.0,
            ring_diameter= 2.3,
            tuple_number_of_points=(6, 9, 12))
chargedDisk(charge=-conductorCharge,
            center_x = -8.0,
            center_y= 0.0,
            ring_diameter= 2.3,
            tuple_number_of_points=(6,9, 12))

# Plot the electric field lines and equipotential lines
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="Two Charged Circular Conductors")
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.5,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=True,
                                                 tuple_equipotentials=(0.00, 2.73, 4.40, 6.21, 8.0, 9.6, 12.05))
EFieldDisplay.display_EFieldLines(EFieldDensity=0.5)
EFieldDisplay.display_EmptyPlot_1()
EFieldDisplay.display_EPotential(set_zero_potential=True,
                                 max_number_of_potentials=9,
                                 tuple_equipotentials=(0.00, 2.73, 4.40, 6.21, 8.0, 9.6, 12.05))
EFieldDisplay.display_EmptyPlot_2()



# ----------------------------------------
# CASE #2 - Two Bars
# Declare first the electric charges

point_charge.clear()
e = point_charge.const_electronic_charge
conductorCharge = 4.70*e*(10**10)

chargedBar(-conductorCharge, -7.5, 5, 7.5, 5, 20, 4, 7.5)
chargedBar(conductorCharge, -7.5, -5, 7.5, -5, 20, 4, 7.5)

# Plot the electric field lines and equipotential lines
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="Two Charged Bar-Shaped Conductors")
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.5,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=True,
                                                 tuple_equipotentials=(0.00, 2.50, 4.86, 5.95, 7.00, 9.40, 12.00),
                                                 cutoff_threshold=26)
EFieldDisplay.display_EFieldLines(EFieldDensity=0.5)
EFieldDisplay.display_EmptyPlot_1()
EFieldDisplay.display_EPotential(set_zero_potential=True,
                                 max_number_of_potentials=9,
                                 tuple_equipotentials=(0.00, 2.50, 4.86, 5.95, 7.00, 9.40, 12.0),
                                 cutoff_threshold=26)
EFieldDisplay.display_EmptyPlot_2()
'''

# ----------------------------------------
# CASE #3 - Bar and Circle

'''
# Declare first the electric charges
point_charge.clear()
e = point_charge.const_electronic_charge
conductorCharge = 6.04*e*(10**10)

chargedBar(charge=-conductorCharge,
           start_x=-7.5,
           start_y=5,
           end_x=7.5,
           end_y=5,
           number_of_column_points=20,
           number_of_row_points=4,
           aspect_ratio=7.5)
chargedDisk(charge=conductorCharge,
            center_x = 0.0,
            center_y= -5.5,
            ring_diameter= 2.3,
            tuple_number_of_points=(6,9, 12))

# Plot the electric field lines and equipotential lines
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="A Charged Circular Conductor and A Charged Bar Conductor")
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.5,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=True,
                                                 cutoff_threshold=22,
                                                 tuple_equipotentials=(0.00, 2.00, 4.00, 5.30, 7.02, 8.70, 12.00))
EFieldDisplay.display_EFieldLines(EFieldDensity=0.5)
EFieldDisplay.display_EmptyPlot_1()
EFieldDisplay.display_EPotential(set_zero_potential=True,
                                 max_number_of_potentials=9,
                                 cutoff_threshold=22,
                                 tuple_equipotentials=(0.00, 2.00, 4.00, 5.30, 7.02, 8.70, 12.00))
EFieldDisplay.display_EmptyPlot_2()



# ----------------------------------------
# SPECIAL CASE: Electric Dipole

# Declare first the electric charges
point_charge.clear()
e = point_charge.const_electronic_charge
conductorCharge = 3*e*(10**10)

point_charge(charge=conductorCharge,
             position_x = -6.0,
             position_y = 0.0)

point_charge(charge=-conductorCharge,
             position_x = 6.0,
             position_y = 0.0)

# Plot the electric field lines and equipotential lines
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 25,
                                       name="Electric Dipole")
print(point_charge.total_EPotential(0.0, 0.70))
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.6,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=False,
                                                 cutoff_threshold=10)
EFieldDisplay.display_EFieldLines(EFieldDensity=0.6)
EFieldDisplay.display_EmptyPlot_1()
EFieldDisplay.display_EPotential(set_zero_potential=False,
                                 max_number_of_potentials=9,
                                 cutoff_threshold=10)
EFieldDisplay.display_EmptyPlot_2()

# ----------------------------------------
# SPECIAL CASE: Intersecting Equipotential Lines

# Declare first the electric charges

point_charge.clear()
e = point_charge.const_electronic_charge
conductorCharge = 3*e*(10**10)

chargedBar(charge=conductorCharge,
           start_x=-7.5,
           start_y=5,
           end_x=7.5,
           end_y=5,
           number_of_column_points=20,
           number_of_row_points=1,
           aspect_ratio=7.5)

point_charge(charge=conductorCharge,
             position_x = 0.0,
             position_y = -5.5)

# Plot the electric field lines and equipotential lines
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="Setup with Intersecting Equipotential Lines")
print(point_charge.total_EPotential(0.0, 0.70))
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.5,
                                                 max_number_of_potentials=15,
                                                 set_zero_potential=False,
                                                 cutoff_threshold=10,
                                                 tuple_equipotentials=(9, 10, 11, 12, 13, 14, 14.458, 15, 16, 17, 18, 19, 20))
EFieldDisplay.display_EFieldLines(EFieldDensity=0.5)
EFieldDisplay.display_EmptyPlot_1()
EFieldDisplay.display_EPotential(set_zero_potential=False,
                                 max_number_of_potentials=15,
                                 cutoff_threshold=10,
                                 tuple_equipotentials=(9, 10, 11, 12, 13, 14, 14.458, 15, 16, 17, 18, 19, 20))
EFieldDisplay.display_EmptyPlot_2()
