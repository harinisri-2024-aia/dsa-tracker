#QUESTION:Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.
n=int(input())
arr=list(map(int,input().split()))
for i in range(n-1):
    if arr[i]<arr[i+1]:
        print("True")
    else:
        print("False")
print(*arr)