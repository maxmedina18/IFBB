import FreeSimpleGUI as sg
import numpy as np
import matplotlib as plt
plt.use("TkAgg")
from space_constants import pi_numerical, speed_of_light, planck_constant, boltzmann_constant
from absorption import calculate_absorption
from emission import calculate_emission
from visualize import plot_absorbed_power

# Stefan–Boltzmann constant
stefan_boltzmann = 5.670374419e-8

# Input layout
layout = [
    [sg.Text("Distance from Sun (AU):"), sg.InputText(key="distance_au")],
    [sg.Text("Spacecraft Radius (m):"), sg.InputText(key="radius_m")],
    [sg.Text("Wavelength Lower Limit (nm):"), sg.InputText(key="wl_lower")],
    [sg.Text("Wavelength Upper Limit (nm):"), sg.InputText(key="wl_upper")],
    [sg.Text("Spectral Absorbance (0-1):"), sg.InputText(key="absorbance")],
    [sg.Text("Spectral Emittance (0-1):"), sg.InputText(key="emittance")],
    [sg.Text("Spacecraft Temperature (K):"), sg.InputText(key="temp_K")],
    [sg.Button("Run Simulation"), sg.Button("Exit")],
    [sg.Text("Results:", font="Any 12 bold")],
    [sg.Multiline(size=(60, 10), key="output", disabled=True)],
]

window = sg.Window("Spacecraft Thermal Simulation", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Run Simulation":
        try:
            # Parse inputs
            d = float(values["distance_au"])
            r = float(values["radius_m"])
            wl_lo = float(values["wl_lower"])
            wl_hi = float(values["wl_upper"])
            a = float(values["absorbance"])
            e = float(values["emittance"])
            T = float(values["temp_K"])

            # Input validation
            if r <= 0 or wl_lo <= 0 or wl_hi <= wl_lo or not (0 <= a <= 1) or not (0 <= e <= 1) or T <= 0:
                raise ValueError("Invalid input values.")
            # Calculate powers
            absorbed, absorbed_err = calculate_absorption(d, r, (wl_lo, wl_hi), a)
            emitted, emitted_err = calculate_emission(r, T, (wl_lo, wl_hi), e)

            # Stefan–Boltzmann total power
            area = 4 * pi_numerical * r ** 2
            stefan_total = e * stefan_boltzmann * area * T ** 4

            # Output results
            result = f"""
Absorbed Power: {absorbed:.3e} W ± {absorbed_err:.2e}
Emitted Power (Integrated): {emitted:.3e} W ± {emitted_err:.2e}
Cross Refrence (Stefan-Boltzmann): {stefan_total:.3e} W
Δ Emission (Integrated vs Stefan-Boltzmann): {abs(emitted - stefan_total):.3e} W
"""
            window["output"].update(result)

            # Optional: show plot
            wavelengths = np.linspace(wl_lo, wl_hi, 500)
            from main import calculate_spectral_power
            powers = calculate_spectral_power(wavelengths, d, r, a)
            plot_absorbed_power(wavelengths, powers)

        except Exception as ex:
            sg.popup_error("Something went wrong:", str(ex))

window.close()
