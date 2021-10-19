import numpy as np
from graphics import *

def neighbourCount(arr,i,j,n): #This function counts the number of alive cells around a cell. It takes an array, and two indexes (i,j) as arguments. The cell would be arr[i][j]
    count = 0 #Variable 'count' increases by 1 everytime an alive cell is detected.
    if (arr[i][j] == 1):
        count -= 1
    if (i==0):
        if (j==0): #TopLeft Corner
            for p in range (i, i+2):
                for q in range (j, j+2):
                    if (arr[p][q]) == 1:
                        count += 1  
            return (count)

        elif (j==n-1): #TopRight Corner
            for p in range (i, i+2):
                for q in range (j-1, j+1):
                    if (arr[p][q]) == 1:
                        count += 1                        
            return (count)

        else: #Top Edge
            for p in range (i, i+2):
                for q in range (j-1, j+2):
                    if (arr[p][q]) == 1:
                        count += 1                         
            return (count)

    elif (i==n-1):
        if (j==0): #BottomLeft Corner
            for p in range (i-1, i+1):
                for q in range (j, j+2):
                    if (arr[p][q]) == 1:
                        count += 1                        
            return (count)                        
        elif (j==n-1): #BottomRight Corner
            for p in range (i-1, i+1):
                for q in range (j-1, j+1):
                    if (arr[p][q]) == 1:
                        count += 1                          
            return (count)                        
        else: #Bottom Corner
            for p in range (i-1, i+1):
                for q in range (j-1, j+2):
                    if (arr[p][q]) == 1:
                        count += 1                        
            return (count)                          

    elif (j==0 and (i!=0 or i!=n-1)): #Left Edge
            for p in range (i-1, i+2):
                for q in range (j, j+2):
                    if (arr[p][q]) == 1:
                        count += 1                           
            return (count)                         

    elif (j==n-1 and (i != 0 or i != n-1)): #Right Edge
            for p in range (i-1, i+2):
                for q in range (j-1, j+1):
                    if (arr[p][q]) == 1:
                        count += 1                         
            return (count)                                

    else:
        for p in range (i-1, i+2): #Centre Square
            for q in range (j-1, j+2):
                if (arr[p][q]) == 1:
                    count += 1                     
        return (count)            
def gol (arr,halter,n): #function 'gol' takes the initial 2d matrix and a halter variable as input. Halter halts the game after a given number of runs.x
    drawMatrix(arr,n) #Draws the new matrix at each iteration
    halter += 1
    flag = 0
    b = np.zeros((n,n))
    for j in range (0,n):
        for i in range (0,n):
            b[i][j] = 0
    for i in range (0,n):
        for j in range (0,n):
                counter = neighbourCount (arr,i,j,n)         
                if (counter == 2):
                    b[i][j] = arr[i][j]
                elif (counter == 3):
                    b[i][j] = 1
                    if (arr[i][j] == 0):
                        flag = 1
                else:
                    b[i][j] = 0
                    if (arr[i][j] == 1):
                        flag = 1
    maturtle.clear() #Clears the grid 
    if (flag == 0): #If flag is 0, then the matrix stays the same. 
        return (b)      
    if (halter == 10000): #game runs 10000 times.
        return (b)
    return (gol (b,halter,n)) #Recursive. The updated array goes back to gol as an input.
