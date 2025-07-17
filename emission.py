"""
Module for spacecraft emission calculations.
Calculates the thermal radiation emitted by the spacecraft using Planck's law.
"""

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


def calculate_emission(spacecraft_radius_m, spacecraft_temp_k, wavelength_range_nm,spectral_emittance):
    """
    Calculate the emitted power from the spacecraft.
    
    Parameters:
    -----------
    spacecraft_radius_m : float
        Radius of the spacecraft in meters
    spacecraft_temp_K : float
        Temperature of the sun in Kelvin
    wavelength_range_nm : tuple
        (lower_limit, upper_limit) in nanometers
    emissivity : float, optional
        Surface emissivity coefficient (default: 1.0)
    
    Returns:
    --------
    tuple
        (emitted_power, error_estimate)
    """
    spacecraft_area = 4*pi_numerical * np.float64(spacecraft_radius_m)**2
    
    def integrand(wavelength_nm):
        wavelength_m = np.float64(wavelength_nm * 1e-9)
        if wavelength_m == 0:
            return np.float64(0)
        
        numerator = np.float64(2) * pi_numerical * planck_constant * speed_of_light**2
        denominator = wavelength_m**5
        exponential_term = (planck_constant * speed_of_light / (wavelength_m * boltzmann_constant * spacecraft_temp_k))

        
        spectral_radiance = (numerator / denominator) * (np.float64(1) / (np.exp(exponential_term) - np.float64(1)))
        return spectral_radiance * spacecraft_area
    
    def integrand_wrapper(wavelength_nm):
        return integrand(wavelength_nm, spacecraft_radius_m, spacecraft_temp_k, wavelength_range_nm)
    
    # Perform integration
    result, error = quad(integrand,
                        float(wavelength_range_nm[0]),
                        float(wavelength_range_nm[1]),
                        epsabs=1e-10,
                        epsrel=1e-10,
                        limit=1000)
    
    return result * np.float64(1e-9), error * np.float64(1e-9)
