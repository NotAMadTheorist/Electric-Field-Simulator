from EFieldSimulator import *
from math import sqrt, pi

# Declare constants for all examples
permittivity = point_charge.const_permittivity
k_constant = 1 / (4*pi*permittivity)
e = point_charge.const_electronic_charge
conductorCharge = 1.65*e*(10**10)

# ---------------------------------------------
# Problem 8: Four Point Charges at Corners of a Square
# Case I: If all charges are positive

q = 2*10**(-6)  # in units of Coulombs
L = 4 # in units of meters
Lhalf = L/2

# Declare all charges involved
point_charge.clear()
point_charge(charge=q,
             position_x = -Lhalf,
             position_y = -Lhalf)
point_charge(charge=q,
             position_x = -Lhalf,
             position_y = Lhalf)
point_charge(charge=q,
             position_x = Lhalf,
             position_y = Lhalf)
point_charge(charge=q,
             position_x = Lhalf,
             position_y = -Lhalf)

# General field and potential
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="Four Point Charges (all +) at the Corners of a Square")
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.8,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=False) # Potential can be (+) or (-)

# At the center point (0,0)
obs_EField_x_val, obs_EField_y_val = point_charge.total_EField(0, 0)
obs_EField_mag_val = sqrt(obs_EField_x_val**2 + obs_EField_y_val**2)
obs_EPotential = point_charge.total_EPotential(0, 0)
expected_EField_x_val, expected_EField_y_val = 0.0, 0.0
expected_EField_mag_val = sqrt(expected_EField_x_val**2 + expected_EField_y_val**2)
expected_EPotential = 4*sqrt(2)*k_constant*q/L

print(f"At the center point (0,0), \n"
      f"Simulated EField = {obs_EField_x_val} [V/m] (i) + {obs_EField_y_val} [V/m] (j) \n"
      f"Simulated EField magnitude = {obs_EField_mag_val} [V/m] \n"
      f"Simulated EPotential = {obs_EPotential} [V] \n \n"
      f"Theoretical EField = {expected_EField_x_val} [V/m] (i) + {expected_EField_y_val} [V/m] (j) \n"
      f"Theoretical EField magnitude = {expected_EField_mag_val} [V/m] \n"
      f"Theoretical EPotential = {expected_EPotential} [V]")
print("-------------------------------------------------------- \n")


# ---------------------------------------------
# Problem 8: Four Point Charges at Corners of a Square
# Case II: If three charges are positive, one charge is negative

q = 2*10**(-6)  # in units of Coulombs
L = 4 # in units of meters
Lhalf = L/2

# Declare all charges involved
point_charge.clear()
point_charge(charge=q,
             position_x = -Lhalf,
             position_y = -Lhalf)
point_charge(charge=q,
             position_x = -Lhalf,
             position_y = Lhalf)
point_charge(charge=-q,
             position_x = Lhalf,
             position_y = Lhalf)
point_charge(charge=q,
             position_x = Lhalf,
             position_y = -Lhalf)

# General field and potential
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="Four Point Charges (all +) at the Corners of a Square")
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.8,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=False) # Potential can be (+) or (-)

# At the center point (0,0)
obs_EField_x_val, obs_EField_y_val = point_charge.total_EField(0, 0)
obs_EField_mag_val = sqrt(obs_EField_x_val**2 + obs_EField_y_val**2)
obs_EPotential = point_charge.total_EPotential(0, 0)
expected_EPotential = 2*sqrt(2)*k_constant*q/L

print(f"At the center point (0,0), \n"
      f"Simulated EField = {obs_EField_x_val} [V/m] (i) + {obs_EField_y_val} [V/m] (j) \n"
      f"Simulated EField magnitude = {obs_EField_mag_val} [V/m] \n"
      f"Simulated EPotential = {obs_EPotential} [V] \n \n"
      f"Theoretical EPotential = {expected_EPotential} [V]")
print("-------------------------------------------------------- \n")

# ---------------------------------------------
# Problem 8: Four Point Charges at Corners of a Square
# Case III: If two charges are positive, two charges are negative (opposite sides)

q = 2*10**(-6)  # in units of Coulombs
L = 4 # in units of meters
Lhalf = L/2

# Declare all charges involved
point_charge.clear()
point_charge(charge=-q,
             position_x = -Lhalf,
             position_y = -Lhalf)
