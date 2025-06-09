from EFieldSimulator import *
from numpy import linspace
from matplotlib.pyplot import subplots, show
from math import sqrt, pi

# Declare constants for all examples
permittivity = point_charge.const_permittivity
k_constant = 1 / (4*pi*permittivity)
e = point_charge.const_electronic_charge
conductorCharge = 1.65*e*(10**10)


# ---------------------------------------------
# Problem 2: Positively Charged Rod of Length L

# Declare the charges involved
L = 4
point_charge.clear()
linearChargeDensity = conductorCharge / L
chargedRod(charge=conductorCharge,
           start_x=-L/2,
           start_y=0,
           end_x=L/2,
           end_y=0,
           number_of_points=30)

# General field and potential
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="Positively Charged Rod of Length L")
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.5,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=True)

# 2A: Axis perpendicular to the endpoint
number_obs_points = 80
obs_point_y = list(linspace(0, 7, number_obs_points))
obs_point_y.pop(0)
obs_EField_x = []
obs_EField_y = []
for obs_pos_y in obs_point_y:
    EField_x, EField_y = point_charge.total_EField(L/2, obs_pos_y)
    obs_EField_x.append(EField_x)
    obs_EField_y.append(EField_y)
obs_EField_mag = [sqrt(x**2 + y**2) for x, y in zip(obs_EField_x, obs_EField_y)]

predicted_EField_x = [k_constant*conductorCharge/L *((1/a) - 1/sqrt(a**2 + L**2)) for a in obs_point_y]
predicted_EField_y = [k_constant*conductorCharge/(a*sqrt(a**2 + L**2)) for a in obs_point_y]
predicted_EField_mag = [sqrt(x**2 + y**2) for x, y in zip(predicted_EField_x, predicted_EField_y)]


fig, ax = subplots(ncols=1, figsize=(9, 5))
ax.set_title("E-Field Magnitude along Axis Perpendicular to the Endpoint (7, 0)")
ax.set(xlabel="Vertical Position y (m)", ylabel="Electric Field Magnitude (V/m)")
ax.grid(visible=True, which='major', axis='both')
ax.plot(obs_point_y, obs_EField_mag, color="r", label="Simulated EField Magnitude")
ax.plot(obs_point_y, predicted_EField_mag, color="g", label="Theoretical EField Magnitude")
ax.legend()
show()


# 2B: Axis perpendicular to the midpoint
number_obs_points = 80
obs_point_y = list(linspace(0, 7, number_obs_points))
obs_point_y.pop(0)
obs_EField_x = []
obs_EField_y = []
for obs_pos_y in obs_point_y:
    EField_x, EField_y = point_charge.total_EField(0, obs_pos_y)
    obs_EField_x.append(EField_x)
    obs_EField_y.append(EField_y)
obs_EField_mag = [sqrt(x**2 + y**2) for x, y in zip(obs_EField_x, obs_EField_y)]

predicted_EField_x = [0 for a in obs_point_y]
predicted_EField_y = [2*k_constant*conductorCharge/(a*sqrt(4*a**2 + L**2))  for a in obs_point_y]
predicted_EField_mag = [sqrt(x**2 + y**2) for x, y in zip(predicted_EField_x, predicted_EField_y)]


fig, ax = subplots(ncols=1, figsize=(9, 5))
ax.set_title("E-Field Magnitude along Axis Perpendicular to the Midpoint (0, 0)")
ax.set(xlabel="Vertical Position y (m)", ylabel="Electric Field Magnitude (V/m)")
ax.grid(visible=True, which='major', axis='both')
ax.plot(obs_point_y, obs_EField_mag, color="r", label="Simulated EField Magnitude")
ax.plot(obs_point_y, predicted_EField_mag, color="g", label="Theoretical EField Magnitude")
ax.legend()
show()


# 2C: Axis along the rod itself
number_obs_points = 100
obs_point_x = list(linspace(L/2, 10, number_obs_points))
obs_point_x.pop(0)
obs_EField_x = []
obs_EField_y = []
for obs_pos_x in obs_point_x:
    EField_x, EField_y = point_charge.total_EField(obs_pos_x, 0)
    obs_EField_x.append(EField_x)
    obs_EField_y.append(EField_y)
obs_EField_mag = [sqrt(x**2 + y**2) for x, y in zip(obs_EField_x, obs_EField_y)]

predicted_EField_x = [4*k_constant*conductorCharge / (4*a**2 - L**2) for a in obs_point_x]
predicted_EField_y = [0 for a in obs_point_x]
predicted_EField_mag = [sqrt(x**2 + y**2) for x, y in zip(predicted_EField_x, predicted_EField_y)]


