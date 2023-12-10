from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import *

N = 100000
tmax = 1
dt = tmax/N
k = 10
m = 0.1
f = 0.1
g = 9.8
y = [0]*N
vy = 0
y[0] = 4 * f * m * g / k
y[1] = y[0] + vy * dt
for i in range(2,N):
    vy = (y[i-1]-y[i-2])/dt
    """if vy > f*m*g/k : 
        y[i:N]=[y[i-1] for j in range(i,N)]
        break"""
    accel = ( - k/m * y[i] +10)
    if vy<=0: 
        y[i] = y[i-1] + (vy+accel*dt)*dt     
    else:
        y[i] = y[i-1] - (vy+accel*dt)*dt
t = linspace(0,tmax,N)
plot(t,y)
ylabel("positions (en m)")
xlabel("temps (en s)")
title("Oscillation du ressort")
show()
