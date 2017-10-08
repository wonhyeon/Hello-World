import turtle as t                                  
import random

print("Up & Down게임")                            
print("육각형이 만들어 지기전까지 숫자를 맞혀라!!")
print("범위는 1~50")
n=random.randint(1,50)                              # 1~50까지 랜덤한 숫자 선

for a in range(6):
    x=input("숫자를 입력하시오 :")
    g=int(x)

    if n==g:
        print("정답")
        break
    if n>g:
        print("Up")
    if n<g:
        print("Down")

    t.fd(50)
    t.lt(360/6)

print("정답은 :",n,"이야")

    

