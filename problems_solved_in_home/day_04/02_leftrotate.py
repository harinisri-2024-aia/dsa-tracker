#QUESTION:Rotate the Array by left n times using Reverse Algorithm
n=int(input())
arr=list(map(int, input().split()))
k=int(input())
arr[:k]=arr[:k][::-1]
arr[k:]=arr[k:][::-1]
arr.reverse()
print(*arr)