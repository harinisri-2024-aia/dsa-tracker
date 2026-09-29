arr=list(map(int,input().split()))
min=arr[0]
for num in arr:
    if num<min:
        min=num
    print(min,end=" ")