#!/usr/bin/env python

import numpy as np
from PIL import Image
import math as math

def transform(x, y, matrix):
	(a, b, c, d, e, f) = matrix
	return a*x + b*y + c, d*x + e*y + f

angle = int(input("Enter angle to be rotated by: "))
img = Image.open(r"assets/rotate.png")
img.show()

angle = angle % 360.0
w, h = img.size
angle = -math.radians(angle)
matrix = [math.cos(angle),math.sin(angle),0.0,-math.sin(angle),math.cos(angle),0.0]
center = (int(w/2.0), int(h/2.0))
matrix[2], matrix[5] = transform(-center[0], center[1], matrix)
matrix[2] += center[0]
matrix[5] += center[1]

rotated_img1 = img.transform((w, h), 0, matrix)

xx = []
yy = []
for x, y in ((0, 0), (w, 0), (w, h), (0, h)):
	x, y = transform(x, y, matrix)
	xx.append(x)
	yy.append(y)
	nw = math.ceil(max(xx)) - math.floor(min(xx))
	nh = math.ceil(max(yy)) - math.floor(min(yy))
	matrix[2], matrix[5] = transform(-(nw - w) / 2.0, -(nh - h) / 2.0, matrix)
	w, h = nw, nh

w = int(w)
h = int(h)

rotated_img2 = img.transform((w, h), 0, matrix)

rotated_img1.show()
rotated_img2.show()
rotated_img1.save("output/Partial.png")
rotated_img2.save("output/Full.png")
