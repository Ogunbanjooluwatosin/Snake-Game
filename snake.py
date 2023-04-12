from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
Up = 90
Down = 270
Right = 360
Left = 180


class Snake:
    def __init__(self):
        self.snake_list = []
        self.generate_snake()
        self.move_snake()

    def generate_snake(self):
        for position in starting_position:
            self.add_segments(position)

    def add_segments(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("darkgreen")
        snake.penup()
        snake.goto(position)
        self.snake_list.append(snake)

    def extend_snake(self):
        self.add_segments(self.snake_list[-1].position())

    def move_snake(self):
        for snake_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snake_num - 1].xcor()
            new_y = self.snake_list[snake_num - 1].ycor()
            self.snake_list[snake_num].goto(new_x, new_y)
        self.snake_list[0].forward(20)




    def reset(self):
        for seg in self.snake_list:
            seg.speed("fastest")
            seg.goto(x=1000,y=1555)
        self.snake_list.clear()
        self.generate_snake()


    def up(self):
        if self.snake_list[0].heading != Down:
            self.snake_list[0].setheading(Up)

    def down(self):
        if self.snake_list[0].heading != Up:
            self.snake_list[0].setheading(Down)

    def go_right(self):
        if self.snake_list[0].heading != Left:
            self.snake_list[0].setheading(Right)

    def go_left(self):
        if self.snake_list[0].heading != Right:
            self.snake_list[0].setheading(Left)
