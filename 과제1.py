import random                       # random 사용


d=0                                 # d선언

for x in range(10):                 # 10문제를 위한 반복문 선언
    a=random.randint(1,30)          # 1~30숫자 중 랜덤하게 선택하여 a에 대입
    b=random.randint(1,30)          # 1~30숫자 중 랜덤하게 선택하여 b에 대입

    print(a,"+",b,"=")              # a,b 화면에 출력
    x=input()                       # x로 값 받음
    c=int(x)                        # 문자값x를 정수형으로 변환

    if a+b==c:                      # 정답일 경우 "정답" 출력
        print("정답")
        d=d+1                       # if문으로 들어오면 +1씩 카운트
    else:                           # 오답일 경우 "오답" 출력
        print("오답")
        
print("당신의 점수는 :",d*10,"점")  # 카운트 된 d값에 10을 곱하여 점수 출력
    
