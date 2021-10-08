import turtle             
colors = [ "red","yellow","green","blue","purple"]
turtle.speed(50)
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 5])
   my_pen.width(x/100 + 1)
   my_pen.forward(x + 2)
   my_pen.left(185)
   
turtle.done()