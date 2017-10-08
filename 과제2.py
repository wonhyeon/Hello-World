import turtle as t                                  
import random

print("Up & Down게임")                            
print("육각형이 만들어 지기전까지 숫자를 맞혀라!!")
print("범위는 1~50")
n=random.randint(1,50)                              # n에 1~50까지 랜덤한 숫자 선택

for a in range(6):                                  # 6번 반복
    x=input("숫자를 입력하시오 :")                  # x에 문자를 받음
    g=int(x)                                        # g에 문자를 정수형으로 변환

    if n==g:                                        # n과g가 같을 경우 정답 출력
        print("정답")
        break                                       # 정답일 경우 for문을 빠져나온다.
    if n>g:                                         # n>g일 경우 Up출력
        print("Up")
    if n<g:                                         # n<g일 경우 Down출력
        print("Down")

    t.fd(50)                                        # 육각형 한 변 출력
    t.lt(360/6)

print("정답은 :",n,"이야")                          # n(정답)출력

    

