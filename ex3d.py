# Resolution du problème de Laplace 2D avec conditions aux limites

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Paramètres
vmax = 10
vmin = 0
xmin = 0
ymin = 0
xmax = 0.9
ymax = 0.9
nx = 50
ny = 50

# intialisation des paramètres
V = np.zeros((nx,ny))
V[0,:] = vmin
V[nx-1,:] = vmax
V[:,0] = vmin
V[:,ny-1] = vmax

# fonction pour calculer l'erreur 
def epsilon(V,Vnext):
    return np.sqrt(np.sum((V-Vnext)**2)/(nx*ny))

# Boucle de calcul
vnext = np.zeros((nx,ny))
while epsilon(V,vnext)>(vmax-vmin)/1000:
    vnext = V.copy()
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            vnext[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])
    V = vnext.copy()

# Affichage
fg,ax = plt.subplots(subplot_kw={'projection':'3d'})
X,Y = np.meshgrid(np.linspace(xmin,xmax,nx),np.linspace(ymin,ymax,ny))
ax.plot_surface(X, Y, np.array(V),cmap = plt.cm.rainbow, linewidth=0, antialiased=False)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V')
plt.show()
