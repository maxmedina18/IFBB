import numpy as np 
import scipy as sp
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
from scipy.integrate import quad
from scipy.integrate import cumulative_trapezoid

# Numerical values
pi_numerical = np.pi
planck_constant = sc.Planck
boltzmann_constant = sc.Boltzmann
sun_radius_km = 432690 # Example: added units
speed_of_light = sc.c
sun_surface_temp_K = 5772 # Example: added units
distance_au = float(input("Distance from the sun (AU) = ")) # Example: added units
wavelength_nm = float(input("Wavelength (nm) = ")) # Example: added units
spacecraft_radius_m = float(input("Spacecraft Radius (m) = ")) # Example: added units

# Symbolic variables
pi_symbol = smp.symbols('pi', real=True, positive=True)
h_symbol = smp.symbols('h', real=True)
k_symbol = smp.symbols('k', real=True)
sr_symbol = smp.symbols('sr', real=True, positive=True)
c_symbol = smp.symbols('c', real=True, positive=True)
st_symbol = smp.symbols('st', real=True, positive=True)
d_symbol = smp.symbols('d', real=True, positive=True)
l_symbol = smp.symbols('l', real=True, positive=True)
r_symbol = smp.symbols('r', real=True, positive=True)
e_symbol = smp.symbols('e', real=True, positive=True)

sun_irradiance1 = 2 * pi_symbol* h_symbol* c_symbol**2/l_symbol**6
sun_irradiance2 = 1 / e_symbol**h_symbol*c_symbol/l_symbol*k_symbol*st_symbol-1

sun_irradiance = sun_irradiance1 * sun_irradiance2
sun_area = 4*pi_symbol*sr_symbol**2
sphere_area = 4*pi_symbol*d_symbol**2
spacecraft_radius = pi_symbol*r_symbol**2

f = ((sun_irradiance*sun_area)/sphere_area)*spacecraft_radius
print("BETA** SYMBOLIC INTEGRAL:",smp.integrate(f, l_symbol), " **BETA")
