from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

WIDTH = 900
HEIGHT = 600
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
game_running = True

player = Snake()
snack = Food()
score_board = Score()


def up():
    player.move_up()


def down():
    player.move_down()


def left():
    player.move_left()


def right():
    player.move_right()



screen.listen()
screen.onkeypress(up, 'Up')
screen.onkeypress(up, 'w')
screen.onkeypress(down, 'Down')
screen.onkeypress(down, 's')
screen.onkeypress(left, 'Left')
screen.onkeypress(left, 'a')
screen.onkeypress(right, 'Right')
screen.onkeypress(right, 'd')
counter = 0


def wall_collision():
    player_x = player.head.xcor()
    player_y = player.head.ycor()

    window_width = screen.window_width()
    window_height = screen.window_height()
    window_max_right = (window_width / 2) - 10
    window_max_left = ((window_width / 2 ) - 10) * -1
    window_max_top = (window_height / 2) - 10
    window_max_bottom = ((window_height / 2) - 10) * -1


    if player_x < window_max_left or player_x > window_max_right:
        return True
    if player_y < window_max_bottom or player_y > window_max_top:
        return True

    # Player is within bounds of screen
    return False


def tail_collision():
    for segment in player.segments[1:len(player.segments)]:
        if segment == player.head:
            continue
        if segment.distance(player.head) < 10:
            return True
    return False


def end_game():
    global game_running
    game_running = False
    score_board.game_over()

# Game Loop
while game_running:
    player.move()
    score_board.display_score()
    screen.update()
    time.sleep(0.2)
    if player.head.distance(snack) < 15:
        player.grow(1)
        snack.random_move()
        score_board.increment()
    # Check for wall collision
    if wall_collision():
        end_game()
    # Check all segments in tail for collision with head
    if tail_collision():
        end_game()


screen.exitonclick()