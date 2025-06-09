from EFieldSimulator.cls_point_charge import *
from numpy import linspace, zeros, meshgrid, quantile, copy
from matplotlib.pyplot import subplots, show, subplots_adjust

class electric_field_display:
    set_of_all_charges = point_charge.set_of_all_charges  # these lists are equivalent to each other
    def __init__(self, bound_xmin = 0.0, bound_ymin = 0.0, bound_xmax = 1.0, bound_ymax = 1.0, resolution = 10, name = ""):
        """Creates a new instance of an electric field display, specified the boundary coordinates and number of points per unit meter"""
        self.bound_xmin = bound_xmin
        self.bound_ymin = bound_ymin
        self.bound_xmax = bound_xmax
        self.bound_ymax = bound_ymax
        self.resolution = resolution
        self.name = name
        self.size_m, self.size_n = int((bound_xmax - bound_xmin) * resolution), int((bound_ymax - bound_ymin) * resolution)
        self.EField_x = zeros((self.size_m, self.size_n))
        self.EField_y = zeros((self.size_m, self.size_n))
        self.EPotential = zeros((self.size_m, self.size_n))
        self.has_computed_EField_x = False
        self.has_computed_EField_y = False
        self.has_computed_EPotential = False
        self.AllPotentials = []

    def display_EFieldLines(self, EFieldDensity = 1.0):
        # Generate the grid of points to evaluate the electric field on the cartesian plane:
        x, y = linspace(self.bound_xmin, self.bound_xmax, self.size_n), linspace(self.bound_ymin, self.bound_ymax, self.size_m)
        x, y = meshgrid(x, y)

        if (not self.has_computed_EField_x) or (not self.has_computed_EField_y):
            for j in range(self.size_m):
                for i in range(self.size_n):
                    pos_x, pos_y = x[j][i], y[j][i]
                    EField_xcomponent, EField_ycomponent = point_charge.total_EField(pos_x, pos_y)
                    self.EField_x[j][i] = EField_xcomponent
                    self.EField_y[j][i] = EField_ycomponent
            self.has_computed_EField_x = True
            self.has_computed_EField_y = True

        # Plot the electric field lines, with (+) charges in red, and (-) charges in blue
        fig, ax = subplots(figsize=(9,5))
        if len(self.name) == 0:
            ax.set_title("Electric Field Lines")
        else:
            ax.set_title(f"Electric Field Lines of {self.name}")
        ax.set(xlabel="Horizontal position x (m)", ylabel="Vertical position x (m)")
        ax.grid(visible=True, which='major', axis='both')
        ax.scatter([q.pos_x for q in point_charge.set_of_all_charges if q.sign_charge == +1.0],
                   [q.pos_y for q in point_charge.set_of_all_charges if q.sign_charge == +1.0], c='red', zorder=1)
        ax.scatter([q.pos_x for q in point_charge.set_of_all_charges if q.sign_charge == -1.0],
                   [q.pos_y for q in point_charge.set_of_all_charges if q.sign_charge == -1.0], c='blue', zorder=1)

        ax.streamplot(x, y, self.EField_x, self.EField_y, linewidth=1, density=EFieldDensity, zorder=0)
        show()
    def display_EPotential(self, max_number_of_potentials = 20, tuple_equipotentials=(), set_zero_potential = False, cutoff_threshold=10):
        # Generate the grid of points to evaluate the electric potential on the cartesian plane:
        x, y = linspace(self.bound_xmin, self.bound_xmax, self.size_n), linspace(self.bound_ymin, self.bound_ymax, self.size_m)
        x, y = meshgrid(x, y)

        if (not self.has_computed_EPotential):
            self.AllPotentials = []
            for j in range(self.size_m):
                for i in range(self.size_n):
                    pos_x, pos_y = x[j][i], y[j][i]
                    EPotential_value = point_charge.total_EPotential(pos_x, pos_y)
                    self.EPotential[j][i] = EPotential_value
                    self.AllPotentials.append(EPotential_value)
            self.has_computed_EPotential = True

        # Get the quantile values needed for the potentials
        number_of_quantiles = max_number_of_potentials # initial number of quantiles (excluding extrema)
        number_of_quantiles += 2  # accounts for the minimum and maximum values (which are excluded)

        # Sort all potential values
        self.AllPotentials.sort()

        # The top-most and bottom-most values will be removed
        # Get quantiles between cutoff_threshold% and (100 - cutoff_threshold)%
        lower_threshold = cutoff_threshold / 100
        upper_threshold = (100 - cutoff_threshold) / 100
        qValues = list(linspace(0, 1, number_of_quantiles))
        qValues = [q for q in qValues if ((q >= lower_threshold) and (q <= upper_threshold))]
        equipotential_levels = list(quantile(self.AllPotentials, qValues))

        # If the zero potential is to be set (True), let the lowest equipotential level be the zero potential.
        plotEPotential = copy(self.EPotential)
        if set_zero_potential:
            zero_potential = equipotential_levels[0]
            for j in range(self.size_m):
                for i in range(self.size_n):
                    plotEPotential[j][i] = plotEPotential[j][i] - zero_potential
            equipotential_levels = [potential - zero_potential for potential in equipotential_levels]

        # If specified, the equipotential levels can then be manually replaced:
        if len(tuple_equipotentials) != 0:
            equipotential_levels = list(tuple_equipotentials).copy()

        # Plot the equipotential lines
        fig, (ax, axbar) = subplots(ncols=2, gridspec_kw={'width_ratios': [13, 1]}, figsize=(9,5))
        if len(self.name) == 0:
            ax.set_title("Equipotential Lines")
        else:
            ax.set_title(f"Equipotential Lines of {self.name}")
        ax.set(xlabel="Horizontal position x (m)", ylabel="Vertical position x (m)")
        ax.grid(visible=True, which='major', axis='both')
        subplots_adjust(hspace=0.5)
        ax.scatter([q.pos_x for q in point_charge.set_of_all_charges if q.sign_charge == +1.0],
                   [q.pos_y for q in point_charge.set_of_all_charges if q.sign_charge == +1.0], c='red', zorder=1)
        ax.scatter([q.pos_x for q in point_charge.set_of_all_charges if q.sign_charge == -1.0],
                   [q.pos_y for q in point_charge.set_of_all_charges if q.sign_charge == -1.0], c='blue', zorder=1)
        equipotential_plot = ax.contour(x, y, plotEPotential, levels=equipotential_levels)
        fig.colorbar(equipotential_plot, axbar, label="Electric Potential (V)")
        ax.clabel(equipotential_plot, inline=False, fontsize=10, colors="black")
        show()

    def display_BothEFieldLines_EPotential (self, EFieldDensity = 1.0, max_number_of_potentials = 20, tuple_equipotentials=(), set_zero_potential = False, cutoff_threshold=10):
        # Generate the grid of points to evaluate the electric field and electric potential on the cartesian plane:
        x, y = linspace(self.bound_xmin, self.bound_xmax, self.size_n), linspace(self.bound_ymin, self.bound_ymax,
                                                                                 self.size_m)
        x, y = meshgrid(x, y)

        if (not self.has_computed_EField_x) or (not self.has_computed_EField_y) or (not self.has_computed_EPotential):
            self.AllPotentials = []
            for j in range(self.size_m):
                for i in range(self.size_n):
                    pos_x, pos_y = x[j][i], y[j][i]
                    EField_xcomponent, EField_ycomponent = point_charge.total_EField(pos_x, pos_y)
                    self.EField_x[j][i] = EField_xcomponent
                    self.EField_y[j][i] = EField_ycomponent
                    EPotential_value = point_charge.total_EPotential(pos_x, pos_y)
                    self.EPotential[j][i] = EPotential_value
                    self.AllPotentials.append(EPotential_value)
            self.has_computed_EField_x = True
            self.has_computed_EField_y = True
            self.has_computed_EPotential = True

        # Get the quantile values needed for the potentials
        number_of_quantiles = max_number_of_potentials  # initial number of quantiles (excluding extrema)
        number_of_quantiles += 2  # accounts for the minimum and maximum values (which are excluded)

        # Sort all potential values
        self.AllPotentials.sort()

        # The top-most and bottom-most values will be removed
        # Get quantiles between cutoff_threshold% and (100 - cutoff_threshold)%
        lower_threshold = cutoff_threshold / 100
        upper_threshold = (100 - cutoff_threshold) / 100
        qValues = list(linspace(0, 1, number_of_quantiles))
        qValues = [q for q in qValues if ((q >= lower_threshold) and (q <= upper_threshold))]
        equipotential_levels = list(quantile(self.AllPotentials, qValues))

        # If the zero potential is to be set (True), let the lowest equipotential level be the zero potential.
        plotEPotential = copy(self.EPotential)
        if set_zero_potential:
            zero_potential = equipotential_levels[0]
            for j in range(self.size_m):
                for i in range(self.size_n):
                    plotEPotential[j][i] = plotEPotential[j][i] - zero_potential
            equipotential_levels = [potential - zero_potential for potential in equipotential_levels]

        # If specified, the equipotential levels can then be manually replaced:
        if len(tuple_equipotentials) != 0:
            equipotential_levels = list(tuple_equipotentials).copy()

        # Plot the electric field lines and equipotential lines, with (+) charges in red, and (-) charges in blue
        fig, (ax, axbar) = subplots(ncols=2, gridspec_kw={'width_ratios': [13, 1]}, figsize=(9,5))
        if len(self.name) == 0:
            ax.set_title("Equipotential Lines")
        else:
            ax.set_title(f"Equipotential Lines of {self.name}")
        ax.set(xlabel="Horizontal position x (m)", ylabel="Vertical position x (m)")
        ax.grid(visible=True, which='major', axis='both')
        subplots_adjust(hspace=0.5)
        ax.scatter([q.pos_x for q in point_charge.set_of_all_charges if q.sign_charge == +1.0],
                   [q.pos_y for q in point_charge.set_of_all_charges if q.sign_charge == +1.0], c='red', zorder=1)
        ax.scatter([q.pos_x for q in point_charge.set_of_all_charges if q.sign_charge == -1.0],
                   [q.pos_y for q in point_charge.set_of_all_charges if q.sign_charge == -1.0], c='blue', zorder=1)
        equipotential_plot = ax.contour(x, y, plotEPotential, levels=equipotential_levels)
        fig.colorbar(equipotential_plot, axbar, label="Electric Potential (V)")

        ax.streamplot(x, y, self.EField_x, self.EField_y, linewidth=1, density=EFieldDensity, zorder=0, color="black")
        show()

    def display_EmptyPlot_1(self):
        fig, ax = subplots(figsize=(9,5))
        if len(self.name) == 0:
            ax.set_title("Electric Field Lines")
        else:
            ax.set_title(f"Electric Field Lines of {self.name}")
        ax.set(xlabel="Horizontal position x (m)", ylabel="Vertical position x (m)")
        ax.grid(visible=True, which='major', axis='both')
        ax.scatter([q.pos_x for q in point_charge.set_of_all_charges if q.sign_charge == +1.0],
                   [q.pos_y for q in point_charge.set_of_all_charges if q.sign_charge == +1.0], c='red', zorder=1)
        ax.scatter([q.pos_x for q in point_charge.set_of_all_charges if q.sign_charge == -1.0],
                   [q.pos_y for q in point_charge.set_of_all_charges if q.sign_charge == -1.0], c='blue', zorder=1)
        ax.set_xlim([self.bound_xmin, self.bound_xmax])
        ax.set_ylim([self.bound_ymin, self.bound_ymax])
        show()

    def display_EmptyPlot_2(self):
        fig, (ax, axbar) = subplots(ncols=2, gridspec_kw={'width_ratios': [13, 1]}, figsize=(9, 5))
        if len(self.name) == 0:
            ax.set_title("Equipotential Lines")
        else:
            ax.set_title(f"Equipotential Lines of {self.name}")
        ax.set(xlabel="Horizontal position x (m)", ylabel="Vertical position x (m)")
        ax.grid(visible=True, which='major', axis='both')
        subplots_adjust(hspace=0.5)
        ax.scatter([q.pos_x for q in point_charge.set_of_all_charges if q.sign_charge == +1.0],
                   [q.pos_y for q in point_charge.set_of_all_charges if q.sign_charge == +1.0], c='red', zorder=1)
        ax.scatter([q.pos_x for q in point_charge.set_of_all_charges if q.sign_charge == -1.0],
                   [q.pos_y for q in point_charge.set_of_all_charges if q.sign_charge == -1.0], c='blue', zorder=1)
        ax.set_xlim([self.bound_xmin, self.bound_xmax])
        ax.set_ylim([self.bound_ymin, self.bound_ymax])
        show()

    def allow_recomputation(self):
        self.has_computed_EField_x = False
        self.has_computed_EField_y = False
        self.has_computed_EPotential = False