from turtle import Turtle

LEVEL_ONE_POSITIONS = [(-360, 50), (-260, 50), (-160, 50), (-60, 50), (40, 50), (140, 50), (240, 50), (340, 50),
                       (-300, 100), (-200, 100), (-100, 100), (0, 100), (100, 100), (200, 100), (300, 100), (400, 100),
                       (-360, 150), (-260, 150), (-160, 150), (-60, 150), (40, 150), (140, 150), (240, 150),
                       (340, 150)]


class Brick(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=4)
        self.hideturtle()

    def create_bricks(self):
        for position in LEVEL_ONE_POSITIONS:
            brick = Brick()
            brick.speed("fastest")
            brick.goto(position)
            self.segments.append(brick)
            brick.showturtle()

    def reset_bricks(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_bricks()

