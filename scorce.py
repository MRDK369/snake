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
snake.shape("head up.gif")


food=turtle.Turtle()
food.penup()
food.color("red")
food.shape("circle")
food.goto(100,10)

turtle.done()