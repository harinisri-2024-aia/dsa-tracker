n, c = map(int, input().split())

arr = list(map(int, input().split()))

count = 0

for i in range(n):
    if arr[i] >= c:
        count += 1

print(count)