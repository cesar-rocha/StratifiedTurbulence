import sys
import glob
import h5py
import numpy as np
import matplotlib.pyplot as plt

simulation = "output"
pathi = simulation+"/snapshots/"
#model =  h5py.File(simulation+"/setup.h5",'r')
#diags =  h5py.File(simulation+"/diagnostics.h5",'r')



fnis = sorted(glob.glob(pathi+'*.h5'))
Fr = 0.1

# kinetic energy series
ke, keb, kep = [], [], []
pe = []

plt.rcParams['image.cmap'] = 'RdBu'
plt.ion()

for fni in fnis[:]:
    snap =  h5py.File(fni,'r')
    u,w,q,b = snap['u'][:],snap['v'][:],snap['q'][:],Fr*snap['b'][:]
    ub = u.mean(axis=1)
    up = u-ub[...,np.newaxis]
    ke.append(0.5*(u**2+w**2).mean())
    keb.append(0.5*(ub**2).mean())
    kep.append(0.5*(up**2+w**2).mean())

    pe.append(0.5*(b**2).sum())

    plt.clf()
    plt.subplot(121)
    plt.imshow(q)
    plt.xticks([])
    plt.yticks([])
    plt.clim([-120., 120.])
    plt.title(fni[-6:-3])
    
    plt.subplot(122)
    plt.imshow(np.sqrt(u**2+w**2),cmap='viridis')
    plt.xticks([])
    plt.yticks([])
    plt.clim([0., 12])
    plt.title(fni[-6:-3])
     
    plt.pause(0.1)
    plt.draw()
    #plt.ioff()

