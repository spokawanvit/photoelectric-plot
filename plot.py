import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

wave_365 = np.loadtxt("/Users/supavit/Desktop/UCSB/Sophomore/Phys15C/365.txt", delimiter = ",")
I_365 = wave_365[:,0].ravel()
I_365_error = wave_365[:,1].ravel()
V_365 = -1*wave_365[:,2].ravel()

wave_436 = np.loadtxt("/Users/supavit/Desktop/UCSB/Sophomore/Phys15C/436.txt", delimiter = ",")
I_436 = wave_436[:,0].ravel()
I_436_error = wave_436[:,1].ravel()
V_436 = -1*wave_436[:,2].ravel()

wave_580 = np.loadtxt("/Users/supavit/Desktop/UCSB/Sophomore/Phys15C/580.txt", delimiter = ",")
I_580 = wave_580[:,0].ravel()
I_580_error = wave_580[:,1].ravel()
V_580 = -1*wave_580[:,2].ravel()

wave_546 = np.loadtxt("/Users/supavit/Desktop/UCSB/Sophomore/Phys15C/546.txt", delimiter = ",")
I_546 = wave_546[:,0].ravel()
I_546_error = wave_546[:,1].ravel()
V_546 = -1*wave_546[:,2].ravel()

plt.errorbar(V_365,I_365,yerr = I_365_error,label = r"$\nu = 365 nm$",linestyle = '--',marker = '*')
plt.errorbar(V_436,I_436,yerr = I_436_error,label = r"$\nu = 436 nm$",linestyle = '--',marker = '.')
plt.errorbar(V_580,I_580,yerr = I_580_error,label = r"$\nu = 580 nm$",linestyle = '--',marker = 'o')
plt.errorbar(V_546,I_546,yerr = I_546_error,label = r"$\nu = 580 nm$",linestyle = '--',marker = 'x')
plt.tick_params(which = 'both', direction='in',labelleft=False, labelright=True,left = 'off',right = 'on')
plt.xlabel("Voltage (mV)")
plt.ylabel("Current (nA)")
plt.legend()
plt.show()
