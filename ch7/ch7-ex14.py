from graphics import *
import math

def no_intersect(x1_value, x2_value):
    x1_value.setText("This line doesn't")
    x2_value.setText("intersect the circle")    

def draw_circle(win, radius, y_intercept, x1_value, x2_value, x1, x2):
    circle = Circle(Point(0,0),radius)
    circle.draw(win)
    line = Line(Point(x1,y_intercept), Point(x2,y_intercept))
    line.setFill("red")
    line.draw(win)

    x1_value.setText(x1)
    x2_value.setText(x2)

def calculate_circle(radius, y_intercept, x1_value, x2_value):  
    num1 = (radius ** 2 - y_intercept ** 2)* -1
    num2 = radius ** 2 - y_intercept ** 2
    if num1 < 0 or num2 < 0:
        no_intersect(x1_value, x2_value)
    else:
        x1 = math.sqrt(num1) 
        x2 = math.sqrt(num2)
        return x1, x2

def get_inputs(radius_field, y_intercept_field):
    radius = eval(radius_field.getText())
    y_intercept = eval(y_intercept_field.getText())
    return radius, y_intercept

def draw_inputs(win):
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

    return radius_field, y_intercept_field, x1_value, x2_value

def draw_window():
    win = GraphWin("Circle Intersection Chart", 400, 400)
    win.setBackground("white")
    win.setCoords(-10.0, -10.0, 10.0, 10.0)
    return win

def main():
    win = draw_window()
    radius_field, y_intercept_field, x1_value, x2_value = draw_inputs(win)
    win.getMouse()
    radius, y_intercept = get_inputs(radius_field, y_intercept_field)
    x1, x2 = calculate_circle(radius, y_intercept, x1_value, x2_value)
    draw_circle(win, radius, y_intercept, x1_value, x2_value, x1, x2)
    win.getMouse()
    win.close

main()
