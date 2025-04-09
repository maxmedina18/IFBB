import numpy as np 
import scipy as sp
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
from scipy.integrate import quad
from scipy.integrate import cumulative_trapezoid
from sympy import pprint
from sympy import Integral

# Set numpy to use double precision
np.set_printoptions(precision=15)
np.seterr(all='raise')  # Raise exceptions for numerical errors

# Numerical values with explicit double precision
pi_numerical = np.float64(np.pi)
planck_constant = np.float64(sc.Planck)
boltzmann_constant = np.float64(sc.Boltzmann)
e_constant = np.float64(sc.e)
sun_radius_km = np.float64(432690)  # Example: added units
speed_of_light = np.float64(sc.c)
sun_surface_temp_K = np.float64(5772)  # Example: added units

# Input values with explicit double precision
distance_au = np.float64(float(input("Distance from the sun (AU) = ")))
wavelength_nm = np.float64(float(input("Wavelength (nm) = ")))
spacecraft_radius_m = np.float64(float(input("Spacecraft Radius (m) = ")))

# Convert inputs to proper units with double precision
distance_m = distance_au * np.float64(149597870700)  # 1 AU in meters
sun_radius_m = sun_radius_km * np.float64(1000)  # Convert km to m
wavelength_m = wavelength_nm * 1e-9

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

sun_irradiance_numerical = sun_irradiance3 * sun_irradiance4
sun_area_final = 4*pi_numerical*sun_radius_m**2
sphere_area_final = 4*pi_numerical*distance_m**2
spacecraft_area = pi_numerical*spacecraft_radius_m**2

lower_limit_nm = np.float64(float(input("Integral Lower Limit (nm) = ")))
upper_limit_nm = np.float64(float(input("Integral Upper Limit (nm) = ")))

# Validate inputs
if lower_limit_nm <= 0:
    print("Warning: Lower limit should be greater than 0 nm to avoid division by zero")
    lower_limit_nm = np.float64(1e-9)  # Set to a very small positive value

def integrand(wavelength_nm):
    # Convert wavelength from nm to meters with double precision
    wavelength_m = np.float64(wavelength_nm * 1e-9)
    if wavelength_m == 0:
        return np.float64(0)  # Avoid division by zero
    
    # Calculate Planck's law components with double precision
    numerator = np.float64(2) * pi_numerical * planck_constant * speed_of_light**2
    denominator = wavelength_m**5
    exponential_term = planck_constant * speed_of_light / (wavelength_m * boltzmann_constant * sun_surface_temp_K)
    
    # Calculate spectral radiance with double precision
    spectral_radiance = (numerator / denominator) * (np.float64(1) / (np.exp(exponential_term) - np.float64(1)))
    
    # Calculate total power with double precision
    power = (spectral_radiance * sun_area_final) / (np.float64(4) * pi_numerical * distance_m**2) * spacecraft_area
    
    return power * 1e-9

# Perform integration with double precision
result, error = quad(integrand, float(lower_limit_nm), float(upper_limit_nm), epsabs=1e-15, epsrel=1e-15)
print(f"Numerical integration result: {result:.15e} W")
print(f"Integration error estimate: {error:.15e} W")

