for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2} ".format(j,i,i*j), end='')
    print('')

sum,tmp = 0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print("运行结果是：{}".format(sum))


n=1
for i in range(5,0,-1):
    n = (n+1) << 1
print(n)

diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁'] 
for x in range(0, 5): 
 for y in range(0, 5): 
  if not(x == y): 
    print("{} {}".format(diet[x], diet[y])) 


from turtle import * 
fillcolor("red") 
begin_fill() 
while True: 
    forward(200) 
    right(144) 
    if abs(pos()) < 1: 
       break 
end_fill()



from turtle import * 
color('red', 'yellow') 
begin_fill() 
while True: 
 forward(200) 
 left(170) 
 if abs(pos()) < 1: 
  break 
end_fill() 
done()


import turtle 
import time 
turtle.speed("fastest") 
turtle.pensize(2) 
for x in range(100): 
    turtle.forward(2*x) 
    turtle.left(90) 
time.sleep(3)


import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red", "yellow",'purple','blue']
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)

