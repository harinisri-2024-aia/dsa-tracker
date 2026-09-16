arr=list(map(int,input().split()))
target=int(input())
count=0
for x in arr:
    if arr[x]==target:
        count+=1
print(count)