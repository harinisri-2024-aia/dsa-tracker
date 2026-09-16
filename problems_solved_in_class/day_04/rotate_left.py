arr=list(map(int,input().split()))
n = len(arr)
k = int(input())
k = k % n

arr[:k] = arr[:k][::-1]
arr[k:] = arr[k:][::-1]
arr.reverse()

print(arr)