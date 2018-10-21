import bpy
import math

"""Moves selected object to predefined xyz"""
def reset_pos():
    bpy.context.object.location[0] = 0
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0

"""Returns Vector2 around a circle given an angle assuming radius of 1"""
def rotate_pos(radian):
    rotated_pos = [0.0, 0.0, 0.0]
    radius = 1 #get_length_2d(origin, pos)
    rotated_pos[0] = math.cos(radian) * radius
    rotated_pos[1] = math.sin(radian) * radius
    return(rotated_pos)

"""Returns a scalar representing the length betwene two Vector2"""
def get_length_2d(a, b):
    length_ab = math.sqrt(
        (b[0] - a[0])**2 +
        (b[1] - a[1])**2)
    return(length_ab)

def degree_to_radian(degree):
    return(degree * math.pi/180)

reset_pos()
new_pos = rotate_pos(degree_to_radian(60))
bpy.context.object.location=(new_pos)
