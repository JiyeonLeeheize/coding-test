
#A,B,C 줄 단위로 입력 받기

A = int(input())
B = int(input())
C = int(input())
    
result = A * B * C
#str을 통한 문자열 변환
result = str(result)

#count함수

for i in range(10):
    print(result.count(str(i))) #문자 i가 result에 몇 회 존재?
