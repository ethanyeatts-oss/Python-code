import math


def main():

    point1 = get_point(1)
    point2 = get_point(2)

    distance = Calc_distance(point1, point2)

    print_output(distance)

def get_point(point_number):
    x = float(input(f"Enter the x corridante for point {point_number}: "))
    y = float(input(f"Enter the y corridante for point {point_number}: "))


    return (x,y)

def Calc_distance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return distance

def print_output(distance):

    print(f"The distance between the points is {distance:.3f}")

main()