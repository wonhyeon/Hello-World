import turtle as t
import random as r
print(5/5-1)
print(5+5/5)

def right_wall():
    ang=t.heading()
    if ang<90:
        t.lt(180-2*ang)
    else:
        t.rt(180-2*(360-ang))

def left_wall():
    ang=t.heading()
    if ang<180:
        t.rt(2*(ang-90))
    else:
        t.lt(2*(270-ang))

def top_wall():
    ang=t.heading()
    if ang<90:
        t.rt(2*ang)
    else:
        t.lt(2*(180-ang))

def bottom_wall():
    ang=t.heading()
    if ang<270:
        t.rt(2*(ang-180))
    else:
        t.lt(2*(360-ang))

def make_rec(x,y,d):
    t.up()
    t.goto(x,y)
    t.goto(x-d/2,y-d/2)
    t.down()             

    for x in range(4):       # 사각형 만들기
        t.fd(d)
        t.lt(90)
    t.up()
    t.home()                  # home으로 돌리기
    t.down()
def if_wall(x1,y1,d1):
    if b<y1+d1/2 and b>y1+d1/2-5 and a>x1-d1/2 and a<x1+d1/2:
        bottom_wall()
        print("top")
    if a>x1-d1/2 and a<x1-d1/2+5 and b<y1+d1/2 and b>y1-d1/2:
        right_wall()
        print("left")
    if b>y1-d1/2 and b<y1-d1/2+5 and a>x1-d1/2 and a<x1+d1/2:
        top_wall()
        print("bottom")
    if a<x1+d1/2 and a>x1+d1/2-5 and b<y1+d1/2 and b>y1-d1/2:
        left_wall()
        print("right")


    
t.speed(0)
t.shape("circle")
t.pensize(5)

recx_1=80
recy_1=100
recd_1=80

recx_2=-100
recy_2=150
recd_2=50

recx_3=100
recy_3=-100
recd_3=100

recx_4=30
recy_4=0
recd_4=60

recx_5=-70
recy_5=-35
recd_5=90

make_rec(0,0,500)
make_rec(recx_1,recy_1,recd_1)
make_rec(recx_2,recy_2,recd_2)
make_rec(recx_3,recy_3,recd_3)
make_rec(recx_4,recy_4,recd_4)
make_rec(recx_5,recy_5,recd_5)

t.lt(r.randint(1,360)) 

x=0
y=0
d=500
n=0
t.speed(0)
t.up()
for n in range(100):
    ang=t.heading()
    while True:
        t.fd(5)
        a=t.xcor()
        b=t.ycor()
        if b>=y+d/2:
            top_wall()
            break
        if a<=-(x+d/2):
            left_wall()
            break
        if b<=-(y+d/2):
            bottom_wall()
            break
        if a>=x+d/2:
            right_wall()
            break
        if_wall(recx_1,recy_1,recd_1)
        if_wall(recx_2,recy_2,recd_2)
        if_wall(recx_3,recy_3,recd_3)
        if_wall(recx_4,recy_4,recd_4)
        if_wall(recx_5,recy_5,recd_5)

        



        
    

