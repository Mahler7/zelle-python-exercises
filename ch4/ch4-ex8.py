from graphics import *
import math

def main():
    win = GraphWin("Line Segment Information", 400, 400)
    win.setBackground("white")
    win.setCoords(-10.0, -10.0, 10.0, 10.0)

    Text(Point(-1,9.5)," Click Twice To Draw Line ").draw(win)

    point1 = win.getMouse()
    point2 = win.getMouse()
    
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()

    dx = x2 - x1
    dy = y2 - y1
    slope = dy / dx
    length = math.sqrt(dx ** 2 + dy ** 2)
    
    line = Line(point1, point2)
    midpoint = line.getCenter()

    line.setFill("red")
    midpoint.setFill("cyan")

    line.draw(win)
    midpoint.draw(win)

    length_value = Text(Point(-1,8.5),"").draw(win)
    slope_value = Text(Point(-1,7.5),"").draw(win)

    length_value.setText("Length:" + str(length))
    slope_value.setText("Slope:" + str(slope))

    win.getMouse()
    win.close()

main()