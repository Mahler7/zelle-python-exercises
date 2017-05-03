from graphics import *

def main():
    win = GraphWin("5 Dice")
    win.setCoords(0.0, 0.0, 26, 26)
    
    die1 = Rectangle(Point(1,13), Point(5,17))
    die2 = die1.clone()
    die2.move(5,0)
    die3 = die2.clone()
    die3.move(5,0)
    die4 = die3.clone()
    die4.move(5,0)
    die5 = die4.clone()
    die5.move(5,0)

    die1_dot1 = Circle(Point(3,15),0.25)
    
    die2_dot1 = Circle(Point(7,16),0.25)
    die2_dot2 = Circle(Point(9,14),0.25)

    die3_dot1 = Circle(Point(12,16),0.25)
    die3_dot2 = Circle(Point(13,15),0.25)
    die3_dot3 = Circle(Point(14,14),0.25)

    die4_dot1 = Circle(Point(17,16),0.25)
    die4_dot2 = Circle(Point(19,16),0.25)
    die4_dot3 = Circle(Point(17,14),0.25)
    die4_dot4 = Circle(Point(19,14),0.25)

    die5_dot1 = Circle(Point(22,16),0.25)
    die5_dot2 = Circle(Point(24,16),0.25)
    die5_dot3 = Circle(Point(23,15),0.25)
    die5_dot4 = Circle(Point(22,14),0.25)
    die5_dot5 = Circle(Point(24,14),0.25)
    
    die1.setFill('white')
    die1_dot1.setFill('black')
    
    die2_dot1.setFill('black')
    die2_dot2.setFill('black')

    die3_dot1.setFill('black')
    die3_dot2.setFill('black')
    die3_dot3.setFill('black')

    die4_dot1.setFill('black')
    die4_dot2.setFill('black')
    die4_dot3.setFill('black')
    die4_dot4.setFill('black')

    die5_dot1.setFill('black')
    die5_dot2.setFill('black')
    die5_dot3.setFill('black')
    die5_dot4.setFill('black')
    die5_dot5.setFill('black')

    die1.draw(win)
    die2.draw(win)
    die3.draw(win)
    die4.draw(win)
    die5.draw(win)

    die1_dot1.draw(win)
    die2_dot1.draw(win)
    die2_dot2.draw(win)
    die3_dot1.draw(win)
    die3_dot2.draw(win)
    die3_dot3.draw(win)
    die4_dot1.draw(win)
    die4_dot2.draw(win)
    die4_dot3.draw(win)
    die4_dot4.draw(win)
    die5_dot1.draw(win)
    die5_dot2.draw(win)
    die5_dot3.draw(win)
    die5_dot4.draw(win)
    die5_dot5.draw(win)

main()

