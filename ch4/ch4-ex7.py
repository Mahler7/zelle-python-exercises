from graphics import *
import math

def main():
    win = GraphWin("Circle Intersection Chart", 400, 400)
    win.setBackground("white")
    win.setCoords(-10.0, -10.0, 10.0, 10.0)

    Text(Point(-2,9)," Radius: ").draw(win)
    Text(Point(-2.5,8)," Y-Intercept: ").draw(win)
    x1_value = Text(Point(-2,7)," First X: ").draw(win)
    x2_value = Text(Point(-2,6)," Second X: ").draw(win)

    radius_field = Entry(Point(0,9),4)
    radius_field.setText("0.0")
    radius_field.draw(win)
    y_intercept_field = Entry(Point(0,8),4)
    y_intercept_field.setText("0.0")
    y_intercept_field.draw(win)

    win.getMouse()

    radius = eval(radius_field.getText())
    y_intercept = eval(y_intercept_field.getText())

    x1 = math.sqrt(radius ** 2 - y_intercept ** 2) * -1
    x2 = math.sqrt(radius ** 2 - y_intercept ** 2)

    circle = Circle(Point(0,0),radius)
    circle.draw(win)
    line = Line(Point(x1,y_intercept), Point(x2,y_intercept))
    line.setFill("red")
    line.draw(win)

    x1_value.setText(x1)
    x2_value.setText(x2)

    win.getMouse()
    win.close

main()