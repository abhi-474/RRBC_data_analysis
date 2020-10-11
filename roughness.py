# to calculate variation of ekman layer thickness which
# helps in designing roughness
#l_ek = 2.284 sqrt(nu= kinematic viscosity/omega = rotation rate)
#nu = 1.004 x 10-6, beta =207x10-6 both at 20 C.
#max=70 rpm.
#omega = 2 pi N /60
# ro = sqrt (ra/pr ta); ta = ek-2; ro =sqrt(g*beta*(del t/hght=0.2m))/2 omega;
#thermal diffu = 0.143 * 10 ** -6,

import numpy as np
import matplotlib.pyplot as plt

delt = 10
alpha = 0.143 * (10 ** (-6))
beta = (207 * (10**(-6)))  #delta T, temperature difference.
h = 0.2 #height of cell in meters
nu = 1.004 * (10**(-6))
pr = 6.86
omg = np.arange(0.5, 3, 0.5)
ra = (9.81 * beta * delt * (h**3)) / (nu * alpha)
kc = np.sqrt(ra / pr)
ro = []
lek = []
ek = []
r = []
rac = []
for t in range(len(omg)):
    ro.append((np.sqrt(9.81 * beta * (delt / h))) / (2 * omg[t]))
    ek.append(ro[t] /kc)
    lek.append(2.284 * 1000 * np.sqrt(nu / omg[t]))
    rac.append(8.6 * (ek[t] ** (-4/3)))
    r.append(ra / (8.6 * (ek[t] ** (-4/3))))

rot = (np.sqrt(9.81 * beta * (delt / h))) / (2 * 3)
ekt = rot / kc
#rot = 0.053107, ekt = 4.13509 10** -6
print(rot, ekt)
plt.plot(ro, lek)
plt.axvspan(0.053107, 0.198, 0.05, 0.59,  facecolor='g', alpha=0.5)
#plt.plot(ek, r)
plt.xlabel('Rossby number(Ro)')
plt.ylabel(r'$\delta_e (mm)$')
plt.show()
