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

V_intercept = 0.001*np.array([V_365[-1],V_436[-1],V_546[-1],V_580[-1]])
lamda = np.array([365.0,436.0,546.0,580.0])*(10**-9)
fre = 299792458/lamda

# Linear regression
def line(x,m,intercept):
    return m*x+intercept

popt, pcov = curve_fit(line,fre,V_intercept)
smooth = np.linspace(fre[0],fre[-1],1000)
q_e = 1.60217*(10**-19)
hphi = q_e*popt
print("h = %s and phi = %s" % (hphi[0],hphi[1]))

plt.plot(fre,V_intercept,linestyle = 'none',marker = '*')
plt.plot(smooth,line(smooth,*popt))
plt.show()
