from typing import List
import numpy as np
import cv2
import math
import os
from datetime import datetime

def calculate_angle(img: np.ndarray, cal_point: tuple, poly_points: List[tuple], prefix: str) -> list:
    img_draw = img.copy()
    for point in poly_points:
        cv2.circle(img_draw, point, 5, (0, 0, 255), -1)
    cv2.circle(img_draw, cal_point, 5, (0, 255, 0), -1)

    angle = 0
    path_ = os.path.join("results", prefix, str(datetime.now().microsecond))
    for idx in range(len(poly_points)):
        p1, p2 = poly_points[idx], poly_points[idx-1]
        vec_a = np.array([p1[0] - cal_point[0], p1[1] - cal_point[1]])
        vec_b = np.array([p2[0] - cal_point[0], p2[1] - cal_point[1]])

        theta = math.acos(np.dot(vec_a, vec_b)/np.linalg.norm(vec_a, 2)/np.linalg.norm(vec_b, 2))
        angle += theta

        tmp_img = img_draw.copy()
        color_1 = (0, 0, 255)
        color_2 = (0, 0, 128)

        cv2.line(tmp_img, p1, cal_point, color_1, 3)
        cv2.line(tmp_img, p2, cal_point, color_2, 3)
        cv2.putText(tmp_img, f"{theta * 180 / math.pi: .3f}", (10, 40), 2, 1, (0, 0, 0))

        if not os.path.exists(path_):
            os.makedirs(path_)
        cv2.imwrite(os.path.join(path_, f"{idx}.png"), tmp_img)
    tmptmp = img.copy()
    cv2.putText(tmptmp, f"{angle * 180 / math.pi: .3f}", (10, 40), 2, 1, (0, 0, 0))
    for i in range(5):
        cv2.imwrite(os.path.join(path_, f"{i+len(poly_points)}.png"), tmptmp)
    os.system("convert -delay 15 -loop 0  " + os.path.join(path_, "*.png") + " " + os.path.join(path_, "vis.gif"))

    return angle % math.pi * 180 / math.pi

    
    
    