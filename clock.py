import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# List of OS/distro names corresponding to each hour
os_names = [
    "Ubuntu", "Windows", "Laser OS", "Android", "Harmony OS", "MacOS",
    "Mint", "Fedora", "Puppy", "Kodachi", "Zorin", "Xubuntu"
]

def draw_os_clock():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw outer circle
    ax.add_artist(plt.Circle((0, 0), 1.0, fill=False, linewidth=2))

    # Place OS names at each hour position
    for i, name in enumerate(os_names):
        angle = np.deg2rad(90 - i * 30)  # rotate clockwise
        x = 0.85 * np.cos(angle)
        y = 0.85 * np.sin(angle)
        ax.text(x, y, name, ha='center', va='center', fontsize=10, weight='bold')

    # Current system time
    now = datetime.now()
    hour = now.hour % 12 + now.minute / 60.0
    minute = now.minute

    # Hour hand
    hour_angle = np.deg2rad(90 - hour * 30)
    hx = 0.5 * np.cos(hour_angle)
    hy = 0.5 * np.sin(hour_angle)
    ax.plot([0, hx], [0, hy], color='red', linewidth=3, label='Hour')

    # Minute hand
    minute_angle = np.deg2rad(90 - minute * 6)
    mx = 0.75 * np.cos(minute_angle)
    my = 0.75 * np.sin(minute_angle)
    ax.plot([0, mx], [0, my], color='blue', linewidth=2, label='Minute')

    # Center dot
    ax.plot(0, 0, 'ko', markersize=5)

    # Title and legend
    ax.set_title("OS Distro Clock", fontsize=14, weight='bold')
    ax.legend(loc='lower right')
    plt.show()

draw_os_clock()

