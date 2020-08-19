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
Ta = list(np.logspace(9, 14, num=1500))

for t in range(len(Ta)):
    #x =Ta[t]
    Ra1.append((0.086 / 4) * Ta[t])
    Ra2.append((1.4 * (2 ** (-7/4))) * (Ta[t] ** (7/8)))
    Ra3.append((1.4 * (2 ** (-1.5))) * (Ta[t] ** 0.75))
x =Ta
y1 = Ra1
y2 = Ra2
y3 = Ra3

plt.plot(Ta, y1, 'b-', Ta, y2, 'r--', Ta, y3, 'g--')
#plt.plot(x, y2)
plt.yscale('log')
plt.xscale('log')
# plt.plot(Ta, Ra3)
print(type(Ta))

plt.show()