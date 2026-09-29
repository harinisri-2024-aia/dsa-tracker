arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
left=0
result=[]
freq={}
for right in range(n):
    freq[arr[right]]=freq.get(arr[right],0)+1
    if right-left+1>k:
        freq[arr[left]]-=1
        if freq[arr[left]]==0:
            del freq[arr[left]]
        left+=1
    if right-left+1==k:
        result.append(len(freq))
print(result)