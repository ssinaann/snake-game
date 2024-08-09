from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def add_segment(self, position):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    """Attach a segment to the end of the snake's body: """
    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            # Make the last one go to second last position and so on:
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            # Last segment should go to second last's position:
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # To prevent the snake from turning on itself:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset_snake(self):
        # Make the old snake go offscreen:
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]



