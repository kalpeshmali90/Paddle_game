from  turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_point = 0
        self.r_point = 0
        self.update_score()
    
        
    def update_score(self):
        self.clear()


        self.goto(-120, 250)
        self.write(self.l_point, align="center", font=("Courier", 45, "normal"))
        self.goto(120, 250)
        self.write(self.r_point, align="center", font=("Courier", 45, "normal"))
        
    
    def update_l_ponit(self):
        self.l_point+=1
        self.update_score()
    

    def update_r_ponit(self):
        self.r_point+=1
        self.update_score()
