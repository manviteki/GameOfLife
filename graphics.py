import Engine
import numpy as np
import turtle
from random import randint


maturtle = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(0,0)
maturtle.hideturtle()
turtle.hideturtle()

l = 7 #Scale factor

def drawSquare(turt): #draws a square
    turt.color('black')
    turt.pensize (l/3)
    turt.fillcolor()
    turt.speed(0)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)

def liveSquare(turt): #draws a black square
    turt.fillcolor('black')
    turt.begin_fill()
    turt.speed(0)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.end_fill()

def inputSquare(turt): #draws a the input squares upon clicking
    turtle.colormode(255)
    turt.fillcolor(240,160,160)
    turt.begin_fill()
    turt.speed(0)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.end_fill()

def deadSquare(turt): #draws a white square
    turt.fillcolor('white')
    turt.begin_fill()
    turt.speed(0)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.forward (2*l)
    turt.right (90)
    turt.end_fill()

def drawGrid(n): #draws a square at the corner of each coordinate. (nxn grid)
    for i in range (n):
        for j in range (n):
            turtle.penup()
            turtle.goto (l*(2*j-n), l*(n-2*i))
            turtle.pendown()
            drawSquare(turtle)
    screen.update()

def drawMatrix(arr,n): #takes a matrix as input and draws a black square wherever there is a '1'
    for i in range (0,n):
        for j in range (0,n):         
            if (arr[i][j] == 1):
                maturtle.penup()
                maturtle.goto (l*(2*j-n), l*(n-2*i))
                maturtle.pendown()
                liveSquare(maturtle)  

    screen.update()