import numpy as np
import matplotlib.pyplot as plt

# Ra = (b*g*t*h*h*h) / (kappa * nu), h= height sample, Ro = sqrt ( (b *g *t) / L) / (2 w),
# Ta = ( (2 * w * h*h) / nu)^2, Ek = 2 / sqrt (Ta), Ro = sqrt (Ra / Pr * Ta)


# Ra = 0.086Ek^(-2) from I to II ; Ra = 1.4 Ek ^(-7/4) II to III; Ra = 1.4 Ek ^ (-3/2)

# Ra = 0.086 * 2^(-2) Ta for I to II, Ra = 1.4 * 2 ^(-7/4) * Ta ^(7/8) for II to III,
# Ra = 1.4 * 2^-1.5ta^0.75 alternateive

Ra1 = []
Ra2 = []
Ra3 = []
Ra4 = []
Rac = []
Ra1_j = []
Ta = list(np.logspace(9, 14, num=1500))

for t in range(len(Ta)):
    #Ra1.append((0.086 / 4) * Ta[t]) # from I to II, non rotating to rotation affected
    #Ra2.append((1.4 * (2 ** (-7/4))) * (Ta[t] ** (7/8)))
   # Ra3.append((1.4 * (2 ** (-1.5))) * (Ta[t] ** 0.75))
    Rac.append(8.6 * (Ta[t] ** (2/3))) # Chandreshekhar
    Ra4.append((0.25 * (2 ** -1.8)) * (Ta[t] ** 0.9)) #Ecke Niemala 2014 II to III
    Ra1_j.append( (2.5 ** 2) * 6.8 * Ta[t]  ) #Transition at Ro = 2.5 Joshi et al


plt.plot(Ta, Rac,'*', Ta, Ra4, 'g-', Ta, Ra1_j, 'b-')
#plt.plot(x, y2)
plt.yscale('log')
plt.xscale('log')
# plt.plot(Ta, Ra3)
print(type(Ta))

def ro_ta (Ra, Ro, Pr):
    Ta = Ra / (Pr * (Ro **2))
    return Ta

##### Joshi et al 2017
Ra_j = 2 * (10 ** 9)
Ro_R2_m = 0.06 #Nusselt number maxima occurs at this Rossby, after ekman pumping disrupts
Ta_R2_m = ro_ta(Ra_j, Ro_R2_m, 6.8)
Ro_R2S_m = 0.08
Ta_R2S_m = ro_ta(Ra_j, Ro_R2S_m, 6.8)
plt.plot(Ta_R2_m, Ra_j, 'ro', Ta_R2S_m, Ra_j, 'go' )
plt.yscale('log')
plt.xscale('log')




plt.show()