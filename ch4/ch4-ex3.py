from graphics import *

def main():
    win = GraphWin('Smile Your Face')
    win.setBackground('white')
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    head = Circle(Point(5,5),5)
    head.setFill('yellow')
    lefteye = Circle(Point(3,7),1)
    lefteye.setFill('black')
    righteye = lefteye.clone()
    righteye.move(4,0)
    mouth = Oval(Point(3,1), Point(7,2))
    mouth.setFill('black')
    
    head.draw(win)
    lefteye.draw(win)
    righteye.draw(win)
    mouth.draw(win)

main()
