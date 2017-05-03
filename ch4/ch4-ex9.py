from graphics import *

def main():
    win = GraphWin("Rectangle Information", 400, 400)
    win.setBackground("white")
    win.setCoords(-10.0, -10.0, 10.0, 10.0)

    Text(Point(0,9.5)," Click Twice To Draw Rectangle ").draw(win)

    point1 = win.getMouse()
    point2 = win.getMouse()

    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()

    length = x1 - x2
    width = y1 - y2
    length = abs(length)
    width = abs(width)

    area = length * width
    perimeter = 2 * (length + width)

    rectangle = Rectangle(point1, point2)

    rectangle.draw(win)

    area_value = Text(Point(0,8.5),"").draw(win)
    perimeter_value = Text(Point(0,7.5),"").draw(win)

    area_value.setText("Area:" + str(area))
    perimeter_value.setText("Perimeter:" + str(perimeter))

    win.getMouse()
    win.close()

main()