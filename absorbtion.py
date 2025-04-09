import numpy as np
from scipy.integrate import quad
from constants import (
    pi_numerical,
    planck_constant,
    boltzmann_constant,
    speed_of_light,
    sun_surface_temp_K,
    sun_radius_km,
    AU_to_meters
)

def integrand(wavelength_nm):
    # Convert wavelength from nm to meters
    wavelength_m = np.float64(wavelength_nm * 1e-9)
    if wavelength_m == 0:
        return np.float64(0)
    
    numerator = np.float64(2) * pi_numerical * planck_constant * speed_of_light**2
    denominator = wavelength_m**5
    exponential_term = planck_constant * speed_of_light / (wavelength_m * boltzmann_constant * sun_surface_temp_K)
    
    spectral_radiance = (numerator / denominator) * (np.float64(1) / (np.exp(exponential_term) - np.float64(1)))
    return spectral_radiance

def calculate_absorption(distance_au, spacecraft_radius_m, wavelength_range_nm):
    """
    Calculate the absorbed power from solar radiation.
    
    Parameters:
    -----------
    distance_au : float
        Distance from the sun in AU
    spacecraft_radius_m : float
        Radius of the spacecraft in meters
    wavelength_range_nm : tuple
        (lower_limit, upper_limit) in nanometers
    
    Returns:
    --------
    tuple
        (absorbed_power, error_estimate)
    """
    # Convert inputs to proper units
    distance_m = np.float64(distance_au * AU_to_meters)
    sun_radius_m = np.float64(sun_radius_km * 1000)
    
    # Calculate areas
    sun_area = np.float64(4) * pi_numerical * sun_radius_m**2
    spacecraft_area = pi_numerical * np.float64(spacecraft_radius_m)**2
    
    # Perform integration
    result, error = quad(integrand, 
                        float(wavelength_range_nm[0]), 
                        float(wavelength_range_nm[1]),
                        epsabs=1e-10,
                        epsrel=1e-10,
                        limit=1000)
    
    # Calculate total power
    total_power = (result * sun_area) / (np.float64(4) * pi_numerical * distance_m**2) * spacecraft_area
    
    return total_power, error 
