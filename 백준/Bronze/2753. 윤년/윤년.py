
year=int(input())
#백준 입력 검증 필요X

#4의 배수 year%4==0
#100의 배수가 아님 year%100!=0
#400의 배수가 아님 year%400==0

if (year%4==0 and year%100!=0) or (year%400==0):
    print(1)
else:
    print(0)
    
#and or식 기본으로 괄호 x,그러나 같이 쓸 때는 괄호로 구분