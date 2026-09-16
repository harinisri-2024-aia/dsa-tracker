#QUESTION:Right Rotation (Clockwise) - n times.Consider index only from 0 to n-1
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

k = k % n

arr = arr[n-k:] + arr[:n-k]

print(*arr)