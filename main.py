import numpy as np 
import scipy as sp
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
from scipy.integrate import quad
from scipy.integrate import cumulative_trapezoid
from sympy import pprint
from sympy import Integral

# Numerical values
pi_numerical = np.pi
planck_constant = sc.Planck
boltzmann_constant = sc.Boltzmann
e_constant = sc.e
sun_radius_km = 432690 # Example: added units
speed_of_light = sc.c
sun_surface_temp_K = 5772 # Example: added units
distance_au = float(input("Distance from the sun (AU) = ")) # Example: added units
wavelength_nm = float(input("Wavelength (nm) = ")) # Example: added units
spacecraft_radius_m = float(input("Spacecraft Radius (m) = ")) # Example: added units

# Convert inputs to proper units
distance_m = distance_au * 149597870700  # 1 AU in meters
sun_radius_m = sun_radius_km * 1000  # Convert km to m

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
smp.init_printing(use_unicode=True)

sun_irradiance1 = 2 * pi_symbol* h_symbol* c_symbol**2/l_symbol**5
sun_irradiance2 = 1 / (e_symbol**(h_symbol*c_symbol/(l_symbol*k_symbol*st_symbol)) - 1)

sun_irradiance = sun_irradiance1 * sun_irradiance2
sun_area = 4*pi_symbol*sr_symbol**2
sphere_area = 4*pi_symbol*d_symbol**2
spacecraft_radius = pi_symbol*r_symbol**2

#f = ((sun_irradiance*sun_area)/sphere_area)*spacecraft_radius
#print("BETA** SYMBOLIC INTEGRAL:", Integral(f, l_symbol), "**BETA")
#print("BETA**Evaluated integral:", smp.integrate(f, l_symbol), "**BETA")

sun_irradiance3 = 2 * pi_numerical* planck_constant* speed_of_light**2/wavelength_nm**5
sun_irradiance4 = 1 / (e_constant**(planck_constant*speed_of_light/(wavelength_nm*boltzmann_constant*sun_surface_temp_K)) - 1)

sun_irradiance_numercal= sun_irradiance3 * sun_irradiance4
sun_area_final = 4*pi_numerical*sun_radius_m**2
sphere_area_final= 4*pi_numerical*distance_m**2
spacecraft_area = pi_numerical*spacecraft_radius_m**2

f = ((sun_irradiance_numercal*sun_area_final)/sphere_area_final)*spacecraft_area

lower_limit_nm = float(input("Integral Lower Limit (nm) = ")) # Example: added units
upper_limit_nm = float(input("Integral Upper Limit (nm) = ")) # Example: added units

# Validate inputs
if lower_limit_nm <= 0:
    print("Warning: Lower limit should be greater than 0 nm to avoid division by zero")
    lower_limit_nm = 1e-9  # Set to a very small positive value

# Symbolic definite integral (commented out for now, uncomment when needed)
# lower_limit = smp.symbols('lambda_min', real=True, positive=True)
# upper_limit = smp.symbols('lambda_max', real=True, positive=True)
# print("BETA** SYMBOLIC DEFINITE INTEGRAL:", Integral(f, (l_symbol, lower_limit, upper_limit)), "**BETA")

# Numerical integration preparation
def integrand(wavelength_nm):
    # Convert wavelength from nm to meters
    wavelength_m = wavelength_nm * 1e-9
    if wavelength_m == 0:
        return 0  # Avoid division by zero
    sun_irradiance3 = 2 * pi_numerical * planck_constant * speed_of_light**2 / wavelength_m**5
    sun_irradiance4 = 1 / (e_constant**(planck_constant*speed_of_light/(wavelength_m*boltzmann_constant*sun_surface_temp_K)) - 1)
    sun_irradiance_numerical = sun_irradiance3 * sun_irradiance4
    return ((sun_irradiance_numerical * sun_area_final) / (4*pi_numerical*distance_m**2)) * spacecraft_area

# Example of how to use numerical integration (commented out for now)

result, error = quad(integrand, lower_limit_nm, upper_limit_nm)
print(f"Numerical integration result: {result:.2e} W")
print(f"Integration error estimate: {error:.2e} W")
