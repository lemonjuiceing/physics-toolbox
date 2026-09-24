import collections
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection

# ==========================================
# 1. Choose or Define Vector Field
# ==========================================
def vector_field(x, y):
    """
    Define 2D velocity (u, v) at coordinates (x, y).
    Preset: Non-linear swirl with multiple vortices and saddles.
    """
    u = np.sin(y) - 0.2 * x
    v = np.cos(x) - 0.2 * y
    return u, v


# ==========================================
# 2. Numerical Integrator (Runge-Kutta 4th Order)
# ==========================================
def rk4_step(x, y, dt):
    """Calculates next position using RK4 for accurate streamline tracking."""
    k1_u, k1_v = vector_field(x, y)
    
    k2_u, k2_v = vector_field(x + 0.5 * dt * k1_u, y + 0.5 * dt * k1_v)
    k3_u, k3_v = vector_field(x + 0.5 * dt * k2_u, y + 0.5 * dt * k2_v)
    k4_u, k4_v = vector_field(x + dt * k3_u, y + dt * k3_v)
    
    x_next = x + (dt / 6.0) * (k1_u + 2 * k2_u + 2 * k3_u + k4_u)
    y_next = y + (dt / 6.0) * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)
    return x_next, y_next


# ==========================================
# 3. Setup Simulation Parameters & Canvas
# ==========================================
X_MIN, X_MAX = -3.5, 3.5
Y_MIN, Y_MAX = -3.5, 3.5
DT = 0.05
TRAIL_LENGTH = 120

# Particle state: [x, y]
pos = np.array([2.5, 2.0], dtype=float)
trail_x = collections.deque(maxlen=TRAIL_LENGTH)
trail_y = collections.deque(maxlen=TRAIL_LENGTH)

# Initialize plot with dark theme
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(9, 9))

# Background quiver arrows
grid_n = 25
gx = np.linspace(X_MIN, X_MAX, grid_n)
gy = np.linspace(Y_MIN, Y_MAX, grid_n)
GX, GY = np.meshgrid(gx, gy)
GU, GV = vector_field(GX, GY)
speed = np.sqrt(GU**2 + GV**2) + 1e-9

ax.quiver(
    GX, GY,
    GU / speed, GV / speed,
    speed,
    cmap="Blues",
    alpha=0.45,
    pivot="mid",
    scale=35
)

# Background subtle streamlines
fine_gx = np.linspace(X_MIN, X_MAX, 80)
fine_gy = np.linspace(Y_MIN, Y_MAX, 80)
FGX, FGY = np.meshgrid(fine_gx, fine_gy)
FGU, FGV = vector_field(FGX, FGY)
ax.streamplot(
    FGX, FGY, FGU, FGV,
    color=(0.3, 0.4, 0.6, 0.25),
    density=0.8,
    linewidth=0.8,
    arrowsize=0.8
)

# Multi-segment line collection for fading gradient trail
trail_collection = LineCollection([], linewidths=np.linspace(0.8, 3.2, TRAIL_LENGTH), zorder=4)
ax.add_collection(trail_collection)

# Glowing particle head
glow_head, = ax.plot([], [], "o", color="#ffdd00", markersize=12, alpha=0.35, zorder=5)
particle_head, = ax.plot([], [], "o", color="#ffffff", markersize=6, zorder=6)

ax.set_xlim(X_MIN, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
ax.set_aspect("equal")
ax.set_title("2D Vector Field Particle Simulation\n(Click anywhere to drop particle)", fontsize=13, pad=12)
ax.set_xlabel("X")
ax.set_ylabel("Y")


# ==========================================
# 4. Interactive Click: Drop particle anywhere
# ==========================================
def on_click(event):
    global pos
    if event.xdata is not None and event.ydata is not None:
        pos = np.array([event.xdata, event.ydata], dtype=float)
        trail_x.clear()
        trail_y.clear()

fig.canvas.mpl_connect("button_press_event", on_click)


# ==========================================
# 5. Animation Update Function
# ==========================================
def update(frame):
    global pos
    
    # Advance position with RK4 integration
    pos[0], pos[1] = rk4_step(pos[0], pos[1], DT)
    
    # Boundary wrap-around / respawn if out of bounds
    if not (X_MIN <= pos[0] <= X_MAX and Y_MIN <= pos[1] <= Y_MAX):
        pos = np.random.uniform(X_MIN * 0.7, X_MAX * 0.7, size=2)
        trail_x.clear()
        trail_y.clear()
    
    trail_x.append(pos[0])
    trail_y.append(pos[1])
    
    # Update trail with fading gradient
    n_pts = len(trail_x)
    if n_pts > 1:
        points = np.array([trail_x, trail_y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        
        # Color gradient: fading cyan/gold trail
        alphas = np.linspace(0.05, 1.0, len(segments))
        colors = np.zeros((len(segments), 4))
        colors[:, 0] = np.linspace(0.2, 1.0, len(segments))   # R
        colors[:, 1] = np.linspace(0.8, 0.85, len(segments))  # G
        colors[:, 2] = np.linspace(1.0, 0.2, len(segments))   # B
        colors[:, 3] = alphas                                # Alpha
        
        trail_collection.set_segments(segments)
        trail_collection.set_color(colors)
    else:
        trail_collection.set_segments([])
    
    # Update particle head
    particle_head.set_data([pos[0]], [pos[1]])
    glow_head.set_data([pos[0]], [pos[1]])
    
    return trail_collection, particle_head, glow_head


# ==========================================
# 6. Run Animation
# ==========================================
ani = FuncAnimation(fig, update, frames=None, interval=20, blit=True, cache_frame_data=False)

if __name__ == "__main__":
    plt.tight_layout()
    plt.show()