nums=list(map(int,input().split()))
target=int(input())
left=0
window_sum=0
min_length=float('inf')
for right in range(len(nums)):
    window_sum+=nums[right]
    while window_sum>=target:
        min_length=min(min_length,right-left+1)
        window_sum-=nums[left]
        left+=1
    if min_length==float('inf'):
        print(0)
print(min_length)
    