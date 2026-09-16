#QUESTION:Given an integer array arr[] of size n, where each element lies in the range [0, n-1], transform the array such that every element at index i becomes:
arr=list(map(int,input().split()))
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    arr[i]=arr[i]+(arr[arr[i]]%n)*n
for i in range(n):
    arr[i]=arr[i]//n
print(*arr)