import turtle
import math
"""
Faba Kouyate | Fall, 2025
"""

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)

# Function to draw a line between two points
def draw_line(x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

# Define the 8 vertices of a cube in 3D space
# Then project them to 2D for isometric view
vertices = [
    (-100, -100, -100),  # 0
    (100, -100, -100),   # 1
    (100, 100, -100),    # 2
    (-100, 100, -100),   # 3
    (-100, -100, 100),   # 4
    (100, -100, 100),    # 5
    (100, 100, 100),     # 6
    (-100, 100, 100)     # 7
]

# Function to project 3D point to 2D isometric view
def project_3d_to_2d(x, y, z):
    iso_x = x - z
    iso_y = y - (x + z) * 0.5
    return iso_x, iso_y

# Project all vertices to 2D
projected = [project_3d_to_2d(v[0], v[1], v[2]) for v in vertices]

# Define the edges of the cube
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Front face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Back face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
]

# Set pen properties
t.pensize(2)
t.pencolor("black")

# Draw all edges
for edge in edges:
    p1 = projected[edge[0]]
    p2 = projected[edge[1]]
    draw_line(p1[0], p1[1], p2[0], p2[1])

# Hold window open
turtle.done()