from turtle import Screen
from paddle import  Paddle
from ball import  Ball
from score import Score
import time

screen=Screen()
screen.screensize(canvwidth=800,canvheight=600)
screen.bgcolor("black")
screen.title("Paddle Game")
screen.tracer(0)
r_paddle=Paddle((340,0))
l_paddle=Paddle((-340,0))
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
ball=Ball()
score=Score()


game_is_on=True
while game_is_on:
    screen.update()
    current_sleep=0.1
    time.sleep(current_sleep)
    current_sleep/=10
    #screen.tracer(1)
    ball.move()
    #detect collision with wall
    if ball.ycor()>280  or ball.ycor()<-280 :
        ball.y_bounce()

    #detect collision with paddle
    if ball.distance(r_paddle)<50 or ball.xcor()>340 and ball.distance(l_paddle)<50 or ball.xcor()<-340:
        ball.x_bounce()

    #detection with ball miss right paddle
    if ball.xcor()>370 :
        ball.reset_position()
        score.update_l_ponit()



    elif ball.xcor()<-370:
        ball.reset_position()
        score.update_r_ponit()

screen.exitonclick()