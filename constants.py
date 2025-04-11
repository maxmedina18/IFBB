import numpy as np
import scipy.constants as sc

# Set numpy to use double precision
np.set_printoptions(precision=15)
np.seterr(all='raise')

# Physical constants with double precision
pi_numerical = np.float64(np.pi)
planck_constant = np.float64(sc.Planck)
boltzmann_constant = np.float64(sc.Boltzmann)
speed_of_light = np.float64(sc.c)
e_numerical = np.float64(sc.e)

# Sun properties
sun_surface_temp_K = np.float64(5772)
sun_radius_km = np.float64(432690)
AU_to_meters = np.float64(149597870700)  # 1 AU in meters 
