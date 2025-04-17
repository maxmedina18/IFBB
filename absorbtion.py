import numpy as np
from scipy.integrate import quad
from space_constants import (
    pi_numerical,
    planck_constant,
    boltzmann_constant,
    speed_of_light,
    sun_surface_temp_K,
    sun_radius_km,
    AU_to_meters
)



def integrand(wavelength_nm, distance_m, sun_radius_m, spacecraft_radius_m, spectral_absorbance):
    """
    Calculate the integrand for the absorption calculation.
    
    Parameters:
    -----------
    wavelength_nm : float
        Wavelength in nanometers
    distance_m : float
        Distance from the sun in meters
    sun_radius_m : float
        Radius of the sun in meters
    spacecraft_radius_m : float
        Radius of the spacecraft in meters
    spectral_absorbance : float
        Spectral absorbance coefficient (0-1)
    
    Returns:
    --------
    float
        Spectral radiance at the given wavelength
    """
    # Convert wavelength to meters
    wavelength_m = np.float64(wavelength_nm) * np.float64(1e-9)
    if wavelength_m == 0:
        return np.float64(0)
    
    # Calculate spectral radiance using Planck's law
    numerator = np.float64(2) * pi_numerical * planck_constant * speed_of_light**2
    denominator = wavelength_m**5
    exponential_term = (planck_constant * speed_of_light / (wavelength_m * boltzmann_constant * sun_surface_temp_K))

    try:
        exp_val = np.exp(exponential_term)
        manager = exp_val - 1.0

        # Safeguard against numerical instability
        if manager > 1e50 or np.isinf(manager) or np.isnan(manager):
            spectral_radiance = 0.0
        elif manager < 1e-10:
            spectral_radiance = 0.0
        else:
            spectral_radiance = (numerator / denominator) * (1.0 / manager)

    except OverflowError:
        spectral_radiance = 0.0    
    # Calculate areas
    sun_area = np.float64(4) * pi_numerical * sun_radius_m**2
    spacecraft_area = pi_numerical * np.float64(spacecraft_radius_m)**2
    
    # Calculate power per unit wavelength
    power_per_wavelength = (spectral_radiance * sun_area) / (np.float64(4) * pi_numerical * distance_m**2) * spacecraft_area * spectral_absorbance
    
    return power_per_wavelength

def calculate_absorption(distance_au, spacecraft_radius_m, wavelength_range_nm, spectral_absorbance):
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
    spectral_absorbance : float
        Spectral absorbance coefficient (0-1)
    
    Returns:
    --------
    tuple
        (absorbed_power, error_estimate)
    """
    # Convert inputs to proper units
    distance_m = np.float64(distance_au * AU_to_meters)
    sun_radius_m = np.float64(sun_radius_km * 1000)
    
    # Create a wrapper function for quad that includes all parameters
    def integrand_wrapper(wavelength_nm):
        return integrand(wavelength_nm, distance_m, sun_radius_m, spacecraft_radius_m, spectral_absorbance)
    
    # Perform integration
    result, error = quad(integrand_wrapper, 
                        float(wavelength_range_nm[0]), 
                        float(wavelength_range_nm[1]),
                        epsabs=1e-10,
                        epsrel=1e-10,
                        limit=1000)
    
    # Multiply by 1e-9 to account for nm to m conversion
    return result * np.float64(1e-9), error * np.float64(1e-9)
