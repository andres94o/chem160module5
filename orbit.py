from math import sqrt
from drawtraj import drawtraj
def force(x,y,m,mstar):
    r2=x**2+y**2
    r32=r2*sqrt(r2)
    fx=-x*m*mstar/r32
    fy=-y*m*mstar/r32
    return fx,fy
def integrate(x,y,vx,vy,fx,fy,m,dt):
    ax, ay = fx/m, fy/m
    vx = vx + (ax*dt)
    vy = vy + (ay*dt)
    x = x+ (vx*dt)
    y = y + (vy*dt)
    return x, y, vx, vy


mstar = 100
m = 1
nsteps = 5000000
dt = 0.01
r = 50
x, y = 0, r
vx, vy = 0.2, 0.4
trajx, trajy = [], []
for t in range(nsteps):
    fx, fy = force(x, y, m, mstar)
    x, y, vx, vy = integrate(x, y, vx, vy, fx, fy, m, dt)
    trajx.append(x)
    trajy.append(y)
drawtraj(trajx,trajy,5*r)