import turtle as t                      #turtle import
import random as r                      #random import


def right_wall():                       #오른쪽 벽을 맞았을 때 튕기는 각도 조절
    ang=t.heading()                     #ang에 현재 각도 넣기
    if ang<90:                          # 아래서 위로 들어갈때 
        t.lt(180-2*ang)
    else:                               #위에서 아래로 들어갈때
        t.rt(180-2*(360-ang))

def left_wall():                        # 왼쪽 벽을 맞았을 때 튕기는 각도 조절
    ang=t.heading()                     #ang에 현재 각도 넣기
    if ang<180:                         # 아래서 위로 들어갈때
        t.rt(2*(ang-90))
    else:                               # 위에서 알래로 들어갈때
        t.lt(2*(270-ang))

def top_wall():                         # 위쪽벽을 맞알을 때 튕기는 각도 조절
    ang=t.heading()                     # ang에 현재 각도 넣기
    if ang<90:                          # 왼쪽에서 오른쪽으로 들어갈때
        t.rt(2*ang)
    else:                               # 오른쪽에서 왼쪽으로 들어갈때
        t.lt(2*(180-ang))

def bottom_wall():                      # 아래쪽을 맞았을 때 튕기는 각도 조절
    ang=t.heading()                     # ang에 현재 각도 넣기
    if ang<270:                         # 왼쪽에서 오른쪽으로 들어갈때
        t.rt(2*(ang-180))
    else:                               # 오른쪽에서 왼쪽으로 들어갈때
        t.lt(2*(360-ang))

def make_rec(x,y,d):                    # x,y를 왼쪽아래로 두고 사각형 만들기
    t.up()
    t.goto(x,y)
    t.goto(x-d/2,y-d/2)
    t.down()             

    for x in range(4):                  
        t.fd(d)
        t.lt(90)
    t.up()
    t.home()                  
    t.down()
def if_wall(x1,y1,d1):                                          # 장애물 생성
    if b<y1+d1/2 and b>y1+d1/2-5 and a>x1-d1/2 and a<x1+d1/2:   # 장애물의 윗벽을 맞았을 때 튀기는 각도 조절
        bottom_wall()
    if a>x1-d1/2 and a<x1-d1/2+5 and b<y1+d1/2 and b>y1-d1/2:   # 장애물의 왼쪽벽을 맞았을 때 튀기는 각도 조절
        right_wall()
    if b>y1-d1/2 and b<y1-d1/2+5 and a>x1-d1/2 and a<x1+d1/2:   # 장애물의 아래벽을 맞았을 때 튀기는 각도 조절
        top_wall()
    if a<x1+d1/2 and a>x1+d1/2-5 and b<y1+d1/2 and b>y1-d1/2:   # 장애물의 오른쪽벽을 맞았을 때 튀기는 각도 조절
        left_wall()
        

    
    
t.speed(0)                                  # 속도 빠르게                  
t.shape("circle")                           # 공모양으로
t.pensize(5)                                # 벽두껍게

recx_1=80                                   # 장애물 좌표
recy_1=100                                  
recd_1=80

recx_2=-100                                 # 장애물좌표
recy_2=150
recd_2=50

recx_3=100                                  # 장애물좌표
recy_3=-100
recd_3=100

recx_4=30                                   # 장애물좌표
recy_4=0
recd_4=60

recx_5=-70                                  # 장애물좌표
recy_5=-35
recd_5=90

make_rec(0,0,500)                           # 벽 생성
make_rec(recx_1,recy_1,recd_1)              # 장애물 생성
make_rec(recx_2,recy_2,recd_2)              # 장애물 생성
make_rec(recx_3,recy_3,recd_3)              # 장애물 생성
make_rec(recx_4,recy_4,recd_4)              # 장애물 생성
make_rec(recx_5,recy_5,recd_5)              # 장애물 생성

t.lt(r.randint(1,360))                      # 시작 할 때 각도 랜덤하게 설정하기

x=0                                         # 여기 숫자를 바꿈으로써 사각벽의 크기가 변해도 적용이 가능
y=0                                         # 여기 숫자를 바꿈으로써 사각벽의 크기가 변해도 적용이 가능
d=500                                       # 여기 숫자를 바꿈으로써 사각벽의 크기가 변해도 적용이 가능
n=0
t.speed(0)
t.up()                  

while True:                                 # 무한으로 돌리기
    ang=t.heading()
    t.fd(5)                                 # 앞으로 5씩 이동
    a=t.xcor()                              # 이동할 때마다 x좌표 a에 저장
    b=t.ycor()                              # 이동할 때마다 y좌표 b에 저장
    if b>=y+d/2:                            # 윗벽을 맞는 다면 top_wall()함수
        top_wall()
    if a<=-(x+d/2):                         # 왼쪽벽을 맞는다면 left_wall()함수                       
        left_wall()
    if b<=-(y+d/2):                         # 아래벽을 맞는다면 bottom_wall()함수
        bottom_wall()
    if a>=x+d/2:                            # 오른쪽 벽을 맞는다면 right_wall()함수
        right_wall()
    if_wall(recx_1,recy_1,recd_1)           # 1번장애물 맞았을 때 if_wall()함수
    if_wall(recx_2,recy_2,recd_2)           # 2번장애물 맞았을 때 if_wall()함수
    if_wall(recx_3,recy_3,recd_3)           # 3번장애물 맞았을 때 if_wall()함수
    if_wall(recx_4,recy_4,recd_4)           # 4번장애물 맞았을 때 if_wall()함수
    if_wall(recx_5,recy_5,recd_5)           # 5번장애물 맞았을 때 if_wall()함수

        



        
    

