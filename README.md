# IFBB
This is a symbolic and Numerical integrator that i am using to find values for absorption and emission of blackbodies for space craft cooling systems. 

# Blackbody Radiation Integrator

This project provides symbolic and numerical tools to compute absorption and emission values for blackbodies — specifically designed for **spacecraft thermal control systems**. These calculations are critical for designing effective radiative cooling systems in space, where conduction and convection are negligible.

---

## Overview

Spacecraft rely on radiative cooling to manage onboard temperatures. This tool computes:

- **Absorbed Power**: Based on incident solar radiation and surface absorptivity
- **Emitted Power**: Derived from Planck’s law and surface temperature
- **Symbolic & Numerical Methods**: For generality and real-world simulations

Built with:
- `SymPy` for symbolic integration
- `NumPy` and `SciPy` for numerical evaluation
- Optional: `Matplotlib` for spectrum visualization

---

## Features

- Symbolic expressions for blackbody radiation
- Numerical integration across wavelength or frequency domains
- Custom material absorptivity/emissivity support
- Configurable temperature and solar input parameters
- Designed for both blackbody and graybody analysis

---

## Use Cases

- Satellite radiator design and passive cooling
- Evaluation of high-emissivity/low-absorptivity surface coatings
- Thermal regulation optimization for deep-space systems

---

## Requirements

Install dependencies with:

```bash
pip install sympy numpy scipy matplotlib



Author : Maximiliano Medina
Physics + Computer Science | UTRGV SEER LEADER
