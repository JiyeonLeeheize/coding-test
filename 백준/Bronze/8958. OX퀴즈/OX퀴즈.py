#반복으로 입력 받기

T = int(input())

for _ in range(T):
    s=input() #S="OOXOOXOXOOOOX"
    
    counto=0
    total=0

    for ch in s:
         if ch=='O':
            counto+=1
            total+=counto 
            #바로 더해야 뒤에 O or X이든 손실 없음
         else:
            counto=0 
            #리셋만 진행
    
    print(total)
            
"""for each test case:
    입력 받기
    처리하기
    출력하기"""