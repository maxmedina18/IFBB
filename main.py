import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from absorption import calculate_absorption

def main():
    # Get user input
    distance_au = float(input("Distance from the sun (AU) = "))
    spacecraft_radius_m = float(input("Spacecraft Radius (m) = "))
    lower_limit_nm = float(input("Integral Lower Limit (nm) = "))
    upper_limit_nm = float(input("Integral Upper Limit (nm) = "))
    spectral_absorbance = float(input("Spectral Absorbance (0-1) = "))
    
    # Define wavelength range from user input
    wavelength_range = (lower_limit_nm, upper_limit_nm)
    
    # Calculate absorbed power
    absorbed_power, abs_error = calculate_absorption(
        distance_au=distance_au,
        spacecraft_radius_m=spacecraft_radius_m,
        wavelength_range_nm=wavelength_range,
        spectral_absorbance=spectral_absorbance
    )
    
    # Print results
    print("\nResults:")
    print(f"Absorbed Power: {absorbed_power:.3e} W ± {abs_error:.3e} W")

if __name__ == "__main__":
    main() 
