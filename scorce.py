import turtle

grass=turtle.Screen()
grass.bgpic("grass.gif")
grass.addshape("head up.gif")
grass.addshape("head down.gif")
grass.addshape("head left.gif")
grass.addshape("head right.gif")
grass.addshape("body.gif")


snake=turtle.Turtle()
snake.penup()
snake.goto(0,0)
snake.setheading(90)
snake.shape("head up.gif")


food=turtle.Turtle()
food.penup()
food.color("red")
food.shape("circle")
food.goto(100,10)



def move():
    snake.forward(1)
      


def up():
    if snake.heading() !=270:
        snake.setheading(90)
        snake.shape("head up.gif")
   
def down():
    if snake.heading() !=90:
     snake.setheading(270)
     snake.shape("head down.gif")

def right():
    if snake.heading() !=180: 
     snake.setheading(0)    
    snake.shape("head right.gif")



def left():
    if snake.heading() !=0:
     snake.setheading(180)
     snake.shape("head left.gif")




turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()


while True:
   move()
   


   
turtle.done()