from graphics import *

def main():

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 100000), ' 10.0K').draw(win)

    Text(Point(2,10000), " Principal: ").draw(win)
    Text(Point(3,9000), " Interest Rate: ").draw(win)
    output = Text(Point(3,8000), " Investment: ").draw(win)

    principal_field = Entry(Point(4,10000),4)
    principal_field.setText("0.0")
    principal_field.draw(win)
    apr_field = Entry(Point(4,9000),4)
    apr_field.setText("0.0")
    apr_field.draw(win)

    win.getMouse()

    principal = eval(principal_field.getText())
    apr = eval(apr_field.getText())

    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point (year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    output.setText(principal)
    win.getMouse()
    win.close()

main()
