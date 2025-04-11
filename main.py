import sys
import os
import numpy as np

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from absorption import calculate_absorption, planck_constant
from emission import calculate_emission, planck_constant
from constants import AU_to_meters, sun_radius_km, pi_numerical, speed_of_light, boltzmann_constant, sun_surface_temp_K
from visualize import plot_absorbed_power

def calculate_spectral_power(wavelengths_nm, distance_au, spacecraft_radius_m, spectral_absorbance):
    """
    Calculate the spectral power distribution.
    
    Parameters:
    -----------
    wavelengths_nm : array-like
        Array of wavelengths in nanometers
    distance_au : float
        Distance from the sun in AU
    spacecraft_radius_m : float
        Radius of the spacecraft in meters
    spectral_absorbance : float
        Spectral absorbance coefficient (0-1)
    
    Returns:
    --------
    array-like
        Array of power values corresponding to each wavelength
    """
    # Convert inputs to proper units
    distance_m = np.float64(distance_au * AU_to_meters)
    sun_radius_m = np.float64(sun_radius_km * 1000)
    
    # Calculate areas
    sun_area = np.float64(4) * pi_numerical * sun_radius_m**2
    spacecraft_area = pi_numerical * np.float64(spacecraft_radius_m)**2
    
    # Calculate power for each wavelength
    power_values = []
    for wavelength_nm in wavelengths_nm:
        wavelength_m = np.float64(wavelength_nm) * np.float64(1e-9)
        if wavelength_m == 0:
            power_values.append(0)
            continue
            
        # Calculate spectral radiance using Planck's law
        numerator = np.float64(2) * pi_numerical * planck_constant * speed_of_light**2
        denominator = wavelength_m**5
        exponential_term = planck_constant * speed_of_light / (wavelength_m * boltzmann_constant * sun_surface_temp_K)
        
        spectral_radiance = (numerator / denominator) * (np.float64(1) / (np.exp(exponential_term) - np.float64(1)))
        
        # Calculate power
        power = (spectral_radiance * sun_area) / (np.float64(4) * pi_numerical * distance_m**2) * spacecraft_area * spectral_absorbance * np.float64(1e-9)
        power_values.append(power)
    
    return np.array(power_values)

def main():
    # Get user input
    distance_au = float(input("Distance from the sun (AU) = "))
    spacecraft_radius_m = float(input("Spacecraft Radius (m) = "))
    lower_limit_nm = float(input("Integral Lower Limit (nm) = "))
    upper_limit_nm = float(input("Integral Upper Limit (nm) = "))
    spectral_absorbance = float(input("Spectral Absorbance (0-1) = "))
    spectral_emittance= float(input("Spectral Irradiance (0-1) = "))
    spacecraft_temp_k= float(input("Spacecraft Temp = "))

    
    # Define wavelength range from user input
    wavelength_range = (lower_limit_nm, upper_limit_nm)
    
    # Calculate absorbed power
    absorbed_power, abs_error = calculate_absorption(
        distance_au=distance_au,
        spacecraft_radius_m=spacecraft_radius_m,
        wavelength_range_nm=wavelength_range,
        spectral_absorbance=spectral_absorbance
    )
    emitted_power, abs_error = calculate_emission(
        spacecraft_radius_m=spacecraft_radius_m,
        spacecraft_temp_K=spacecraft_temp_k, 
        wavelength_range_nm=wavelength_range
    )


    
    # Print results
    print("\nResults:")
    print(f"Absorbed Power: {absorbed_power:.3e} W ± {abs_error:.3e} kW")

    print("\nResults:")
    print(f"Power Emitted: {emitted_power:.3e} W ± {abs_error:.3e} kW")
    
    # Create wavelength array for visualization
    wavelengths = np.linspace(lower_limit_nm, upper_limit_nm, 1000)
    power_values = calculate_spectral_power(wavelengths, distance_au, spacecraft_radius_m, spectral_absorbance)
    
    # Plot the spectral power distribution
    plot_absorbed_power(wavelengths, power_values)

if __name__ == "__main__":
    main() 
    
