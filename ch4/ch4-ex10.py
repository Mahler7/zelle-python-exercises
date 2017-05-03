from graphics import *
import math

def main():
    win = GraphWin("Triangle Information", 400, 400)
    win.setBackground("white")
    win.setCoords(-10.0, -10.0, 10.0, 10.0)

    Text(Point(0,9.5)," Click Thrice To Draw Triangle ").draw(win)

    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()

    x1 = point1.getX()
    x2 = point2.getX()
    x3 = point3.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    y3 = point3.getY()

    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x3 - x2
    dy2 = y3 - y2
    dx3 = x1 - x3
    dy3 = y1 - y3

    side1_length = math.sqrt(dx1 ** 2 + dy1 ** 2)
    side2_length = math.sqrt(dx2 ** 2 + dy2 ** 2)
    side3_length = math.sqrt(dx3 ** 2 + dy3 ** 2)
    
    perimeter = side1_length + side2_length + side3_length
    s = perimeter / 2
    area = math.sqrt(s * (s - side1_length) * (s - side2_length) * (s - side3_length))

    triangle = Polygon(point1, point2, point3)
    triangle.draw(win)

    area_value = Text(Point(0,8.5),"").draw(win)
    perimeter_value = Text(Point(0,7.5),"").draw(win)

    area_value.setText("Area:" + str(area))
    perimeter_value.setText("Perimeter:" + str(perimeter))

main()