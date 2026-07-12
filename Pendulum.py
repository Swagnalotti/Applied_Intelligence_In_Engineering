import numpy
import matplotlib.pyplot
import matplotlib.animation
from matplotlib import pyplot as plt

# Parameters
theta0 = 145  # degrees
l = 1  # pendulum length (m)
g = 9.81  # gravity (m/s^2)

frame_rate = 60  # frames per second
duration = 10  # seconds
num_frames = duration * frame_rate

# Convert initial angle to radians
theta0 = theta0 * numpy.pi / 180

# Angular frequency
omega = numpy.sqrt(g / l)

# Time array
t = numpy.linspace(0, duration, num_frames)

# Small-angle pendulum motion
theta = theta0 * numpy.cos(omega * t)

# Cartesian coordinates
x = l * numpy.sin(theta)
y = -l * numpy.cos(theta)

# Create figure
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(aspect='equal')

ax.set_xlim(-l * 7 / 6, l * 7 / 6)
ax.set_ylim(-l * 7 / 6, l * 7 / 6)

# Pendulum rod
#line, = ax.plot((0, x[0]), (0, y[0]), linewidth=2)
line, = ax.plot((0, x[0]), (0, y[0]))

# Pendulum bob
#circle = matplotlib.pyplot.Circle((x[0], y[0]), 0.05)
circle = matplotlib.pyplot.Circle((x[0], y[0]))
ax.add_patch(circle)

# Animation update function
def update(i):
    line.set_data((0, x[i]), (0, y[i]))
    circle.set_center((x[i], y[i]))
    return line, circle

# Create animation
ani = matplotlib.animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/frame_rate, blit=True)
matplotlib.pyplot.show()
