
import numpy as np
import matplotlib.pyplot as plt
import itertools

##############################To decide with roughnes values####################

# to calculate variation of ekman layer thickness which
# helps in designing roughness
#l_ek = 2.284 sqrt(nu= kinematic viscosity/omega = rotation rate)
#nu = 1.004 x 10-6, beta =207x10-6 both at 20 C.
#max=70 rpm.
#omega = 2 pi N /60
# ro = sqrt (ra/pr ta); ta = 2/ ek-2 = ( (2 * omg * h**2) / nu )**2; ro =sqrt(g*beta*(del t/hght=0.2m))/2 omega;
#thermal diffu = 0.143 * 10 ** -6, Fr = ((omega ** 2) * D) / (2*g)


delt = 5 #delta T, temperature difference.
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

plt.figure(1)

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
#plt.show()
############################################################



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
ek_cheng = list(np.logspace(-7, -8, num=20))

#alpha = 0.143 * (10 ** (-6))
#beta = (207 * (10**(-6)))  #Expansion coefficient.
#h = 0.2 #height of cell in meters
#nu = 1.004 * (10**(-6))
#omg = np.arange(0.5, 3, 0.5)
#ra = (9.81 * beta * delt * (h**3)) / (nu * alpha)
#kc = (np.sqrt(ra / pr) ) / 2
ro = []
r = []
rac = []
r12 = []
r23 = []
rnt =[]
ek1 =[]
for t in range(len(ek)):
    rac.append(8.6 * (ek[t] ** (-4/3)))
    r12.append(((2 ** 2) / (ek[t] ** 2)) * (pr / rac[t])) #Ro = 2
    r23.append((0.3 * (ek[t] ** (-1.8))) / (rac[t]))
    rnt.append(3)

def cheng2020PRF ():
    ro = 0.06 #Transition between rotation affected and non-rotating
    rh_cheng2020 = []
    rl_cheng2020 = []
    rac_cheng=[]
    for t in range(len(ek_cheng)):
        rac_cheng.append(8.6 * (ek_cheng[t] ** (-4/3)))
        rh_cheng2020.append( ( (ro**2) / ( (1/4) * (ek_cheng[t] ** 2) ) ) * ( pr / rac_cheng[t] ) )
        rl_cheng2020.append( (ek_cheng[t] ** (-8/5)) * ( ( pr ** (3/5) ) / rac_cheng[t] ) )
    ek_visual_exp = 5 * ( 10 ** (-8) )
    r_ctc = (9.6 * (10 ** 10) ) / (8.6 * (ek_visual_exp ** (-4/3)))
    r_plumes = ( 8.6 * (1e11) ) / (8.6 * (ek_visual_exp ** (-4/3)))
    r_gt = ( 1.2 * (1e12) ) / (8.6 * (ek_visual_exp ** (-4/3)))
    r_rit = ( 3.3 * (1e12) ) / (8.6 * (ek_visual_exp ** (-4/3)))

    ra_asp0p5 = (np.logspace(10, 11, num=10))
    ra_asp0p2 = (np.logspace(11, 13, num=10))
    ra_asp0p1 = (np.logspace(12, 14, num=10))
    ek_asp0p5 = ( 3 * (1e-7) )
    ek_asp0p2 = (5 * (1e-8)  )
    ek_asp0p1 = (1 * (1e-8) )
    r_asp0p5 = ra_asp0p5 / (8.6 * (ek_asp0p5 ** (-4/3) ) )
    r_asp0p2 = ra_asp0p2 / (8.6 * (ek_asp0p2 ** (-4/3) ) )
    r_asp0p1 = ra_asp0p1 / (8.6 * (ek_asp0p1 ** (-4/3) ) )
    ek_asp0p5 = ( 3 * (1e-7), 3 * (1e-7),3 * (1e-7),3 * (1e-7),3 * (1e-7),3 * (1e-7),3 * (1e-7),3 * (1e-7),3 * (1e-7),3 * (1e-7) )
    ek_asp0p2 = (5 * (1e-8), 5 * (1e-8),5 * (1e-8),5 * (1e-8),5 * (1e-8),5 * (1e-8),5 * (1e-8),5 * (1e-8),5 * (1e-8),5 * (1e-8)  )
    ek_asp0p1 = (1 * (1e-8), 1 * (1e-8),1 * (1e-8),1 * (1e-8),1 * (1e-8),1 * (1e-8),1 * (1e-8),1 * (1e-8),1 * (1e-8),1 * (1e-8) )

    return rh_cheng2020, rl_cheng2020, ek_asp0p5, r_asp0p5, ek_asp0p2, r_asp0p2, ek_asp0p1, r_asp0p1, ek_visual_exp, r_ctc, r_plumes, r_gt, r_rit

#for t in range(len(omg)):
 #   ro.append((np.sqrt(9.81 * beta * (delt / h))) / (2 * omg[t]))
  #  ek1.append((2 * ro[t]) / kc)
   # r.append(ra / (8.6 * (ek1[t] ** (-4 / 3)) ))

#operating range ro=0.1 to ro = 0.18

plt.figure(2)

rh_cheng2020, rl_cheng2020, cheng_ek_asp0p5, cheng_r_asp0p5, cheng_ek_asp0p2, cheng_r_asp0p2, cheng_ek_asp0p1, cheng_r_asp0p1, exp_ek_visual, exp_ctc, exp_plumes, exp_gt, exp_rit = cheng2020PRF()
print(exp_ctc)
ekl = 1 * (0.053107 / kc)
ekh = 1 * (0.198 / kc)
plt.plot(ek, r12 ) #label = 'Transition from Rotation unaffected to Rotation affected regime ')
plt.plot(ek, r23 ) #label = 'Transition from Rotation affected to Geostrophic regime ')
plt.plot(ek, rnt ) #label = 'Transition to Non-turbulent regime')
plt.plot(ek_cheng, rh_cheng2020, label = 'Upper Limit-Cheng2020 Scaling')
plt.plot(ek_cheng, rl_cheng2020, label = 'Lower Limit-Cheng2020 Scaling')
plt.plot(cheng_ek_asp0p5, cheng_r_asp0p5, label = 'Cheng2020_ASP0p5')
plt.plot(cheng_ek_asp0p2, cheng_r_asp0p2, label = 'Cheng2020_ASP0p2')
plt.plot(cheng_ek_asp0p1, cheng_r_asp0p1, label = 'Cheng2020_ASP0p1')
plt.annotate("CTC", (exp_ek_visual, exp_ctc))
plt.annotate("Plumes", (exp_ek_visual, exp_plumes))
plt.annotate("GT", (exp_ek_visual, exp_gt))
plt.annotate("RIT", (exp_ek_visual, exp_rit))

plt.plot(Ek, R, 'o-', label = 'Our Exp' )
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Ekman number(Ek)')
plt.ylabel(r'$R/Ra_c$')
plt.axvspan(ekl, ekh, 0.22, 0.35, facecolor='g', alpha=0.5)
plt.legend(loc = 1, fontsize = 10)
plt.show()
plt.tight_layout()

