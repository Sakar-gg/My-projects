import turtle
import time
import random

DELAY = 0.1
WIDTH = 600
HEIGHT = 600

score = 0
high_score = 0

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, HEIGHT // 2 - 40)
pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))


def update_scoreboard():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)
    if head.direction == "down":
        head.sety(y - 20)
    if head.direction == "left":
        head.setx(x - 20)
    if head.direction == "right":
        head.setx(x + 20)


def reset_game():
    global score, high_score

    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    if score > high_score:
        high_score = score
    score = 0
    update_scoreboard()


# Keyboard bindings
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Detect wall collision
    if (
        head.xcor() > WIDTH / 2 - 10
        or head.xcor() < -WIDTH / 2 + 10
        or head.ycor() > HEIGHT / 2 - 10
        or head.ycor() < -HEIGHT / 2 + 10
    ):
        reset_game()

    # Detect food collision
    if head.distance(food) < 20:
        x = random.randint(-WIDTH // 2 + 20, WIDTH // 2 - 20)
        y = random.randint(-HEIGHT // 2 + 20, HEIGHT // 2 - 20)
        food.goto(x - x % 20, y - y % 20)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
        update_scoreboard()

    # Move segments from end to front
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Detect self collision
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()
            break

    time.sleep(DELAY)

screen.mainloop()
