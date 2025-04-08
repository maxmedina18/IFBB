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





#x = smp.symbols('x', real=True)
#f = smp.sin(x)**3 * smp.exp(-5*x)
#print(smp.integrate(f, x))






