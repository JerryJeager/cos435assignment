# draws a triangle and perform translation on it (method 2)
import pygame
import sys

# Initialize Pygame
pygame.init()

# Define window size
window_width = 800
window_height = 600

# Set up the display
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Triangle Translation")

# Define the origin
origin_x = window_width // 2
origin_y = window_height // 2

# Define translate points
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

def translate_point(x, y):
    new_x = x + dx
    new_y = y + dy
    return new_x, new_y

def translate_triangle(vertices):
    return [translate_point(x, y) for x, y in vertices]

# translate triangle
translated_vertices = translate_triangle(triangle_vertices)

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

    # Draw the translated triangle
    pygame_translated_triangle = [to_pygame_coords(x, y) for x, y in translated_vertices]
    pygame.draw.polygon(window, (255, 0, 0), pygame_translated_triangle, 1)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
