from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for each_segment in range(len(self.segments)-1,0,-1):
            new_x = self.segments[each_segment -1].xcor()
            new_y = self.segments[each_segment -1].ycor()
            self.segments[each_segment].goto(new_x,new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if(self.head.heading()!= DOWN):
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for each_segments in self.segments:
            each_segments.goto(10000,10000)

        self.segments.clear()
        self.create()
        self.head = self.segments[0]