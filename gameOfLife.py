from Engine import gol
from graphics import drawMatrix, drawGrid, liveSquare, inputSquare
import numpy as np
import turtle 
from random import randint

c = int(input("Press 1 for user input or 0 for random input: "))
t = turtle.Turtle() 
t.hideturtle()
screen = turtle.Screen()
screen.title("John Conway's Game Of Life")

l = 7
n = 50 #Change this to change game of life size.
a = np.zeros ((n,n))

def drawInput(x,y):     
    t.penup()
    cx = int(x-(x+(n*l))%(2*l))
    cy = int(y-(y-(n*l))%(2*l)+2*l)
    j = abs((cx+n*l)//(2*l))
    i = abs((cy-n*l)//(2*l))
    a[i][j] = 1
    if (cx>=-n*l and cx < n*l and cy<=n*l and cy >-n*l):
        t.goto(cx,cy)    
        inputSquare(t)

def createMatrix(n,i): #This function creates the initial input matrix for the gol
    if (i==1):
        x = np.zeros ((n,n))
        for j in range (0,n):
            for i in range (0,n):
                r = randint (0,10)
                if (r>8):
                    x[i][j] = 1
                else:
                    x[i][j] = 0
        return x
    if (i==0):
        w = t.getscreen()
        w.onclick(drawInput)

drawGrid(n)

createMatrix(n,0) #User input option array 'a'
x = createMatrix(n,1) #Randomised option


turtle.listen()
if (c==0):
    turtle.onkey(lambda: gol(x,0,n),"space") #Pass array a for user input and x for random
elif (c==1):
    turtle.onkey(lambda: gol(a,0,n),"space") #Pass array a for user input and x for random
turtle.done()