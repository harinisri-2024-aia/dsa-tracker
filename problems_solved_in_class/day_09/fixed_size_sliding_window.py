# cook your dish here
arr=list(map(int,input().split()))
k=int(input())
left=0
right=k-1
while right<len(arr):
    print(arr[left:right+1])
    left+=1
    right+=1