point_charge(charge=q,
             position_x = -Lhalf,
             position_y = Lhalf)
point_charge(charge=-q,
             position_x = Lhalf,
             position_y = Lhalf)
point_charge(charge=q,
             position_x = Lhalf,
             position_y = -Lhalf)

# General field and potential
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="Four Point Charges (all +) at the Corners of a Square")
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.8,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=False) # Potential can be (+) or (-)

# At the center point (0,0)
obs_EField_x_val, obs_EField_y_val = point_charge.total_EField(0, 0)
obs_EField_mag_val = sqrt(obs_EField_x_val**2 + obs_EField_y_val**2)
obs_EPotential = point_charge.total_EPotential(0, 0)
expected_EField_x_val, expected_EField_y_val = 0.0, 0.0
expected_EField_mag_val = sqrt(expected_EField_x_val**2 + expected_EField_y_val**2)
expected_EPotential = 0.0

print(f"At the center point (0,0), \n"
      f"Simulated EField = {obs_EField_x_val} [V/m] (i) + {obs_EField_y_val} [V/m] (j) \n"
      f"Simulated EField magnitude = {obs_EField_mag_val} [V/m] \n"
      f"Simulated EPotential = {obs_EPotential} [V] \n \n"
      f"Theoretical EField = {expected_EField_x_val} [V/m] (i) + {expected_EField_y_val} [V/m] (j) \n"
      f"Theoretical EField magnitude = {expected_EField_mag_val} [V/m] \n"
      f"Theoretical EPotential = {expected_EPotential} [V]")
print("-------------------------------------------------------- \n")

# ---------------------------------------------
# Problem 8: Four Point Charges at Corners of a Square
# Case IV: If two charges are positive, two charges are negative (same side)

q = 2*10**(-6)  # in units of Coulombs
L = 4 # in units of meters
Lhalf = L/2

# Declare all charges involved
point_charge.clear()
point_charge(charge=-q,
             position_x = -Lhalf,
             position_y = -Lhalf)
point_charge(charge=-q,
             position_x = -Lhalf,
             position_y = Lhalf)
point_charge(charge=q,
             position_x = Lhalf,
             position_y = Lhalf)
point_charge(charge=q,
             position_x = Lhalf,
             position_y = -Lhalf)

# General field and potential
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="Four Point Charges (all +) at the Corners of a Square")
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.8,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=False) # Potential can be (+) or (-)

# At the center point (0,0)
obs_EField_x_val, obs_EField_y_val = point_charge.total_EField(0, 0)
obs_EField_mag_val = sqrt(obs_EField_x_val**2 + obs_EField_y_val**2)
obs_EPotential = point_charge.total_EPotential(0, 0)
expected_EField_x_val, expected_EField_y_val = 0.0, 0.0
expected_EField_mag_val = sqrt(expected_EField_x_val**2 + expected_EField_y_val**2)
expected_EPotential = 0.0

print(f"At the center point (0,0), \n"
      f"Simulated EField = {obs_EField_x_val} [V/m] (i) + {obs_EField_y_val} [V/m] (j) \n"
      f"Simulated EField magnitude = {obs_EField_mag_val} [V/m] \n"
      f"Simulated EPotential = {obs_EPotential} [V] \n \n"
      f"Theoretical EField = {expected_EField_x_val} [V/m] (i) + {expected_EField_y_val} [V/m] (j) \n"
      f"Theoretical EField magnitude = {expected_EField_mag_val} [V/m] \n"
      f"Theoretical EPotential = {expected_EPotential} [V]")
print("-------------------------------------------------------- \n")

# ---------------------------------------------
# Problem 9: Assembling Row of Alternating Charge (UNFINISHED)
q = conductorCharge  # in units of Coulombs
a = 1 # in units of meters

# First two charged particles I (+) and II (+)
point_charge.clear()
point_charge(charge=+q,
             position_x = -a,
             position_y = 0)
point_charge(charge=+q,
             position_x = a,
             position_y = 0)

cumulative_work_applied = 0.0
# to be done...

# First three charged particles (+), (-), and (+) (UNFINISHED)


# Generalizing to an infinite row (vary with length "a") (UNFINISHED)


# ---------------------------------------------
# Simulation of an Ionic Solid (Born-Lande and Born-Mayer Equations) (UNFINISHED)




