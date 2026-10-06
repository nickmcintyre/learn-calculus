import numpy as np
from ipycc.turtle import Turtle, showscreen, tracer, bgcolor

# =====
# Color
# =====

def clip(number, low, high):
    """Clips a number to keep it within an interval"""
    return max(low, min(number, high))

def interp(low, high, pct):
    """Interploates a value between two numbers"""
    return low + pct * (high - low)

def blend_colors(color_1, color_2, pct):
    """Blends two colors using interpolation"""
    r1, g1, b1 = color_1
    r2, g2, b2 = color_2
    pct = clip(pct, 0, 1)
    r = interp(r1, r2, pct)
    g = interp(g1, g2, pct)
    b = interp(b1, b2, pct)
    return [r, g, b]

BLACK = [0, 0, 0]
GRAY20 = [0.2, 0.2, 0.2]
GRAY40 = [0.4, 0.4, 0.4]
GRAY60 = [0.6, 0.6, 0.6]
WHITE = [1, 1, 1]
BACKGROUND = [0.921, 0.921, 0.921]

def show():
    """Shows the plot beneath the current code cell"""
    bgcolor(BACKGROUND)
    showscreen()

# ====
# Axes
# ====

# Plot dimensions
WIDTH = 400
HEIGHT = 400
X_MAX = WIDTH // 2
X_MIN = -X_MAX
Y_MAX = HEIGHT // 2
Y_MIN = -Y_MAX

# Plotting Turtle
plot_turtle = Turtle()
plot_turtle.hideturtle()

def draw_axis(x_start, y_start, x_end, y_end, color=BLACK):
    """Draws an axis between two points"""    
    tracer(10, 0)
    
    # Set the drawing color
    plot_turtle.color(color)
    
    # Go to the start position
    plot_turtle.teleport(x_start, y_start)
    
    # Point towards the end position
    heading = plot_turtle.towards(x_end, y_end)
    plot_turtle.seth(heading)
    
    # Draw the line
    plot_turtle.pensize(1)
    plot_turtle.pendown()
    plot_turtle.goto(x_end, y_end)
    
    # Stamp the Turtle's shape
    plot_turtle.penup()
    plot_turtle.forward(3)
    plot_turtle.stamp()

    tracer(1, 10)

def draw_axes(color=BLACK):
    """Draws the x- and y-axes"""
    
    # x-axis
    draw_axis(X_MIN, 0, X_MAX - 5, 0, color)
    
    # y-axis
    draw_axis(0, Y_MIN, 0, Y_MAX - 5, color)

# ========
# Plotting
# ========

def plot(f, color=GRAY60):
    """Plots a function in a given color"""
    tracer(10, 0)
    
    # Go to the starting point
    x_start = X_MIN
    y_start = f(X_MIN)
    plot_turtle.teleport(x_start, y_start)
    
    # Plot the function
    plot_turtle.pencolor(color)
    plot_turtle.pensize(3)
    plot_turtle.pendown()
    for x in range(X_MIN, X_MAX, 1):
        y = f(x)
        plot_turtle.goto(x, y)
    
    tracer(1, 10)

def clear():
    """Clears the screen"""
    tracer(10, 0)
    
    plot_turtle.reset()
    plot_turtle.hideturtle()

    tracer(1, 10)

def draw_grid(spacing=50, color=WHITE):
    """Draws horizontal and vertical lines"""
    tracer(10, 0)

    # Go to the origin
    plot_turtle.teleport(0, 0)

    # Draw vertical lines
    plot_turtle.pencolor(color)
    plot_turtle.pensize(1)
    for x in range(0, X_MAX, spacing):
        plot_turtle.penup()
        plot_turtle.goto(x, Y_MIN)
        plot_turtle.pendown()
        plot_turtle.goto(x, Y_MAX)
        plot_turtle.penup()
        plot_turtle.goto(-x, Y_MIN)
        plot_turtle.pendown()
        plot_turtle.goto(-x, Y_MAX)
    
    # Go to the origin
    plot_turtle.teleport(0, 0)
    
    # Draw horizontal lines
    for y in range(0, Y_MAX, spacing):
        plot_turtle.penup()
        plot_turtle.goto(X_MIN, y)
        plot_turtle.pendown()
        plot_turtle.goto(X_MAX, y)
        plot_turtle.penup()
        plot_turtle.goto(X_MIN, -y)
        plot_turtle.pendown()
        plot_turtle.goto(X_MAX, -y)

    tracer(1, 10)

COURIER16 = ["Courier New", 16, "normal"]
COURIER20 = ["Courier New", 20, "normal"]
COURIER24 = ["Courier New", 24, "normal"]

