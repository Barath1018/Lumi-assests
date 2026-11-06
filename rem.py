import cv2
import numpy as np

img = cv2.imread("image.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 30, 30])
upper_green = np.array([90, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)

# Smooth edges
mask = cv2.GaussianBlur(mask, (5, 5), 0)

alpha = 255 - mask

b, g, r = cv2.split(img)
rgba = cv2.merge([b, g, r, alpha])

cv2.imwrite("sheet3.png", rgba)