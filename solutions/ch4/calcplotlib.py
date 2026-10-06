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