fig, ax = subplots(ncols=1, figsize=(9, 5))
ax.set_title("E-Field Magnitude along Axis of the Rod Itself")
ax.set(xlabel="Horizontal Position x (m)", ylabel="Electric Field Magnitude (V/m)")
ax.grid(visible=True, which='major', axis='both')
ax.plot(obs_point_x, obs_EField_mag, color="r", label="Simulated EField Magnitude")
ax.plot(obs_point_x, predicted_EField_mag, color="g", label="Theoretical EField Magnitude")
ax.legend()
show()
'''

# ---------------------------------------------
# Problem 3: Electric Dipole with Two Charged Rods

'''
# Declare the charges involved
point_charge.clear()
L = 5
chargedRod(charge=-conductorCharge,
           start_x=-L,
           start_y=0,
           end_x=0,
           end_y=0,
           number_of_points=30)
chargedRod(charge=conductorCharge,
           start_x=0,
           start_y=0,
           end_x=L,
           end_y=0,
           number_of_points=30)

# General field and potential
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="Electric Dipole with Two Charged Rods")
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.8,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=True)

# 3A: Axis perpendicular to the midpoint
number_obs_points = 80
obs_point_y = list(linspace(0, 7, number_obs_points))
obs_point_y.pop(0)
obs_EField_x = []
obs_EField_y = []
for obs_pos_y in obs_point_y:
    EField_x, EField_y = point_charge.total_EField(0, obs_pos_y)
    obs_EField_x.append(EField_x)
    obs_EField_y.append(EField_y)
obs_EField_mag = [sqrt(x**2 + y**2) for x, y in zip(obs_EField_x, obs_EField_y)]

predicted_EField_x = [-2*k_constant*conductorCharge/L*(1/a - 1/sqrt(a**2 + L**2)) for a in obs_point_y]
predicted_EField_y = [0 for a in obs_point_y]
predicted_EField_mag = [sqrt(x**2 + y**2) for x, y in zip(predicted_EField_x, predicted_EField_y)]


fig, ax = subplots(ncols=1, figsize=(9, 5))
ax.set_title("E-Field Magnitude along Axis Perpendicular to the Midpoint (0, 0)")
ax.set(xlabel="Vertical Position y (m)", ylabel="Electric Field Magnitude (V/m)")
ax.grid(visible=True, which='major', axis='both')
ax.plot(obs_point_y, obs_EField_mag, color="r", label="Simulated EField Magnitude")
ax.plot(obs_point_y, predicted_EField_mag, color="g", label="Theoretical EField Magnitude")
ax.legend(loc="upper right")
show()

# ---------------------------------------------
# Problem 4: Electric Dipole with Two Charged Quarter Arcs

# Declare the charges involved
point_charge.clear()
r = 6
chargedArc(charge=+conductorCharge,
           center_x = 0.0,
           center_y = 0.0,
           arc_radius = r,
           start_angle_deg = 90.0,
           width_angle_deg = 90.0,
           number_of_points = 30)
chargedArc(charge=-conductorCharge,
           center_x = 0.0,
           center_y = 0.0,
           arc_radius = r,
           start_angle_deg = 0.0,
           width_angle_deg = 90.0,
           number_of_points = 30)

# General field and potential
EFieldDisplay = electric_field_display(bound_xmin = -10.0,
                                       bound_ymin = -7.0,
                                       bound_xmax = 10.0,
                                       bound_ymax = 7.0,
                                       resolution = 15,
                                       name="Electric Dipole with Two Charged Quarter Arcs")
EFieldDisplay.display_BothEFieldLines_EPotential(EFieldDensity=0.8,
                                                 max_number_of_potentials=9,
                                                 set_zero_potential=True)

# At the center point (Electric field should be zero)
obs_EField_x_val, obs_EField_y_val = point_charge.total_EField(0, 0)
obs_EField_mag_val = sqrt(obs_EField_x_val**2 + obs_EField_y_val**2)
expected_EField_x_val, expected_EField_y_val = 4*k_constant*conductorCharge / (pi*r**2), 0
expected_EField_mag_val = sqrt(expected_EField_x_val**2 + expected_EField_y_val**2)

print(f"At the center point (0,0), \n"
      f"Simulated EField = {obs_EField_x_val} [V/m] (i) + {obs_EField_y_val} [V/m] (j) \n"
      f"Simulated EField magnitude = {obs_EField_mag_val} [V/m] \n \n"
      f"Theoretical EField = {expected_EField_x_val} [V/m] (i) + {expected_EField_y_val} [V/m] (j) \n"
      f"Theoretical EField magnitude = {expected_EField_mag_val} [V/m]")





