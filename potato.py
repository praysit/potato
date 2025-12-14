import math

print("\n--- Foam Projectile Physics Calculator (RK4, with Drag) ---")

# ================= USER INPUTS =================
m = float(input("Projectile mass (kg): "))
diameter = float(input("Projectile diameter (m): "))
Cd = float(input("Drag coefficient (≈1.1 foam): "))
rho = float(input("Air density (kg/m^3, 1.225 sea level): "))
v0 = float(input("Launch speed (m/s): "))
theta_deg = float(input("Launch angle θ (degrees, 0–90): "))
y0 = float(input("Initial height (m): "))
dt = float(input("Time step dt (s, e.g. 0.002): "))
stop_dist = float(input("Stopping distance on impact (m, e.g. 0.05): "))

# ================= CONSTANTS =================
g = 9.81
A = math.pi * (diameter / 2) ** 2
k = 0.5 * rho * Cd * A

theta = math.radians(theta_deg)

# Initial velocities
vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)

x = 0.0
y = y0
t = 0.0
y_max = y

# ================= ACCELERATION FUNCTION =================
def accel(vx, vy):
    v = math.sqrt(vx*vx + vy*vy)
    ax = -(k/m) * v * vx
    ay = -g - (k/m) * v * vy
    return ax, ay

# ================= RK4 INTEGRATION =================
while y > 0:
    # k1
    ax1, ay1 = accel(vx, vy)
    k1_vx, k1_vy = ax1*dt, ay1*dt
    k1_x, k1_y = vx*dt, vy*dt

    # k2
    ax2, ay2 = accel(vx + k1_vx/2, vy + k1_vy/2)
    k2_vx, k2_vy = ax2*dt, ay2*dt
    k2_x, k2_y = (vx + k1_vx/2)*dt, (vy + k1_vy/2)*dt

    # k3
    ax3, ay3 = accel(vx + k2_vx/2, vy + k2_vy/2)
    k3_vx, k3_vy = ax3*dt, ay3*dt
    k3_x, k3_y = (vx + k2_vx/2)*dt, (vy + k2_vy/2)*dt

    # k4
    ax4, ay4 = accel(vx + k3_vx, vy + k3_vy)
    k4_vx, k4_vy = ax4*dt, ay4*dt
    k4_x, k4_y = (vx + k3_vx)*dt, (vy + k3_vy)*dt

    # Update state
    vx += (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx) / 6
    vy += (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy) / 6
    x  += (k1_x  + 2*k2_x  + 2*k3_x  + k4_x ) / 6
    y  += (k1_y  + 2*k2_y  + 2*k3_y  + k4_y ) / 6

    t += dt
    if y > y_max:
        y_max = y

# ================= RESULTS =================
impact_speed = math.sqrt(vx*vx + vy*vy)
impact_energy = 0.5 * m * impact_speed**2
momentum = m * impact_speed
impact_force = m * impact_speed**2 / (2 * stop_dist)

print("\n--- Results ---")
print(f"Launch angle: {theta_deg:.1f}°")
print(f"Time of flight: {t:.3f} s")
print(f"Horizontal range: {x:.3f} m")
print(f"Maximum height: {y_max:.3f} m")
print(f"Impact speed: {impact_speed:.3f} m/s")
print(f"Impact energy: {impact_energy:.2f} J")
print(f"Impact momentum: {momentum:.2f} kg·m/s")
print(f"Average impact force: {impact_force:.1f} N")
print(f"Impact velocity components:")
print(f"  vx = {vx:.3f} m/s")
print(f"  vy = {vy:.3f} m/s (downward)")

# ================= OPTIONAL ANGLE SWEEP =================
do_sweep = input("\nSweep angles to find max range? (y/n): ").lower()

if do_sweep == "y":
    best_range = 0
    best_angle = 0

    for ang in range(0, 91):
        vx = v0 * math.cos(math.radians(ang))
        vy = v0 * math.sin(math.radians(ang))
        x = 0.0
        y = y0
        t = 0.0

        while y > 0:
            ax, ay = accel(vx, vy)
            vx += ax * dt
            vy += ay * dt
            x += vx * dt
            y += vy * dt
            t += dt

        if x > best_range:
            best_range = x
            best_angle = ang

    print(f"\nMax range ≈ {best_range:.2f} m at angle ≈ {best_angle}°")
