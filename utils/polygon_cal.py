from typing import List
import os.path
import numpy as np
import cv2
from utils.tools import calculate_angle

def polygon(poly_points: List[tuple], in_pt: tuple, out_pt: tuple) -> None:
    w, h = 0, 0
    for pt in poly_points:
        if w < pt[0]: w = pt[0]
        if h < pt[1]: h = pt[1]
    w, h = int(w * 1.5), int(h * 1.5)
    
    img = np.full((h, w, 3), 255, dtype=np.uint8)
    for idx in range(len(poly_points)):
        p1, p2 = poly_points[idx-1], poly_points[idx]
        cv2.line(img, p1, p2, (0, 0, 0), 5)
    in_angle = calculate_angle(img, in_pt, poly_points, "in")
    out_angle = calculate_angle(img, out_pt, poly_points, "out")
    print(f"in_pt: total angle: {in_angle : .2f}")
    print(f"out_pt: total angle: {out_angle: .2f}")

    return