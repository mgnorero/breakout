from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard
import random
from brick import Brick

screen = Screen()
score = ScoreBoard()
ball = Ball()
brick = Brick()
paddle = Paddle(-260)

screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")


brick.create_bricks()


game_on = True

while game_on is True:

    ball.move_ball()
    time.sleep(0.09)
    screen.update()

    screen.listen()
    screen.onkeypress(paddle.move_right, "Right")
    screen.onkeypress(paddle.move_left, "Left")

    colors = ["red", "yellow", "blue"]
    ball_color = random.choice(colors)

    if ball.ycor() > 260:
        ball.color(ball_color)
        ball.bounce_up_down()

    if ball.ycor() == -240 and ball.distance(paddle) < 80:
        ball.color(ball_color)
        ball.bounce_up_down()

    if ball.xcor() > 360:
        ball.color(ball_color)
        ball.bounce_sides()

    if ball.xcor() < -360:
        ball.color(ball_color)
        ball.bounce_sides()

    if ball.ycor() < -240 and ball.distance(paddle) > 80:
        ball.reset_position()
        score.dead()

    for item in brick.segments:
        index = brick.segments.index(item)

        if ball.distance(item) <= 50:
            ball.bounce_up_down()
            del brick.segments[index]
            item.hideturtle()
            score.point()

    if score.lives == 0:
        game_over = Turtle()
        game_over.hideturtle()
        game_over.color("yellow")
        game_over.write(arg=f"        GAME OVER             ", align="center",font=("Courier", 50, "bold"))
        game_on = False
        screen.listen()
        new_game = screen.textinput(title="NEW GAME", prompt="To play again write YES").lower()
        if new_game == "yes":
            game_on = True
            game_over.reset()
            score.reset_score()
            brick.reset_bricks()
            count_back = Turtle()
            count_back.color("yellow")
            count_back.hideturtle()
            count_back.write(arg="3", align="center", font=("Courier", 50, "bold"))
            time.sleep(1)
            count_back.clear()
            count_back.write(arg="2", align="center", font=("Courier", 50, "bold"))
            time.sleep(1)
            count_back.clear()
            count_back.write(arg="1", align="center", font=("Courier", 50, "bold"))
            time.sleep(1)
            count_back.reset()








screen.exitonclick()