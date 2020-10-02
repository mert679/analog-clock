import time
import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=500, height=400)
wn.title("Analog")
wn.tracer(0)

#create our drawing pen

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
def draw_clock(h,m,s ,pen):
    pen.up()
    pen.goto(0,180)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(180)
#draw lines
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(150)
        pen.pendown()
        pen.fd(30)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    #draw the hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle=(h/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    #draw the minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("blue")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)

    #draw the second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("gold")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    draw_clock(h,m,s,pen)
    wn.update()
    time.sleep(1)
    pen.clear()

wn.mainloop()
