import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------ PARAMETERS ------------------
m = 0.5          # mass (kg)
diameter = 0.10  # projectile diameter (m)
Cd = 1.1         # drag coefficient
rho = 1.225      # air density (kg/m^3)
v0 = 20.0        # launch speed (m/s)
theta_deg = 45   # launch angle in degrees
y0 = 0.5         # initial height (m)
dt = 0.01        # time step (s)

stop_dist = 0.05  # stopping distance for reference

g = 9.81
A = math.pi * (diameter/2)**2
k = 0.5 * rho * Cd * A

theta = math.radians(theta_deg)

# Initial velocities
vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)

x = 0.0
y = y0

# Store trajectory for plotting
xs = [x]
ys = [y]

# ------------------ SIMULATION ------------------
while y > 0:
    v = math.sqrt(vx**2 + vy**2)
    ax = -(k/m) * v * vx
    ay = -g - (k/m) * v * vy
    
    # Update velocities
    vx += ax * dt
    vy += ay * dt
    
    # Update positions
    x += vx * dt
    y += vy * dt
    
    xs.append(x)
    ys.append(y)

print(f"Number of points: {len(xs)}")
print(f"First 5 points X: {xs[:5]}")
print(f"First 5 points Y: {ys[:5]}")
print(f"Final point X: {xs[-1]}, Y: {ys[-1]}")


# ------------------ ANIMATION ------------------
fig, ax = plt.subplots()
ax.set_xlim(0, max(xs)*1.1)
ax.set_ylim(0, max(ys)*1.2)
ax.set_xlabel('Horizontal distance (m)')
ax.set_ylabel('Height (m)')
ax.set_title(f'Projectile Motion θ={theta_deg}° with Drag')

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

ani = animation.FuncAnimation(fig, animate, frames=len(xs), init_func=init,
                              interval=dt*1000, blit=True, repeat=False)

plt.show()
