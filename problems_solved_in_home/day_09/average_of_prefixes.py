arr=list(map(int,input().split()))
n=len(arr)
result=[]
total=0
for i in range(n):
    total+=arr[i]
    average=total//(i+1)
    result.append(average)
print(result)