import turtle

#Function to draw a square using  a given turtle object

def drawSquare(turtle_object):
        for i in range(1,5):
            turtle_object.forward(100)
            turtle_object.right(90)

def drawFlower(someTurtle):
    #Petals, base distance 10 pixels/points idk
    for i in range(1,37):
        drawRhombus(someTurtle)  
        someTurtle.right(10)
    #Flower Steam
    someTurtle.right(90)    
    someTurtle.forward(300)
        
def drawRhombus(someTurtle):
    #The four interior angles in any rhombus must have a sum of 360 degrees
    for i in range(1,3):
        someTurtle.forward(100)
        someTurtle.right(45)
        someTurtle.forward(100)
        someTurtle.right(135)

def drawArt():

    #Create a window, a canvas.
    window = turtle.Screen()
    window.bgcolor('red')

    #Create a turtle object.
    ivan = turtle.Turtle()
    ivan.shape('turtle')
    ivan.color('blue')
    ivan.speed(100)

    drawSquare(ivan)
    drawFlower(ivan)

    window.exitonclick()
        

drawArt()

    
