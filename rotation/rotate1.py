# draws a triangle and rotates it by 30 degress (method 1)
import pygame 
from sys import exit
import math

width = 700
height = 500
origin_x = width // 2
origin_y = height // 2

screen = pygame.display.set_mode((width, height))
screen.fill("Green")
surface = pygame.Surface((width, height))
surface.fill("White")

triangle_coordinates = {
    "A": (0, -150),
    "B": (-150, 150),
    "C": (150, 150)
}
rotation_deg = math.radians(30)

def to_pygame_coords(custom_x, custom_y):
    pygame_x = origin_x + custom_x
    pygame_y = origin_y - custom_y
    return (pygame_x, pygame_y)

def draw_triangle(triangle_coords, color, width): 
    line_AB = pygame.draw.line(surface, color, to_pygame_coords(triangle_coords["A"][0], triangle_coords["A"][1]), to_pygame_coords(triangle_coords["B"][0], triangle_coords["B"][1]), width)
    line_BC = pygame.draw.line(surface, color, to_pygame_coords(triangle_coords["B"][0], triangle_coords["B"][1]), to_pygame_coords(triangle_coords["C"][0], triangle_coords["C"][1]), width)
    line_AC = pygame.draw.line(surface, color, to_pygame_coords(triangle_coords["A"][0], triangle_coords["A"][1]), to_pygame_coords(triangle_coords["C"][0], triangle_coords["C"][1]), width)

draw_triangle(triangle_coordinates, "Blue", 5) # triangle without any rotation

# functions to get new coordinates for rotation of the triangle
def x_coordinate(x, y): 
    return ((x * math.cos(rotation_deg)) - (y * math.sin(rotation_deg)))
def y_coordinate(x, y): 
    return ((x * math.sin(rotation_deg)) + (y * math.cos(rotation_deg)))
def rotate_triangle(): 
    triangle_rotate = {
        "A": (x_coordinate(triangle_coordinates["A"][0], triangle_coordinates["A"][1]), y_coordinate(triangle_coordinates["A"][0],triangle_coordinates["A"][1])),
        "B": (x_coordinate(triangle_coordinates["B"][0], triangle_coordinates["B"][1]), y_coordinate(triangle_coordinates["B"][0],triangle_coordinates["B"][1])),
        "C": (x_coordinate(triangle_coordinates["C"][0], triangle_coordinates["C"][1]), y_coordinate(triangle_coordinates["C"][0], triangle_coordinates["C"][1]))
    }
    draw_triangle(triangle_rotate, "Red", 3) # triangle after rotation

rotate_triangle()
clock = pygame.time.Clock()
pygame.init()
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.QUIT()
            exit()
    screen.blit(surface, (0, 0))
    pygame.display.update()
    clock.tick(60)
