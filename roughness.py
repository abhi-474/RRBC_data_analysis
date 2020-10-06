# to calculate variation of ekman layer thickness which
# helps in designing roughness
#l_ek = 2.284 sqrt(nu= kinematic viscosity/omega = rotation rate)
#nu = 1.004 x 10-6, beta =207x10-6 both at 20 C.
#max=70 rpm.
#omega = 2 pi N /60
# ro = sqrt (ra/pr ta); ta = ek-2; ro =sqrt(g*beta*(del t/hght=0.2m))/2 omega;

import numpy as np
import matplotlib.pyplot as plt

delt = 10
beta = (207 * (10**(-6)))  #delta T, temperature difference.
h = 0.2 #height of cell in meters
nu = 1.004 * (10**(-6))
omg = np.arange(0.5, 3, 0.5)
ro = []
lek = []
for t in range(len(omg)):
    ro.append((np.sqrt(9.81 * beta * (delt / h))) / (2* omg[t]))
    lek.append(2.284 * np.sqrt(nu / omg[t]))

plt.plot(ro, lek)
plt.show()
