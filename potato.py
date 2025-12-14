import math

print("\n--- Horizontal Projectile Simulator (with air drag) ---")

# ==== USER INPUTS ====
m = float(input("Projectile mass (kg): "))
diameter = float(input("Projectile diameter (m): "))
C_d = float(input("Drag coefficient (e.g. 1.1 for foam): "))
rho = float(input("Air density (kg/m^3, ~1.225 at sea level): "))
v0 = float(input("Initial horizontal speed (m/s): "))
y0 = float(input("Initial height above ground (m): "))
dt = float(input("Time step dt (s, e.g. 0.01): "))

# ==== CONSTANTS ====
g = 9.81

# ==== DERIVED VALUES ====
A = math.pi * (diameter / 2) ** 2

# ==== INITIAL CONDITIONS ====
x = 0.0
y = y0
vx = v0
vy = 0.0
t = 0.0

# ==== SIMULATION LOOP ====
while y > 0:
    v = math.sqrt(vx**2 + vy**2)

    # Drag forces
    Fdx = -0.5 * rho * C_d * A * v * vx
    Fdy = -0.5 * rho * C_d * A * v * vy

    # Accelerations
    ax = Fdx / m
    ay = -g + Fdy / m

    # Update velocities
    vx += ax * dt
    vy += ay * dt

    # Update positions
    x += vx * dt
    y += vy * dt

    t += dt

# ==== FINAL RESULTS ====
impact_speed = math.sqrt(vx**2 + vy**2)
impact_energy = 0.5 * m * impact_speed**2

print("\n--- Results ---")
print(f"Time of flight: {t:.3f} s")
print(f"Horizontal distance: {x:.3f} m")
print(f"Impact speed: {impact_speed:.3f} m/s")
print(f"Impact kinetic energy: {impact_energy:.2f} J")
print(f"Impact velocity components:")
print(f"  vx = {vx:.3f} m/s")
print(f"  vy = {vy:.3f} m/s (downward)")
