import turtle, math, random
# Space Invaders Game Project

# Score Settings
score = 0
score_screen = turtle.Turtle()
score_screen.speed(0)
score_screen.color("white")
score_screen.penup()
score_screen.setpos(-310, 300)
score_display = "Score:" + str(score)
score_screen.write(score_display, False, align="left", font = ("Arial", 14, "normal"))
score_screen.hideturtle()

# Screen Settings
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("SPACE INVADERS")
screen.setup(950, 695, 190, 0)
screen.bgpic("space_invaders_background.gif")
screen.tracer(0)

# Enemy Amount
enemy_amount = 36
enemy_list = []

for enemy in range(enemy_amount):
    enemy_list.append(turtle.Turtle())

turtle.register_shape("invader.gif")

enemy_start_x = -285
enemy_start_y = 250
enemy_number = 0

#  Enemy Setup
for enemy in enemy_list:
    enemy.color("#00FF00")
    enemy.penup()
    enemy.shape("invader.gif")
    enemy.speed(0)
    enemy.setpos(enemy_start_x + (50 * enemy_number), enemy_start_y)
    enemy_number += 1
    if enemy_number == 12:
        enemy_start_y -= 50
        enemy_number = 0

enemy_speed = .05

turtle.register_shape("ship.gif")

# Player Setup
player = turtle.Turtle()
player.shape("ship.gif")
player.speed(2)
player.penup()
player.color("green")
player.left(90)
player.setpos(0, -250)
player.shapesize(3)

player_movement = 100

turtle.register_shape("missile.gif")
# Player Bullet Setup
bullet = turtle.Turtle()
bullet.penup()
bullet.shape("missile.gif")
bullet.speed(0)
bullet.shapesize(.5)
bullet.setpos(0, -500)
bullet.hideturtle()

bullet_speed = 2

# Player Movement Functions
def move_right():
    x = player.xcor()
    x += player_movement
    if x > 290:
        player.setx(290)
    else:
        player.setx(x)


def move_left():
    x = player.xcor()
    x -= player_movement
    if x < -290:
        player.setx(-290)
    else:
        player.setx(x)

# Shooting Bullet
def shoot_bullet():
    if not bullet.isvisible():
        bullet.setpos(player.xcor(), player.ycor()+10)
        bullet.showturtle()


# KeyBoard Bindings
turtle.onkey(move_right, "Right")
turtle.onkey(move_left, "Left")
turtle.onkey(shoot_bullet, "space")


turtle.listen()

# Main Game Loop
while True:
    screen.update()
    for enemy in enemy_list:
        x = enemy.xcor()
        x -= enemy_speed
        enemy.setx(x)

        # Checks Enemy Boundaries
        # Original: -600
        if enemy.xcor() < -290:
            for e in enemy_list:
                y = e.ycor()
                y -= 25
                e.sety(y)
            enemy_speed *= -1
        # Original: 600
        if enemy.xcor() > 290:
            for e in enemy_list:
                y = e.ycor()
                y -= 25
                e.sety(y)
            enemy_speed *= -1

        # Checks Collision
        if bullet.distance(enemy) < 45:
            # Score Updating
            score += 10
            score_display = "Score:" + str(score)
            score_screen.clear()
            score_screen.write(score_display, False, align="left", font=("Arial", 14, "normal"))

            # Resets enemy and bullet after collision
            bullet.hideturtle()
            bullet.setpos(0, -500)
            enemy.setpos(0, -600)


        if player.distance(enemy) < 40:
            player.hideturtle()
            enemy.hideturtle()
            break

    # Checks if bullet is ready to be fired again.
    if bullet.isvisible():
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 290:
        bullet.hideturtle()


