import turtle
import time
import datetime as dt

# basics of turtle for getting screen
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=740, height=740)
s.title("Clock")
s.tracer(0)
t.ht()

sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour


def clock(h_h, m_h, s_h, t):
    # Clock's base
    t.up()
    t.goto(0, 260)
    t.setheading(180)
    t.color("Blue")
    t.pd()
    t.circle(260)

    # Hour hands
    t.up()
    t.goto(0, 0)
    t.setheading(90)
    c = 13
    t.color("lime")

    # Drawing numbers on clock
    for i in range(12):
        t.pensize(4)
        c -= 1
        t.fd(220)
        t.pd()
        t.write(str(c), font="Georgia")
        t.pu()
        t.fd(15)
        t.pd()
        t.fd(20)
        t.pu()
        t.goto(0, 0)
        t.rt(-30)

    hands = [("white", 80, 12), ("red", 150, 60), ("yellow", 110, 60)]   # tuple contains (color, length, divisor for angle) of hands
    time_set = (h_h, m_h, s_h)

    # equalising real time and clock's time
    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part / hand[2]) * 360
        t.pensize(3)
        t.pu()
        t.goto(0, 0)
        t.color(hand[0])
        t.setheading(90)
        t.rt(angle)
        t.pd()
        t.fd(hand[1])


char = True


while char:  # for continuous view of clock
    h_h, m_h, s_h = int(time.strftime("%I")), int(time.strftime("%M")), int(time.strftime("%S"))

    clock(h_h, m_h, s_h, t)
    print(str(h_h).zfill(2) + ":" + str(m_h).zfill(2) + ":" + str(s_h).zfill(2))
    # for digital clock
    t.pu()
    t.goto(-110, 296)
    t.pendown()
    t.color("orange")
    t.write(str(h_h).zfill(2) + ":" + str(m_h).zfill(2) + ":" + str(s_h).zfill(2), font=("Georgia", 45, "normal"))
    s.update()
    time.sleep(1)
    t.clear()
    # turtle.Screen.exitonclick()
