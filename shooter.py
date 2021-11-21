import turtle
import math
import random

#setup screen
win=turtle.Screen()
win.bgcolor("black")
##background picture
#win.bgpic("background.gif")
win.tracer(5)



#create boder
boder=turtle.Turtle()
boder.color("green")
boder.penup()
boder.setposition(-300,-300)
boder.pendown()
boder.pensize(3)
for side in range(4):
    boder.forward(600)
    boder.left(90)
boder.hideturtle()



#Create player turtle
player=turtle.Turtle()
player.color("Green")
player.shape("triangle")
player.penup()
player.speed(0)
#set speed
speed=1

#create multiple targets
maxtargets=10
targets=[]
for count in range(maxtargets):
    targets.append(turtle.Turtle())
    targets[count].color("Blue")
    targets[count].shape("circle")
    targets[count].penup()
    targets[count].speed(0)
    targets[count].setposition(random.randint(-300,300), random.randint(-300,300))



#functions
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increasespeed():
    global speed
    speed+=1
def decreasespeed():
    global speed
    speed-=1
def isCollision(t1,t2):
    dis=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2))+math.pow(t1.ycor()-t2.ycor(),2)
    if dis<20:
        return True
    else:
        return False

    
#keyboard bindings
turtle.listen()##event Listening##
turtle.onkey(turnleft,"a")
turtle.onkey(turnright,"d")
turtle.onkey(increasespeed,"w")
turtle.onkey(decreasespeed,"s")


while True:
    player.forward(speed)

    #boundry check
    if player.xcor()>300 or player.xcor()<-300:
        player.right(100)
    if player.ycor()>300 or player.ycor()<-300:
        player.right(100)

    

    #moving Target
    for count in range(maxtargets):
        targets[count].forward(3)
    #target boundry check
        if targets[count].xcor()>300 or targets[count].xcor()<-300:
            targets[count].right(100)
        if targets[count].ycor()>300 or targets[count].ycor()<-300:
            targets[count].right(100)
        #collision check
        if isCollision(player,targets[count]):
            targets[count].setposition(random.randint(-300,300), random.randint(-300,300))
            targets[count].right(random.randint(0,360))
        

delay=raw_input("press enter to end")
