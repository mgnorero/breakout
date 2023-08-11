from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 15
        self.y_move = 15

    def move_ball(self):
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        self.goto(newx, newy)

    def bounce_up_down(self):
        self.y_move *= -1

    def bounce_sides(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.color("white")
        self.x_move *= -1




