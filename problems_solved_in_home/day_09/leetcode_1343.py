arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
threshold=int(input())
count=0
left=0
current_sum=0
for right in range(n):
    current_sum+=arr[right]
    if right-left+1>k:
        current_sum-=arr[left]
        left+=1
    if right-left+1==k:
        if current_sum>=k*threshold:
            count+=1
print(count)