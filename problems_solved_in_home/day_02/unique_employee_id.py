n = int(input())
arr = list(map(int, input().split()))

unique = 0

for num in arr:
    unique = unique ^ num

print(unique)