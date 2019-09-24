#Project 4
#This is the Traffic Light project, which displays a vertical rectangular traffic light
#By Arturo Ortiz, arturo.ortiz1@marist.edu
from graphics import *
def main():
    win=GraphWin("Traffic light")
    rectangle=Rectangle(Point(45, 45), Point(112, 150))
    rectangle.setOutline("black")
    rectangle.setFill("white")
    rectangle.draw(win)
#This is the actual traffic rectangle followed by the traffic lights: red, yellow, and green
    redlight=Circle(Point(80, 65), 14)
    redlight.setOutline("black")
    redlight.setFill("red")
    redlight.draw(win)
    
    yellowlight=Circle(Point(80, 95), 14)
    yellowlight.setOutline("black")
    yellowlight.setFill("yellow")
    yellowlight.draw(win)
    
    greenlight=Circle(Point(80, 125), 14)
    greenlight.setOutline("black")
    greenlight.setFill("green")
    greenlight.draw(win)
main()
