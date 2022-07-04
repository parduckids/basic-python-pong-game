from turtle import Turtle

#  Creating a line
class Line(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.color("white")
        self.right(270)
        self.penup()
        self.pensize(3)
        self.goto(0, 300)

    def draw_line(self):
        for _ in range(60):
            self.pendown()
            self.backward(10)
            self.penup()
            self.backward(10)
