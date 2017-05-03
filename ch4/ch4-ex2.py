from graphics import *

def main():
    win = GraphWin('Bullseye!')
    win.setBackground('white')
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    yellow = Circle(Point(5,5),5)
    red = Circle(Point(5,5),4)
    blue = Circle(Point(5,5),3)
    black = Circle(Point(5,5),2)
    white = Circle(Point(5,5),1)
    yellow.setFill('yellow')
    red.setFill('red')
    blue.setFill('blue')
    black.setFill('black')
    white.setFill('white')
    yellow.draw(win)
    red.draw(win)
    blue.draw(win)
    black.draw(win)
    white.draw(win)

main()
