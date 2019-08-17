#Improt Turtle 
from turtle import Turtle

#Import random
from random import randint

#Turtle
Rishi = Turtle()
Rishi.color("red")
Rishi.shape("turtle")


Rishi.penup()
Rishi.goto(-160,100)
Rishi.pendown()

Riki = Turtle()
Riki.color("powderblue")
Riki.shape("turtle")
Riki.penup()
Riki.goto(-150,60)
Riki.pendown()

Rishabh = Turtle()
Rishabh.color("Green")
Rishabh.shape("turtle")
Rishabh.penup()
Rishabh.goto(-170,20)
Rishabh.pendown()


for movement in range(100):
    Rishi.forward(randint(1,5))
    Riki.forward(randint(1,5))
    Rishabh.forward(randint(1,5))
    
    
