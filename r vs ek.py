
import numpy as np
import matplotlib.pyplot as plt

# to calculate variation of ekman layer thickness which
# helps in designing roughness
#l_ek = 2.284 sqrt(nu= kinematic viscosity/omega = rotation rate)
#nu = 1.004 x 10-6, beta =207x10-6 both at 20 C.
#max=70 rpm.
#omega = 2 pi N /60
# ro = sqrt (ra/pr ta); ta = ek-2; ro =sqrt(g*beta*(del t/hght=0.2m))/2 omega;
#ro =ek sqrt(ra/pr), pr = 6.4
#r12 = ((ro **2) / (ek**2)) * (pr / rac) or ro = 2 (nimela 2014)
#thermal diffu = 0.143 * 10 ** -6,

ek = list(np.logspace(-7, -3, num=1500))
pr = 6.8
delt = 10
alpha = 0.143 * (10 ** (-6))
beta = (207 * (10**(-6)))  #delta T, temperature difference.
h = 0.2 #height of cell in meters
nu = 1.004 * (10**(-6))
omg = np.arange(0.5, 3, 0.5)
ra = (9.81 * beta * delt * (h**3)) / (nu * alpha)
kc = np.sqrt(ra / pr)
ro = []
r = []
rac = []
r12 = []
r23 = []
rnt =[]
ek1 =[]
for t in range(len(ek)):
    rac.append(8.6 * (ek[t] ** (-4/3)))
    r12.append(((2 ** 2) / (ek[t] ** 2)) * (pr / rac[t]))
    r23.append((0.3 * (ek[t] ** (-1.8))) / (rac[t]))
    rnt.append(3)

for t in range(len(omg)):
    ro.append((np.sqrt(9.81 * beta * (delt / h))) / (2 * omg[t]))
    ek1.append((ro[t]) / kc)
    r.append(ra / (8.6 * (ek1[t] ** (-4 / 3)) ))

#operating range ro=0.1 to ro = 0.18
ekl = (0.053107 / kc)
ekh = (0.198 / kc)
plt.plot(ek, r12, label = 'Transition from Rotation unaffected to Rotation affected regime ')
plt.plot(ek, r23, label = 'Transition from Rotation affected to Geostrophic regime ')
plt.plot(ek, rnt, label = 'Transition to Non-turbulent regime')
plt.plot(ek1, r, 'o-' )
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Ekman number(Ek)')
plt.ylabel(r'$R/Ra_c$')
plt.axvspan(ekl, ekh, 0.22, 0.35, facecolor='g', alpha=0.5)
#plt.legend()
plt.show()
plt.tight_layout()

