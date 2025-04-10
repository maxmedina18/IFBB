# bbs/visualize.py
import matplotlib.pyplot as plt
import numpy as np

def plot_absorbed_power(wavelengths, power_values):
    """
    Plot the spectral distribution of the absorbed power.
    
    Parameters:
    - wavelengths: array-like, wavelengths in nm
    - power_values: array-like, absorbed power corresponding to each wavelength
    """
    plt.figure(figsize=(10, 6))
    plt.plot(wavelengths, power_values, label='Absorbed Power')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Power (W)')
    plt.title('Spectral Distribution of Absorbed Power')
    
    # Format y-axis with scientific notation
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    
    # Add grid for better readability
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    
    # Add legend
    plt.legend()
    
    # Ensure tight layout
    plt.tight_layout()
    
    plt.show()
