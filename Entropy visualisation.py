import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Simulation Settings ---
num_slices = 5          # Number of vertical splits/slices
particles_per_slice = [100, 10, 0, 0, 0]  # Initial distribution (Hot left, cold right)
slice_width = 10.0      # Physical width of each slice
height = 10.0           # Height of the container

# Calculate total particles
total_particles = sum(particles_per_slice)

# --- Initialize Particle State ---
# Positions: X spreads across the slices based on initial counts, Y is random
x_positions = []
for i, count in enumerate(particles_per_slice):
    x_min = i * slice_width
    x_max = (i + 1) * slice_width
    x_positions.extend(np.random.uniform(x_min, x_max, count))

positions = np.zeros((total_particles, 2))
positions[:, 0] = x_positions
positions[:, 1] = np.random.uniform(0, height, total_particles)

# Random initial directions for velocity vectors (angles 0 to 2pi)
angles = np.random.uniform(0, 2 * np.pi, total_particles)
velocities = np.column_stack((np.cos(angles), np.sin(angles)))

# --- Setup Plotting Structure ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, num_slices * slice_width)
ax.set_ylim(0, height)
ax.set_title("Microscopic Heat Rod: Energy Points Accelerating Across Slices", fontsize=14)
ax.set_xlabel("Rod Slices (Left to Right)")
ax.set_ylabel("Slice Height")

# Draw vertical lines to visually represent the splits/slices
for i in range(1, num_slices):
    ax.axvline(i * slice_width, color='black', linestyle='--', alpha=0.5)

# The scatter plot representing our moving energy units
scatter = ax.scatter(positions[:, 0], positions[:, 1], c='red', s=15, edgecolor='black', alpha=0.7)

# --- Animation Core Loop ---
def update(frame):
    global positions, velocities
    
    # 1. Identify which slice each particle currently resides in
    current_slices = (positions[:, 0] // slice_width).astype(int)
    # Clip indices to prevent edge boundary numerical overflows
    current_slices = np.clip(current_slices, 0, num_slices - 1)
    
    # 2. Count current population per slice to determine local temperature/speed
    counts = np.bincount(current_slices, minlength=num_slices)
    
    # 3. Scale speed: local speed is proportional to population density
    # Base speed is 0.1; adds more speed the more energy units occupy that specific slice
    speeds = 0.05 + 0.005 * counts[current_slices]
    
    # 4. Advance particle positions based on calculated velocities and custom local speeds
    positions += velocities * speeds[:, np.newaxis]
    
    # 5. Handle Boundary Collisions (Bounce off outer walls and allow slice crossing)
    max_x = num_slices * slice_width
    
    # Left/Right outer walls bounce
    hit_left = positions[:, 0] <= 0
    hit_right = positions[:, 0] >= max_x
    velocities[hit_left, 0] = np.abs(velocities[hit_left, 0])
    velocities[hit_right, 0] = -np.abs(velocities[hit_right, 0])
    
    # Top/Bottom outer walls bounce
    hit_bottom = positions[:, 1] <= 0
    hit_top = positions[:, 1] >= height
    velocities[hit_bottom, 1] = np.abs(velocities[hit_bottom, 1])
    velocities[hit_top, 1] = -np.abs(velocities[hit_top, 1])
    
    # Keep positions strictly contained within boundaries
    positions[:, 0] = np.clip(positions[:, 0], 0.1, max_x - 0.1)
    positions[:, 1] = np.clip(positions[:, 1], 0.1, height - 0.1)
    
    # 6. Update the visual scatter position matrix
    scatter.set_offsets(positions)
    
    # Dynamically change color intensity based on localized speed for aesthetic mapping
    colors = plt.cm.plasma(np.clip(speeds / max(speeds), 0, 1))
    scatter.set_color(colors)
    
    return scatter,

# --- Run the Continuous Frame Render ---
# Note: blit=True ensures smooth rendering by updating only shifted data blocks
ani = animation.FuncAnimation(fig, update, frames=200, interval=20, blit=True)
plt.show()
