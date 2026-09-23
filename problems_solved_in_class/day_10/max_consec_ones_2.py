n=int(input())
nums=list(map(int,input().split()))
left=0
zeroes=0
max_length=0
for right in range(n):
    if nums[right]==0:
        zeroes+=1
        while zeroes>1:
            if nums[left]==0:
                zeroes-=1
            left+=1
            max_length=max(max_length,right-left+1)
print(max_length)