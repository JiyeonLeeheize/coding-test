#여러 줄에 하나씩 입력 받기

arr=[]

for _ in range(9): #9번 루프
    num=int(input())
    arr.append(num) #arr에 append
    
    
max_val=arr[0] #max를 arr[0]으로 설정한 후

for n in arr:
    if n > max_val:
        max_val=n #n이 현재max보다 크면, n이 max가 된다.

print(max_val)

#위치 찾기
for i in range(9):
    if arr[i] == max_val:
        print(i+1)
        break