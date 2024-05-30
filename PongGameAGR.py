import turtle

wn = turtle.Screen()
wn.title("Pong Game! / Juego del Pong! by @AGranados87")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
ScoreA = 0
ScoreB = 0

#Players
PlayerA = input("Name: ")
PlayerB = input("Name: ")

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(4)
paddleA.shape("square")
paddleA.color("grey")
paddleA.shapesize( stretch_wid=7, stretch_len=1 )
paddleA.penup()
paddleA.goto(-350, 0)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(4)
paddleB.shape("square")
paddleB.color("grey")
paddleB.shapesize(stretch_wid=7, stretch_len=1)
paddleB.penup()
paddleB.goto(+350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"{PlayerA}: 0 {PlayerB}: 0", align="center", font=("Aptos", 20, "normal"))


#Function

def paddleAup():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Keyboard binding

wn.listen()
wn.onkeypress(paddleAup, "w")
wn.onkeypress(paddleADown, "s")
wn.onkeypress(paddleBUp, "Up")
wn.onkeypress(paddleBDown, "Down")


#Main game loop

while True:
    wn.update()

    # Ball movement.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        ScoreA += 1
        pen.clear()
        pen.write(f"{PlayerA}: {ScoreA}  {PlayerB}: {ScoreB}", align="center", font=("Aptos", 20, "normal"))

    if ball.xcor() < - 390:
        ball.goto(0, 0)
        ball.dx *= -1
        ScoreB += 1
        pen.clear()
        pen.write(f"{PlayerA}: {ScoreA}  {PlayerB}: {ScoreB}", align="center", font=("Aptos", 20, "normal"))


    #Paddle physics and ball bouncing

    if ball.xcor() > 340 and (paddleB.ycor() + 50 > ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and (paddleA.ycor() + 50 > ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
