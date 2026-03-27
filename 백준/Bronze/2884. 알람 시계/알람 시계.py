
#첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 
#map,split()를 이용한 입력
#공백으로 숫자 여러 개 들어올 경우

H,M=map(int,input().split())
S=M-45

#중복 if문 사용


if S>=0:
    print(H,S)
else:
    if H==0:
        print(23,60+S)
    else:
        print(H-1,60+S)