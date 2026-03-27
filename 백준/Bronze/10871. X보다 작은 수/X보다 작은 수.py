
N,X=map(int,input().split())
arr=list(map(int,input().split())) #N개만큼 알아서 입력됨


for num in arr:
    if num < X:
        print(num,end=" ")
    
