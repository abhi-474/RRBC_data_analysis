# to calculate variation of ekman layer thickness which
# helps in designing roughness
#l_ek = 2.284 sqrt(nu= kinematic viscosity/omega = rotation rate)
#nu = 1.004 x 10-6, beta =207x10-6 both at 20 C.
#max=70 rpm.
#omega = 2 pi N /60
# ro = sqrt (ra/pr ta); ta = 2/ ek-2 = ( (2 * omg * h**2) / nu )**2; ro =sqrt(g*beta*(del t/hght=0.2m))/2 omega;
#thermal diffu = 0.143 * 10 ** -6, Fr = ((omega ** 2) * D) / (2*g)

import numpy as np
import matplotlib.pyplot as plt

delt = 10 #delta T, temperature difference.
g = 9.81 # gravity
alpha = 0.143 * (10 ** (-6)) #thermal diffusivity
beta = (207 * (10**(-6)))  #Expansion coefficient
h = 0.2 #height of cell in meters
d = 0.2 * np.sqrt(2) #Diameter of cell
nu = 1.004 * (10**(-6)) #kinematic viscosity
pr = 6.86 #Prandtl number of fluid
Fr = 0.1 #Froude number
omgl = 0.5 # Lowest angular velocity
omgh = np.sqrt( (2 * g * Fr) / d ) #Hisghest angular velocity, restricted due to froude number
omg = np.linspace(0.5, omgh, 10)
ra = (9.81 * beta * delt * (h**3)) / (nu * alpha) # Rayleigh number of flow
kc = (np.sqrt(ra / pr) ) / 2

#for t in range(len(omg)):
 #   ro.append((np.sqrt(9.81 * beta * (delt / h))) / (2 * omg[t]))
  #  ek.append(ro[t] /kc)
   # lek.append(2.284 * 1000 * np.sqrt(nu / omg[t]))
    
l = len(omg)
def params(ra, pr, omg, h, nu, l):
    ta=[]
    ek = []
    rac = []
    r =[]
    ro = []
    for i in range(l):
        ta.append( ( (2 * omg[i] * h * h) / nu ) ** 2 )
        ek.append( 2 / ( np.sqrt(ta[i]) ) )
        rac.append(8.6 * (ek[i] ** (-4/3) ) )
        r.append(ra / (8.6 * (ek[i] ** (-4/3) ) ) )
        ro.append( np.sqrt( ra / (pr * ta[i] ) ) )
    return ta, ek, rac, r, ro

def ekbl(nu, omg, l):
    ekl=[]
    j =l
    for i in range(j):
        ekl.append(2.284 * 1000 * np.sqrt(nu / omg[i]))
    return ekl

Ta, Ek, Rac, R, Ro = params(ra, pr, omg, h, nu, l)
lek = ekbl(nu, omg, l)

print(omg)
print(omgh)
print(Ro)
print(Ta)
print(ra)
#rot = (np.sqrt(9.81 * beta * (delt / h))) / (2 * 3)
#ekt = rot / kc
#rot = 0.053107, ekt = 4.13509 10** -6
#print(rot, ekt)
plt.plot(Ro, lek)
plt.axvspan(0.053107, 0.198, 0.05, 0.59,  facecolor='g', alpha=0.5)
#plt.plot(ek, r)
plt.xlabel('Rossby number(Ro)')
plt.ylabel(r'$\delta_e (mm)$')
plt.show()
