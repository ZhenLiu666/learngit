from scipy.optimize import fsolve
import math

def equations(p):
    x0, x1 = p
    return ( x0 + x1**2 - 4, math.exp(x0) + x0 * x1 -3 )

x0, x1 = fsolve(equations, (1, 1))

print(x0, x1)
# 0.6203445234801195 1.8383839306750887
print(equations((x0, x1)))
# (4.4508396968012676e-11, -1.0512035686360832e-11)