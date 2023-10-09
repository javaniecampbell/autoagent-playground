# filename: pong_game.py

import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Function to move paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Function to move paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Function to move paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Function to move paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    try:
        win.update()

        # Ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
        elif ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle collision
        if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            ball.color("blue")
            ball.dx *= -1

        elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            ball.color("red")
            ball.dx *= -1

        elif (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 < ball.ycor() < paddle_b.ycor() - 50):
            ball.goto(0, 0)
            ball.dx *= -1

        elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 < ball.ycor() < paddle_a.ycor() - 50):
            ball.goto(0, 0)
            ball.dx *= -1

        # Missed ball paddle A
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dy *= -1

        # Missed ball paddle B
        elif ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dy *= -1

        # Paddle and ball collisions
        if (350 > ball.xcor() > 340) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1

        elif (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

        elif (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
            ball.color("blue")
            ball.dx *= -1

        elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
            ball.color("red")
            ball.dx *= -1

    except turtle.Terminator:
        print("Game Closed")
        break