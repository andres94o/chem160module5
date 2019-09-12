from math import pi, cos, sqrt
dt = 0.0007
mass = 10
period = 10
omega = (2 * pi)/period
k = mass * omega**2
tmax = period #this is how long the simulation will run; max time
x = + 1 #the spring is extended out, there is tenison in the spring that is pulling the spring back
v = 0
t = 0
rms_error = 0 #this keeps a sum of the difference between the exact results and predicted results 
steps = 0 #counter of steps
while t < tmax: #this loop will be performed while t (time) is less than tmax
    f = -k * x 
    a = f/mass
    x = x + (v * dt)
    v = v + (a * dt)
    x_exact = cos(2*pi*t/period)
    rms_error = rms_error + (x - x_exact)**2
    steps += 1
    t += dt
print("dt = %f RMS Error = %f"%(dt, sqrt(rms_error/steps)))
