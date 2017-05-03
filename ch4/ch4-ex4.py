from graphics import *

def main():
    win = GraphWin('Snowman Tree')
    win.setCoords(0.0, 0.0, 20.0, 12.0)
    stump = Rectangle(Point(4,0), Point(6,2))
    stump.setFill('brown')
    basetree = Polygon(Point(1,2),Point(9,2),Point(5,6))
    basetree.setFill('green')
    midtree = Polygon(Point(2,4),Point(8,4),Point(5,8))
    midtree.setFill('green')
    toptree = Polygon(Point(3,6),Point(7,6),Point(5,10))
    toptree.setFill('green')
    
    baseman = Circle(Point(15,3),3)
    baseman.setFill('white')
    midman = Circle(Point(15,6),2)
    midman.setFill('white')
    topman = Circle(Point(15,8),1)
    topman.setFill('white')

    stump.draw(win)
    basetree.draw(win)
    midtree.draw(win)
    toptree.draw(win)

    baseman.draw(win)
    midman.draw(win)
    topman.draw(win)

main()