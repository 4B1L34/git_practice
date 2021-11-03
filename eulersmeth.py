import numpy as np
from matplotlib import pyplot as plt
import math

#IVP: y'(t) = -2y+4, y(0) = 1
## the lab wants me to do dt = 0.2 and N = 5

x0 = 0
y0 = 1
z0 = 1
error0 = 0
xf = 1
n = 6
deltax = (xf-x0)/(n-1)

x = np.linspace(x0, xf, n)

y = np.zeros([n])
z = np.zeros([n])
error = np.zeros([n])

y[0] = y0
z[0] = z0
error[0] = 0
for i in range(1,n):
    y[i] = deltax*(-2*y[i-1] + 4) + y[i-1]

for i in range(1,n):
    z[i] = 2 - math.e**(-2*x[i])
    
for i in range(1, n):
    error[i] = np.absolute(((z[i] - y[i]) / z[i]) * 100)

for i in range(n):
    print("Approximate: (%.0f) " % (i+1))
    print("%.2f, %.2f" % (x[i],y[i]))
 
    print("Real: ")
    print("%.2f, %.2f" % (x[i],z[i]))
    print("Error: ")
    print("%.2f" % (error[i]) + "%\n")



plt.plot(x,y, label = "Approx.")
plt.plot(x,z, label = "Real")
plt.legend()
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximate Solution with Euler's Method")
plt.show()