def draw_xlabel(text, color=BLACK, font=COURIER20):
    """Draws the label for the x-axis"""
    tracer(10, 0)

    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.goto(X_MAX - 20, 10)
    plot_turtle.write(text, align="right", font=COURIER20)

    tracer(1, 10)

def draw_ylabel(text, color=BLACK, font=COURIER20):
    """Draws the label for the y-axis"""
    tracer(10, 0)

    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.goto(10, Y_MAX - 20)
    plot_turtle.write(text, align="left", font=font)

    tracer(1, 10)

def draw_title(text, color=BLACK, font=COURIER20):
    """Draws the title"""
    tracer(10, 0)

    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.goto(X_MIN + 10, Y_MAX - 25)
    plot_turtle.write(text, align="left", font=font)

    tracer(1, 10)

# ===========
# Derivatives
# ===========

def diff(f, x, dx=0.001):
    """Estimates a function's derivative with a forward difference"""
    df = f(x + dx) - f(x)
    return df / dx

def draw_tangent(f, x, color=GRAY20, length=200, dx=0.001):
    """Draws a tangent line"""
    tracer(10, 0)
    
    # Go to the point of tangency
    y = f(x)
    plot_turtle.teleport(x, y)
    
    # Draw the point of tangency
    plot_turtle.color(color)
    plot_turtle.pensize(3)
    plot_turtle.pendown()
    plot_turtle.dot()
    
    # Calculate a point along the tangent line
    x1 = x + dx
    y1 = y + dx * diff(f, x, dx)
    
    # Point the turtle along the tangent line
    angle = plot_turtle.towards(x1, y1)
    plot_turtle.seth(angle)
    
    # Draw the tangent line
    plot_turtle.pensize(1)
    plot_turtle.forward(0.5 * length)
    plot_turtle.back(length)
    
    tracer(1, 10)

# =========
# Integrals
# =========

def left_sum(f, x_start, x_end, dx=0.001):
    """Estimates a function's integral with a left Riemann sum"""
    num_steps = int((x_end - x_start) / dx)
    integral = 0
    for i in range(num_steps):
        x_i = x_start + dx * i
        integral += dx * f(x_i)
    return integral

def draw_rect(x, y, width, height, color=GRAY60):
    """Draws a rectangle that is filled with a given color"""

    # Go to the starting point
    plot_turtle.teleport(x, y)

    # Set the drawing color
    plot_turtle.pendown()
    plot_turtle.color(color)

    # Draw the polygon
    plot_turtle.begin_fill()
    plot_turtle.begin_poly()
    plot_turtle.goto(x, y + height)
    plot_turtle.goto(x + width, y + height)
    plot_turtle.goto(x + width, y)
    plot_turtle.goto(x, y)
    plot_turtle.end_poly()
    plot_turtle.end_fill()

def draw_riemann(f, x_start, x_end, dx, color=GRAY60, kind="left"):
    """Fills the area between a curve and the x-axis with rectangles"""
    tracer(10, 0)
    
    # Go to the starting point
    plot_turtle.teleport(x_start, 0)

    # Compute the offset
    num_steps = int((x_end - x_start) / dx)
    if kind == "left":
        offset = 0
    if kind == "middle":
        offset = 0.5
    if kind == "right":
        offset = 1

    # Draw the rectangles
    for i in range(num_steps):
        x_i = x_start + dx * (i + offset)
        y = 0
        width = dx
        height = f(x_i)
        draw_rect(x_i - offset * dx, y, width, height, color)
    
    tracer(1, 10)

def right_sum(f, x_start, x_end, dx=0.001):
    """Estimates a function's integral with a right Riemann sum"""
    integral = 0
    num_steps = int((x_end - x_start) / dx)
    for i in range(num_steps):
        x_i = x_start + dx * (i + 1)
        integral += dx * f(x_i)
    return integral

def middle_sum(f, x_start, x_end, dx=0.001):
    """Estimates a function's integral with a middle Riemann sum"""
    integral = 0
    num_steps = int((x_end - x_start) / dx)
    for i in range(num_steps):
        x_i = x_start + dx * (i + 0.5)
        integral += dx * f(x_i)
    return integral

# ===============
# Vector Graphics
# ===============

def translate_2D(tx, ty):
    """Returns a 2D translation matrix"""
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    return T

def rotate_2D(angle):
    """Returns a 2D rotation matrix"""
    c = np.cos(angle)
    s = np.sin(angle)
    R = np.array([[c, -s, 0],
                  [s,  c, 0],
                  [0,  0, 1]])
    return R

