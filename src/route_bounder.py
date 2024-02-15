import math
import sys 

def calc_bounds(p0: tuple, p1: tuple, radius: float):
    p0p1_run = p0[0] - p1[0]
    p0p1_rise = p0[1] - p1[1]
    if p0p1_run == 0:
        p0p1_run = sys.float_info.min 

    p0p1_slope = p0p1_rise / p0p1_run


    p1_beta = math.atan(p0p1_slope)

    r = radius
    a_0 = r * math.cos(p1_beta)
    b_0 = r * math.sin(p1_beta)

    x_0 = p0[0] - b_0
    y_0 = p0[1] + a_0

    x_1 = p0[0] + b_0
    y_1 = p0[1] - a_0

    return ((x_0, y_0), (x_1, y_1))

def create_polygon(route, radius):
    """Return a list of coordinates (long, lat) that create the bounded polygon for this route"""
    coordinates = [route[0]]
    for i in range(len(route) - 1):
        waypoint_a = route[i]
        waypoint_b = route[i + 1]
        for bounds in calc_bounds(waypoint_a, waypoint_b, radius):
            coordinates.append(bounds)
    coordinates.append(route[:-1])
    return coordinates
