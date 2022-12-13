
from turtle import Turtle
# POSITIONS=[(-350,0),(-350,20),(-350,-20)]
# full_paddle=[]


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)






       # paddle.setheading(90)

    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)





