import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- USER INPUTS ---
m = float(input("Projectile mass (kg): "))
diameter = float(input("Projectile diameter (m): "))
Cd = float(input("Drag coefficient (e.g. 1.1 for foam): "))
rho = float(input("Air density (kg/m^3, e.g. 1.225): "))
v0 = float(input("Launch speed (m/s): "))
theta_deg = float(input("Launch angle (degrees): "))
y0 = float(input("Initial height (m): "))
dt = float(input("Time step dt (s, e.g. 0.01): "))

# --- CONSTANTS & DERIVED VALUES ---
g = 9.81
A = math.pi * (diameter / 2) ** 2
k = 0.5 * rho * Cd * A

theta = math.radians(theta_deg)

# Initial velocities
vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)

# Initial positions
x = 0.0
y = y0

# Trajectory storage
xs = [x]
ys = [y]

# --- SIMULATION LOOP ---
while y >= 0:
    v = math.sqrt(vx * vx + vy * vy)
    ax = -(k / m) * v * vx
    ay = -g - (k / m) * v * vy

    vx += ax * dt
    vy += ay * dt

    x += vx * dt
    y += vy * dt

    xs.append(x)
    ys.append(y)

# --- PLOT SETUP ---
fig, ax = plt.subplots()
ax.set_xlim(0, max(xs) * 1.1)
ax.set_ylim(0, max(ys) * 1.2)
ax.set_xlabel("Horizontal distance (m)")
ax.set_ylabel("Height (m)")
ax.set_title(f"Projectile Motion θ={theta_deg}° with Drag")

line, = ax.plot([], [], 'b-', lw=2)
point, = ax.plot([], [], 'ro', markersize=6)

def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

def animate(i):
    line.set_data(xs[:i], ys[:i])
    point.set_data(xs[i-1], ys[i-1])
    return line, point

ani = animation.FuncAnimation(fig, animate, frames=len(xs),
                              init_func=init, interval=dt*1000,
                              blit=True, repeat=False)

plt.show()
