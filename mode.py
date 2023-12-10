import matplotlib.pyplot as plt
import numpy as np

t0 = 1
d = 1e-10
L = 1
N = 100

def a(n):
    return 2*n

def f(t,x):
    s = t0
    for n in range(1,N):
        s += a(n)*np.exp(-n**2*d*np.pi*np.pi/(L*L)*t)*np.cos(n*np.pi/L*x)
    return s

# linspace permet de créer un tableau de valeurs régulièrement espacées
x = np.linspace(0,L,500)
# debut fin nb de points
t = np.linspace(0,100,50)
X,T = np.meshgrid(x,t)

# Z est un tableau à deux dimensions, de même taille que X et Y
Z = f(T,X)
plt.xlabel('distance')
plt.ylabel('temps')
plt.contourf(X,T,Z)
plt.show()