def scale_2D(sx, sy):
    """Returns a 2D scale matrix"""
    S = np.array([[sx,  0, 0],
                  [ 0, sy, 0],
                  [ 0,  0, 1]])
    return S

def translate_3D(tx, ty, tz):
    """Returns a 3D translation matrix"""
    T = np.array([[1, 0, 0, tx],
                  [0, 1, 0, ty],
                  [0, 0, 1, tz],
                  [0, 0, 0,  1]])
    return T

def scale_3D(sx, sy, sz):
    """Returns a 3D scale matrix"""
    S = np.array([[sx,   0,  0, 0],
                  [ 0,  sy,  0, 0],
                  [ 0,   0, sz, 0],
                  [ 0,   0,  0, 1]])
    return S

def rotate_x(angle):
    """Returns a 3D rotation matrix about the x-axis"""
    c = np.cos(angle)
    s = np.sin(angle)
    Rx = np.array([[1,  0, 0, 0],
                   [0,  c, s, 0],
                   [0, -s, c, 0],
                   [0,  0, 0, 1]])
    return Rx

def rotate_y(angle):
    """Returns a 3D rotation matrix about the y-axis"""
    c = np.cos(angle)
    s = np.sin(angle)
    Ry = np.array([[c, 0, -s, 0],
                   [0, 1,  0, 0],
                   [s, 0,  c, 0],
                   [0, 0,  0, 1]])
    return Ry

def rotate_z(angle):
    """Returns a 3D rotation matrix about the z-axis"""
    c = np.cos(angle)
    s = np.sin(angle)
    Rz = np.array([[ c, s, 0, 0],
                   [-s, c, 0, 0],
                   [ 0, 0, 1, 0],
                   [ 0, 0, 0, 1]])
    return Rz

def draw_wireframe(V, E, color=GRAY60):
    """Draws a 3D wireframe given an object's vertices and edges"""
    tracer(10, 0)
    
    # Draw the vertices
    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.pensize(7)
    
    rows, cols = V.shape
    
    for j in range(cols):
        plot_turtle.goto(V[0:2, j])
        plot_turtle.dot()
    
    # Draw the edges
    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.pensize(2)
    
    for j in range(cols):
        root = V[:, j]
        neighbors = E[j]
        for n in neighbors:
            neighbor = V[:, n]
            plot_turtle.penup()
            plot_turtle.goto(root[0:2])
            plot_turtle.pendown()
            plot_turtle.goto(neighbor[0:2])

    tracer(1, 10)

# =============
# Vector Fields
# =============

def create_field(spacing=50, color=GRAY20):
    """Create a list of Turtles to visualize a vector field"""
    tracer(10, 0)

    num_rows = HEIGHT // spacing + 1
    num_cols = WIDTH // spacing + 1
    num_turtles = num_rows * num_cols

    # Construct the Turtle objects
    turtles = [Turtle() for i in range(num_turtles)]
    for t in turtles:
        t.speed(0)
        t.color(color)
        t.penup()
        t.hideturtle()

    # Set their coordinates
    for i in range(num_rows):
        for j in range(num_cols):
            # Access a Turtle
            index = j + i * num_rows
            t = turtles[index]
            # Set the Turtle's coordinates
            x = X_MIN + i * spacing
            y = Y_MIN + j * spacing
            t.teleport(x, y)

    tracer(1, 10)

    return turtles

# Create a default list of Turtles
FIELD_ARROWS = create_field()

def hide_field():
    """Hide the Turtles used to draw a vector field"""
    tracer(10, 0)

    for t in FIELD_ARROWS:
        t.hideturtle()
    
    tracer(1, 10)

def show_field():
    """Show the Turtles used to draw a vector field"""
    tracer(10, 0)

    for t in FIELD_ARROWS:
        t.showturtle()
    
    tracer(1, 10)

def draw_field(field, scale=0.007, min_scale=0.001):
    """Draw a vector field using arrows"""
    show_field()

    tracer(10, 0)

    for t in FIELD_ARROWS:
        # Calculate the field
        x, y = t.pos()
        state = np.array([x, y])
        change = field(state)
        # Point the Turtle along the field
        next_state = state + change
        next_x, next_y = next_state
        angle = t.towards(next_x, next_y)
        t.seth(angle)
        # Set the Turtle size based on the field magnitude
        size = np.linalg.norm(change) * scale + min_scale
        t.shapesize(size)
    
    tracer(1, 10)

