import numpy as np
import matplotlib.pyplot as plt
# Parameter
E0 = 1.0
k = 2 * np.pi
z = np.linspace(0, 2, 300)
t = 0
phase = k * z - t
# Vertikal lineare Polarisation
Ex_lin = np.zeros_like(z)
Ey_lin = E0 * np.cos(phase)
Ez_lin = z
# Zirkuläre Polarisation
Ex_circ = E0 * np.cos(phase)
Ey_circ = E0 * np.sin(phase)
Ez_circ = z
# Achsen zeichnen
def draw_axes(ax, zlen=2.2, elen=1.2):
    # z-Achse (Ausbreitung)
    ax.quiver(0, 0, 0, zlen, 0, 0,
              color='k', arrow_length_ratio=0.06, linewidth=1.5)
    # x-Achse
    ax.quiver(0, 0, 0, 0, elen, 0,
              color='k', arrow_length_ratio=0.10, linewidth=1.5)
    # y-Achse
    ax.quiver(0, 0, 0, 0, 0, elen,
              color='k', arrow_length_ratio=0.10, linewidth=1.5)
    # Beschriftung
    ax.text(zlen, 0, 0, "z")
    ax.text(0, elen, 0, "x")
    ax.text(0, 0, elen, "y")
def clean_3d_axes(ax):
    # Hintergrund-Panes aus
    ax.xaxis.pane.set_visible(False)
    ax.yaxis.pane.set_visible(False)
    ax.zaxis.pane.set_visible(False)
    # Achsenbox aus
    ax._axis3don = False

# Plot
fig = plt.figure(figsize=(10, 4))
#
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot(Ez_lin, Ex_lin, Ey_lin, linewidth=2)
draw_axes(ax1)
clean_3d_axes(ax1)
ax1.set_title("Lineare vertikale Polarisation")
ax1.set_xlim(0, 2.2)
ax1.set_ylim(-1.2, 1.2)
ax1.set_zlim(-1.2, 1.2)
ax1.view_init(elev=20, azim=-60)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_zticks([])
ax1.grid(False)
#
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot(Ez_circ, Ex_circ, Ey_circ, linewidth=2)
draw_axes(ax2)
clean_3d_axes(ax2)
ax2.set_title("Zirkuläre Polarisation")
ax2.set_xlim(0, 2.2)
ax2.set_ylim(-1.2, 1.2)
ax2.set_zlim(-1.2, 1.2)
ax2.view_init(elev=20, azim=-60)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_zticks([])
ax2.grid(False)
plt.tight_layout()
plt.show()