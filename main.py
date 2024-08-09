from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('My Snake Game')

"""1. Creating the snake body: """
# Initializing an object from Snake class, triggering the create snake method:
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# Update the screen after making the snake:
screen.update()


# Setting up key listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


"""2. Moving the snake: """
game_is_on = True
while game_is_on:
    # Take a 0.1 seconds rest:
    sleep(.1)
    # Update the screen only after the segments are fully moved:
    screen.update()
    # Calling the move method from Snake class:
    snake.move()
    # Detecting collision with food:
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 295 or snake.head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detecting collision with tail:
    for segment in snake.snake_body:
        if snake.head.distance(segment) < 10 and segment != snake.head:
            scoreboard.reset_scoreboard()
            snake.reset_snake()


screen.exitonclick()