def integrate_field(field, initial_state, t_f, num_vars=2, dt=0.001):
    """Integrates a vector field and returns a trajectory"""
    num_steps = int(t_f / dt)
    trajectory = np.zeros([num_vars, num_steps])
    trajectory[:, 0] = initial_state
    
    for i in range(1, num_steps):
        state = trajectory[:, i - 1]
        change = field(state)
        next_state = state + dt * change
        trajectory[:, i] = next_state
    
    return trajectory

def draw_trajectory_2D(trajectory, start_color=BLACK, end_color=WHITE):
    """Draws a 2D trajectory through a vector field"""
    tracer(10, 0)

    # Prepare to draw
    x, y = trajectory[0:2, 0]
    plot_turtle.teleport(x, y)
    plot_turtle.pendown()
    plot_turtle.pensize(1)

    # Integrate the vector field
    num_steps = trajectory.shape[1]
    for i in range(num_steps):
        pct = i / num_steps
        color = blend_colors(start_color, end_color, pct)
        plot_turtle.color(color)
        x, y = trajectory[0:2, i]
        plot_turtle.goto(x, y)
    
    tracer(1, 10)

I4 = np.eye(4) # Identity matrix

def draw_axes_3D(A=I4, axis_length=30, font=COURIER20):
    """Draws axes in 3D"""
    a = axis_length
    origin = np.array([0, 0, 0, 1])
    x_axis = np.array([a, 0, 0, 1])
    y_axis = np.array([0, a, 0, 1])
    z_axis = np.array([0, 0, a, 1])
    axes = [[x_axis, "x"], [y_axis, "y"], [z_axis, "z"]]

    tracer(10, 0)
    for axis in axes:
        point, name = axis
        start = A @ origin
        end = A @ point
        plot_turtle.color(BLACK)
        plot_turtle.pensize(3)
        plot_turtle.penup()
        plot_turtle.goto(start[0:2])
        plot_turtle.pendown()
        plot_turtle.goto(end[0:2])
        plot_turtle.penup()
        plot_turtle.goto(end[0:2] * 1.5)
        plot_turtle.write(name, align="center", font=font)
    tracer(1, 10)

def draw_trajectory_3D(trajectory, A=I4, start_color=BLACK, end_color=WHITE):
    """Draws a 3D trajectory through a vector field"""
    tracer(10, 0)

    # Prepare to draw
    num_steps = trajectory.shape[1]
    trajectory_h = np.ones([4, num_steps])
    trajectory_h[0:3, :] = trajectory
    trajectory_h = A @ trajectory_h
    x, y = trajectory_h[0:2, 0]
    plot_turtle.teleport(x, y)
    plot_turtle.pendown()
    plot_turtle.pensize(1)

    # Integrate the vector field
    for i in range(num_steps):
        pct = i / num_steps
        color = blend_colors(start_color, end_color, pct)
        plot_turtle.color(color)
        x, y = trajectory_h[0:2, i]
        plot_turtle.goto(x, y)
    
    tracer(1, 10)

# =============
# Surface Plots
# =============

def draw_quad(V, color=GRAY60):
    """Draws a quadrilateral"""
    x, y = V[0:2, 0]
    plot_turtle.teleport(x, y)
    plot_turtle.color(color)
    plot_turtle.pendown()
    plot_turtle.begin_fill()
    plot_turtle.begin_poly()
    for i in range(4):
        x, y = V[0:2, i]
        plot_turtle.goto(x, y)
    x, y = V[0:2, 0]
    plot_turtle.goto(x, y)
    plot_turtle.end_poly()
    plot_turtle.end_fill()

def normalize(a):
    """Normalizes the values in an array"""
    a_min = np.min(a)
    a_max = np.max(a)
    a_range = a_max - a_min
    if a_range == 0:
        return np.zeros(a.shape)
    a_n = (a - a_min) / a_range
    return a_n

def get_corners(M, i, j):
    """Gets the four values surrounding a grid cell"""
    m0 = M[i, j]         # Top-left
    m1 = M[i + 1, j]     # Bottom-left
    m2 = M[i + 1, j + 1] # Bottom-right
    m3 = M[i, j + 1]     # Top-right
    return [m0, m1, m2, m3]

def get_vertices(X, Y, Z, i, j):
    """Returns the homogeneous coordinates of the face's vertices"""
    x0, x1, x2, x3 = get_corners(X, i, j)
    y0, y1, y2, y3 = get_corners(Y, i, j)
    z0, z1, z2, z3 = get_corners(Z, i, j)
    V = np.array([[x0, x1, x2, x3],
                  [y0, y1, y2, y3],
                  [z0, z1, z2, z3],
                  [ 1,  1,  1,  1]])
    return V

