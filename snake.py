from turtle import Turtle


class Snake:
    current_heading = 0
    MOVE_DISTANCE = 20
    segments = []
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    head = None

    def __init__(self):
        for position in self.starting_positions:
            new_segment = Turtle()
            new_segment.color("grey")
            new_segment.shape("square")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.showturtle()
            self.segments.append(new_segment)

        self.head = self.segments[0]
        self.head.color("white")

    def set_move_distance(self, size):
        self.MOVE_DISTANCE = size

    def get_move_distance(self):
        return self.MOVE_DISTANCE

    def get_current_heading(self):
        return self.current_heading

    def move(self):
        self.head.setheading(self.current_heading)
        length = len(self.segments) -1
        for i in range(length, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)

    def move_right(self):
        if self.current_heading != 180:
            self.current_heading = 0
            self.move()

    def move_up(self):
        if self.current_heading != 270:
            self.current_heading = 90
            self.move()

    def move_left(self):
        if self.current_heading != 0:
            self.current_heading = 180
            self.move()

    def move_down(self):
        if self.current_heading != 90:
            self.current_heading = 270
            self.move()

    def grow(self, size):
        for i in range(0, size):
            tail_segment_id = len(self.segments) - 1
            tail_segment = self.segments[tail_segment_id]
            tail_x = tail_segment.xcor()
            tail_y = tail_segment.ycor()
            position = (tail_x, tail_y)
            new_segment = Turtle()
            new_segment.color("grey")
            new_segment.shape("square")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.showturtle()
            self.segments.append(new_segment)

    def get_cords(self):
        x = self.head.xcor()
        y = self.head.ycor()
        vector2d = (x, y)
        return vector2d

    def tail_collision(self):
        for segment in self.segments:
            if self.head.distance(segment) < 0:
                return True
            else:
                return False

    def segment_count(self):
        return len(self.segments)