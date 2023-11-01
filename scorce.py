import turtle
import random



segment=[]

grass=turtle.Screen()
grass.bgpic("grass.gif")
grass.addshape("head up.gif")
grass.addshape("head down.gif")
grass.addshape("head left.gif")
grass.addshape("head right.gif")
grass.addshape("body.gif")


snake=turtle.Turtle()
snake.penup()
snake.speed(0)
snake.goto(0,0)
snake.setheading(90)
snake.shape("head up.gif")


food=turtle.Turtle()
food.penup()
food.color("red")
food.shape("circle")
food.speed(50)
food.goto(100,10)

pen=turtle.Turtle()
pen.penup()
pen.speed(50)
pen.hideturtle()
pen.goto(0,250)
pen.write("score : 0",font=("courier",27,"bold"))



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

score=0,



while True:

    grass.update()
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290 :
       grass.bgpic("OVER.gif")
       food.hideturtle()

    for i in segment:
       if i.distance(snake)<1:
          grass.bgpic("OVER.gif")   
          food.hideturtle()
       


    move()
   
    if snake.distance(food) < 4:
      x=random.randint(-285,285)
      y=random.randint(-285,285)
      food.setpos(x,y)
      score=score+1
      pen.clear()
      pen.write("score : {}".format(score),font=("courier",27,"bold"))
     

      body=turtle.Turtle()
      body.penup()
      body.shape("body.gif")
      body.speed(0)
      segment.append(body)
      


    for i in range(len(segment)-1,0,-1):
      x=segment[i-1].xcor()
      y=segment[i-1].ycor()
      segment[i].goto(x,y)

    if len(segment)> 0: 
       x=snake.xcor()
       y=snake.ycor()
       segment[0].goto(x,y)

    move()

        


#turtle.done()