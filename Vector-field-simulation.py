import numpy as np
import matplotlib.pyplot as plt

# 1. Generate the grid coordinates for the vector field
x = np.linspace(-0.5, 2.5, 15)
y = np.linspace(-0.5, 2.5, 15)
X, Y = np.meshgrid(x, y)

# 2. Define the whirlpool vector field components: F = <-y, x>
P = -Y  # Horizontal component
Q = X   # Vertical component

# 3. Create the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the vector field arrows
# (angles='xy', scale_units='xy', scale=7 adjusts arrow sizing for clarity)
ax.quiver(X, Y, P, Q, color='gray', alpha=0.6, angles='xy', scale_units='xy', scale=7, label='Vector Field F = <-y, x>')

# 4. Shade the Region R (Square from x:, y:)
ax.fill_between([0, 2], 0, 2, color='skyblue', alpha=0.3, label='Region R (Area = 4)')

# 5. Draw the Boundary Curve C with directional arrows (Counterclockwise)
# Path 1: Bottom Edge (0,0) -> (2,0)
ax.annotate('', xy=(2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="red", lw=2.5))
# Path 2: Right Edge (2,0) -> (2,2)
ax.annotate('', xy=(2, 2), xytext=(2, 0), arrowprops=dict(arrowstyle="->", color="red", lw=2.5))
# Path 3: Top Edge (2,2) -> (0,2)
ax.annotate('', xy=(0, 2), xytext=(2, 2), arrowprops=dict(arrowstyle="->", color="red", lw=2.5))
# Path 4: Left Edge (0,2) -> (0,0)
ax.annotate('', xy=(0, 0), xytext=(0, 2), arrowprops=dict(arrowstyle="->", color="red", lw=2.5))

# Dummy plot line just to get 'Curve C' into the legend beautifully
ax.plot([], [], color='red', lw=2.5, label='Boundary Curve C')

# 6. Formatting and Labels
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 2.5)
ax.set_xlabel('X Axis', fontsize=12)
ax.set_ylabel('Y Axis', fontsize=12)
ax.set_title("Green's Theorem Visualization\nField: F = <-y, x> | Net Twist (Curl) = 2", fontsize=14, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')

# Add text labels directly to the plot
ax.text(1.0, 1.0, "Region R\n(dQ/dx - dP/dy = 2)", color='blue', fontsize=12, ha='center', fontweight='bold')
ax.text(1.0, -0.15, "Path 1", color='red', fontsize=10, ha='center')
ax.text(2.15, 1.0, "Path 2", color='red', fontsize=10, va='center', rotation=270)
ax.text(1.0, 2.1, "Path 3", color='red', fontsize=10, ha='center')
ax.text(-0.25, 1.0, "Path 4", color='red', fontsize=10, va='center', rotation=90)

plt.show()
