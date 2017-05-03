from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(60,60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        tx = p.getX() - 5
        ty = p.getY() - 5
        bx = p.getX() + 5
        by = p.getY() + 5
        shape = Rectangle(Point(bx, by), Point(tx, ty))
        shape.setFill("blue")
        shape.draw(win)
    closing_message = Text(Point(50, 10),'Click to Exit').draw(win)
    win.getMouse()
    win.close()
main()

