import numpy as np
from numpy import pi, cos, sin, cosh, tanh
import matplotlib.pyplot as plt
import spectral_model as model

sech = lambda x: 1./np.cosh(x)

reload(model)

Fr =  0.1
Fr2 = Fr**2
Reb = 10

# the model object
m = model.Boussinesq2d(Lx=2.*np.pi,nx=256, tmax = 40,tavestart=20, dt = 2*0.00075, \
        use_fftw=True,ntd=4,Fr=Fr,use_filter=True,tsave=100000,
        twrite=1,nu=Fr2/Reb,sig=1.e5,kf=25,
        save_snapshots=True,
        tsave_snapshots=1000,
        ext_forc=True)

# run the model and plot some figs
plt.rcParams['image.cmap'] = 'RdBu'

plt.ion()

# forcing q
m0 = 1.
A0 = 1/2.
ep = pi/2.
zmin,zmax = pi-ep,pi+ep

# initial conditions
sig = 1.e-7
qi = sig*np.random.randn(m.nx,m.nx)
bi = sig*np.random.randn(m.nx,m.nx)

qi = qi
m.set_q(qi)
m.set_b(bi)

# forcing in the vorticity equation
#fq = Fr2*( (m0**3) / (Reb))*cos(m0*m.z)
fq = cos(m0*m.z)
m.set_forcing(fq)

m.run()

ubar = m.get_diagnostic('ubar')*((m0**3) / (Reb)/2.)
bbar = m.get_diagnostic('bbar')
uwbar = m.get_diagnostic('uwbar')
wbbar = m.get_diagnostic('wbbar')
z = m.z[...,0]

plt.figure()
plt.plot(-ubar,z,linewidth=2)
plt.plot(np.sin(3*z),z,'--',linewidth=1)
plt.xlabel(r'$\bar{u}$')
plt.ylabel(r'z')
plt.savefig('ubar_dns.png')

plt.figure()
plt.plot(bbar+z,z,linewidth=2)
plt.plot(z,z,'--',linewidth=1)
plt.xlabel(r'$\bar{b}$')
plt.ylabel(r'z')
plt.savefig('bbar_dns.png')

plt.figure()
plt.plot(uwb0ar,z,linewidth=2)
plt.xlabel(r'$\bar{uw}$')
plt.ylabel(r'z')
plt.savefig('uwbar_dns.png')


#t, ke = [],[]
#for snapshot in m.run_with_snapshots(tsnapstart=0, tsnapint=100*m.dt):
#
#    plt.clf()
#    p1 = plt.contourf(m.q,np.linspace(-30,30,15))
#    plt.clim([-30., 30.])
#    plt.title('t='+str(m.t))
#
#    plt.xticks([])
#    plt.yticks([])
#
#    plt.pause(0.001)
#    
#    plt.draw()
#
#    t.append(m.t)
#    ke.append(m.ke)
#
#plt.show()
#plt.ion()
