from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)
        self.shapesize(5, 1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(y=new_y, x=self.xcor())

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(y=new_y, x=self.xcor())