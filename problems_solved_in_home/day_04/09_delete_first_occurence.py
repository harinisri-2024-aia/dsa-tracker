n=int(input())
arr=list(map(int,input().split()))
ele=int(input())
for i in range(n):
    if arr[i]==ele:
        for j in range(i,n-1):
            arr[j]=arr[j+1]
        arr.pop()
        break
print(*arr)