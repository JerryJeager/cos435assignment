# draws a triangle and rotates it by 30 degress (method 2)
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Define window size
window_width = 800
window_height = 600

# Set up the display
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Triangle Rotation")

# Define the origin
origin_x = window_width // 2
origin_y = window_height // 2

# Define rotate points
dx = 50
dy = 60

# Define the triangle vertices (relative to the origin)
triangle_vertices = [
    (0, -100),  # Top vertex
    (-100, 100),  # Bottom left vertex
    (100, 100)  # Bottom right vertex
]

def to_pygame_coords(custom_x, custom_y):
    pygame_x = origin_x + custom_x
    pygame_y = origin_y - custom_y
    return pygame_x, pygame_y

def rotate_point(x, y, angle):
    rad = math.radians(angle)
    cos_rad = math.cos(rad)
    sin_rad = math.sin(rad)
    new_x = x * cos_rad - y * sin_rad
    new_y = x * sin_rad + y * cos_rad
    return new_x, new_y

def rotate_triangle(vertices, angle):
    return [rotate_point(x, y, angle) for x, y in vertices]

# rotate triangle
rotated_vertices = rotate_triangle(triangle_vertices, 30)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    window.fill((255, 255, 255))

    # Draw the original triangle
    pygame_triangle = [to_pygame_coords(x, y) for x, y in triangle_vertices]
    pygame.draw.polygon(window, (0, 0, 255), pygame_triangle, 1)

    # Draw the rotated triangle
    pygame_rotated_triangle = [to_pygame_coords(x, y) for x, y in rotated_vertices]
    pygame.draw.polygon(window, (255, 0, 0), pygame_rotated_triangle, 1)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