def plot_surface(X, Y, Z, A=I4, min_color=BLACK, max_color=WHITE):
    """Plots a 3D surface with a given transformation"""
    tracer(10, 0)
    
    # Get the number of rows/columns
    N = X.shape[0]
    # Normalize each vertex
    Z_n = normalize(Z)
    for i in range(N - 1):
        for j in range(N - 1):
            # Get the face's vertex coordinates
            V = get_vertices(X, Y, Z, i, j)
            # Change the basis for drawing
            V = A @ V
            # Compute the face's average color
            z = get_corners(Z_n, i, j)
            pct = np.sum(z) / 4
            color = blend_colors(min_color, max_color, pct)
            # Draw the face
            draw_quad(V, color)
    
    tracer(1, 10)

# ====
# Data
# ====

def get_interval(data):
    """Returns the interval of a dataset"""
    data_min = np.min(data)
    data_max = np.max(data)
    return np.array([data_min, data_max])

def draw_xticks(labels, length=10, color=BLACK, font=COURIER16):
    """Draw tick marks along the x-axis"""
    tracer(10, 0)

    plot_turtle.color(color)
    plot_turtle.pendown()
    
    for label in labels:
        text, x = label
        plot_turtle.teleport(x, 0)
        plot_turtle.goto(x, -length)
        plot_turtle.teleport(x, -length * 2.5)
        plot_turtle.write(text, align="center", font=font)

    tracer(1, 10)

def draw_yticks(labels, length=10, color=BLACK, font=COURIER16):
    """Draw tick marks along the y-axis"""
    tracer(10, 0)

    plot_turtle.color(color)
    plot_turtle.pendown()
    
    for label in labels:
        text, y = label
        plot_turtle.teleport(0, y)
        plot_turtle.goto(-length, y)
        plot_turtle.teleport(-length * 2.5, y)
        plot_turtle.write(text, align="center", font=font)

    tracer(1, 10)

def scatter(x, y, xscale=1, yscale=1, color=WHITE, size=5):
    """Draws a scatter plot of y vs x"""
    tracer(10, 0)

    plot_turtle.color(color)

    x = xscale * x
    y = yscale * y

    num_points = len(x)
    for i in range(num_points):
        plot_turtle.teleport(x[i], y[i])
        plot_turtle.dot(size)
    
    tracer(1, 10)

def plot_regression(w, b, xscale=1, yscale=1, color=GRAY60, weight=1):
    """Draws a regression line"""
    tracer(10, 0)
    
    y_start = (w * (X_MIN / xscale) + b) * yscale
    y_end = (w * (X_MAX / xscale) + b) * yscale

    plot_turtle.penup()
    plot_turtle.color(color)
    plot_turtle.pensize(weight)

    plot_turtle.goto(X_MIN, y_start)
    plot_turtle.pendown()
    plot_turtle.goto(X_MAX, y_end)
    
    tracer(1, 10)

# =======
# Fourier
# =======

def draw_complex(z, color=GRAY60):
    """Draws a complex number as an arrow"""
    tracer(10, 0)
    
    # Set the drawing color
    plot_turtle.color(color)

    # Draw the vector
    re = np.real(z)
    im = np.imag(z)
    plot_turtle.teleport(0, 0)
    # Point towards the end position
    heading = plot_turtle.towards(re, im)
    plot_turtle.seth(heading)
    # Draw the line
    plot_turtle.pensize(1)
    plot_turtle.pendown()
    mag = abs(z)
    plot_turtle.forward(mag)
    # Stamp the Turtle's shape
    plot_turtle.penup()
    plot_turtle.forward(3)
    plot_turtle.stamp()

    tracer(1, 10)

def plot_spectrum(s_hat, num_bins=100, color=GRAY60):
    """Plots a signal's spectrum"""
    tracer(10, 0)

    # Calculate the size of the bins
    N = len(s_hat)
    bin_width = int(N / num_bins)

    # Add the DFT values within each interval
    bin_total = np.zeros(num_bins)
    s_hat_n = normalize(np.abs(s_hat))
    for i in range(num_bins):
        start = i * bin_width
        stop = (i + 1) * bin_width
        bin_total[i] = np.sum(s_hat_n[start:stop])

    # Prepare to plot
    plot_turtle.teleport(0, 0)

    # Plot the spectrum
    x = np.linspace(0, X_MAX, num_bins)
    y = 0
    width = X_MAX / num_bins
    height = Y_MAX * normalize(bin_total)
    for i in range(num_bins):
        draw_rect(x[i], 0, width, height[i], color)

    tracer(1, 10)
