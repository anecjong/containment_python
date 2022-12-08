#! /usr/bin/env python3
from utils.polygon_cal import *
from utils.tools import remove_dummy_data

def convex():
    remove_dummy_data()
    print("====angle calculation is valid if polygon is convex====")
    poly_points = [(100, 100), (500, 100), (500, 200), (300, 300), (100, 200)]
    out_pt = (30, 300)
    in_pt = (200, 150)
    polygon(poly_points, in_pt, out_pt)

def concave():
    '''
    THIS EXAMPLE IS NOT VALID
    '''
    remove_dummy_data()
    print("====angle calculation is valid if polygon is convex====")
    print("====This example is concave, so it does not give right answer====")
    poly_points = [(159, 195), (192, 558), (625, 443), (292, 303), (718, 296), (354, 61)]
    out_pt = (524, 342)
    in_pt = (293, 194)
    polygon(poly_points, in_pt, out_pt)

def main():
    concave()
    convex()


if __name__ == "__main__":
    main()