from PIL import Image
from Vec3 import vec3
from Ray import ray
from PPM import ppm
import os
import math
# from os.path import splitext

# http://www.realtimerendering.com/raytracing/Ray%20Tracing%20in%20a%20Weekend.pdf
# https://www.python-course.eu/python3_magic_methods.php

def color(r):
    # bgColor = vec3(0.5, 0.7, 1.0)
    t = hit_sphere(vec3(0,0,-1), 0.50, r)
    if t > 0.0:
        N = vec3.unit_vector(r.point_at_parameter(t) - vec3(0,0,-1))
        return 0.5 * vec3(N.x+1, N.y+1, N.z+1)
    unit_direction = vec3.unit_vector(r.direction)
    t = 0.5*(unit_direction.y + 1.0)
    return (1.0-t)*vec3(1.0, 1.0, 1.0) + t * vec3(0.5, 0.7, 1.0)

def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = vec3.dot(r.direction, r.direction)
    b = 2.0 * vec3.dot(oc, r.direction)
    c = vec3.dot(oc, oc) - radius*radius
    discriminat = b*b - 4 * a * c
    if discriminat < 0:
        return -1.0
    else:
        return (-b - math.sqrt(discriminat)) / (2.0 * a)

def render(width=200, height=100):
    hor_size = 4.0
    ver_size = hor_size * 0.5
    line = []
    # Preload function
    line_append = line.append
    frame  = []
    # Preload function
    frame_append = frame.append
    nx = width
    ny = height
    lower_left_corner = vec3(-(hor_size / 2.0), -(ver_size / 2.0), -1.0)
    horizontal = vec3(hor_size, 0.0, 0.0)
    vertical = vec3(0.0, ver_size, 0.0)
    origin = vec3(0.0, 0.0, 0.0)

    for j in range(ny-1, -1, -1):
        line.clear()
        v = float(j) / float(ny)
        for i in range(nx):
            u = float(i) / float(nx)
            r = ray(origin, lower_left_corner + u*horizontal + v*vertical)
            col = color(r)
            #pix = vec3(int(255.99 * col.r), int(255.99 * col.g), int(255.99 * col.b))
            #line.append([pix.x, pix.y, pix.z])
            # line.append([int(255.99 * col.r), int(255.99 * col.g), int(255.99 * col.b)])
            line_append([int(255.99 * col.r), int(255.99 * col.g), int(255.99 * col.b)])
        # frame.append(line.copy())
        frame_append(line.copy())
    return frame

def run_render(file_name='output.ppm', width=200, height=100, scale=1.0, binary=True):
    nx = int(width * scale)
    ny = int(height * scale)
    with ppm(file_name,nx,ny,binary) as f:
        f.write_data(render(nx, ny))
        f.saveas(file_format='png', delete_source=False)


if __name__ == '__main__':
    fname = 'output.ppm'
    run_render(file_name=fname, width=200, height=100, scale=5.0, binary=True)


