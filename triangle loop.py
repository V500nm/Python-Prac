import turtle

t = turtle.Turtle()
s= turtle.Screen()

s.bgcolor('black')
t.width(3)
t.speed(20)

col=('white','blue')

for i in range(300):
    t.pencolor(col[i%2])
    t.forward(i*2)
    t.right(134)