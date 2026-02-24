import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m = 0.50   # (kg)
x0 = -0.20   # (m)
v0 = 0.1    # (m/s)

g = 9.81    # tierra (9.81 m/s^2)
k = 28      # resorte L1 (28 N/m) (N = kg*m/s^2)
l0 = 0.36   # resorte L1 (0.28 m)
mu = 0.20   # madera(0.20)

s = 5      
fps = 60 
tiempo = np.linspace(0, s, s*fps)  

def x(t):
    w0 = np.sqrt(k/m)
    b = (mu*g)/2
    if b == w0:
            return np.exp(-b*t)*(x0 + (v0 + b*x0)*t) + l0
    else:
        if b > w0:
            a = np.sqrt(b**2 - w0**2)
            return np.exp(-b*t)*(((v0+(a+b)*(x0-l0))/(2*a))*np.exp(a*t) + ((-v0+a*(x0-l0)+b*l0)/(2*a))*np.exp(-a*t)) + l0
        else:
             w = np.sqrt(w0**2 - b**2)
             return np.exp(-b*t)*((((w - 1j*b)*(x0-l0) - 1j*v0)/(2*w))*np.exp(1j*w*t) + (((w + 1j*b)*(x0-l0) + 1j*v0)/(2*w))*np.exp(-1j*w*t)) + l0

xt = [x(t) for t in tiempo]
yt = [0*t for t in tiempo] 

def update(frame):
    point.set_data(x(tiempo[frame]).real, 0*tiempo[frame])
    return point,

fig, ax = plt.subplots()
ax.set_xlim(np.min(x(tiempo))-np.max(x(tiempo))/50,np.max(x(tiempo))+np.max(x(tiempo))/50)
ax.set_ylim(-2, 2)
ax.plot(l0,0,".r")
point, = ax.plot([], [], 'bo')

ani = FuncAnimation(fig, update, frames=len(tiempo), blit=True, interval=1000/fps)

plt.figure()
plt.plot(tiempo,(x(tiempo)))
# plt.plot(tiempo, (x0+l0)*np.exp(-(mu*g/2)*tiempo), "--r")
plt.axhline(l0, color="r")
plt.title("Posición")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")

plt.show()

input("...  ")
plt.close()

