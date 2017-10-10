import turtle as t                                           #turtle 소환
import random                                                #random 소환
import time                                                  # time 소환
t.speed(1)                                                   # turtle 속도 1
ct=30                                                        # 방향전환을 위한 count
ct2=0                                                        # 게임 끝내기 위한 count
sec=2.5                                                      # 초수 설정
print(sec,"초안에 정답을 맞혀야한다. 사각형이 만들어지면 탈락") # 게임 설명
enter=input("enter를 누르면 시작")                           # enter 누르면 시작
for x in range(30):                                          # 더하기 30번 돌리기
    a=random.randint(1,50)                                   # a에 랜덤 숫자
    b=random.randint(1,50)                                   # b에 랜덤 숫자
    c=a+b                                                    # 정답은 c
    
    print(a,"+",b,"=")                                       # a+b= 출력
    start=time.time()                                        # 현재시간 저장
    
    x=input()                                                # 값 받기
    d=int(x)                                                 # 값을 정수형으로 변환
    end=time.time()                                          # 정답적은 시간 저장

    et=end-start                                             # 계산시간 저장
    
    if et>sec:                                                 # 계산시간 3초지나면 전진
        t.fd(20)
        print("Time out")                                    # Time out 출력
        ct=ct+1                                              # 방향전환을 위한 count
    if c==d and et<sec:                                        # 정답일 경우 뒷걸음
        t.back(20)  
        print("정답")                                        # 정답 출력
        ct=ct-1                                              # 정사각형을 위한 -count
    else:                                                    # 오답일 경우 전진
        t.fd(20)
        print("오답")
        ct=ct+1                                              # 방향전환을 위한 count
    if ct==33:                                               # 60전진이면 방향 전환
        t.left(90)                                           # 왼쪽으로 90도
        ct=30                                                # count초기화
        ct2=ct2+1                                            # 게임을 끝내기 위한 count
    if ct2==4:                                               # 사각형이 완성 되면 탈락 출력
        print("탈락")
        break                                                # for문을 빠져나감

enter=input("아쉽네요")                                      # 아쉽네요 출력
        
        
