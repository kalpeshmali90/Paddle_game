from turtle import  Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("slow")
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.goto(0,0)
        self.xmove=10
        self.ymove=10


    def move(self):
        #right_screen_bal_xcor=random.randint(20,320)
        new_xcor=self.xcor()+self.xmove
        
        new_ycor=self.ycor()+self.ymove
        self.goto(new_xcor,new_ycor)
    def y_bounce(self):


       self.ymove *= -1
    
    def x_bounce(self):
        self.xmove *=-1
    
    def reset_position(self):
        self.goto(0,0)
        self.x_bounce()
    
    