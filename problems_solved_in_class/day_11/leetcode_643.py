nums=list(map(int,input().split()))
k=int(input())
current_sum=sum(nums[:k])
max_sum=current_sum
for right in range(k,len(nums)):
    current_sum+=nums[right]-nums[right-k]
    max_sum=max(max_sum,current_sum)
print(max_sum/k)