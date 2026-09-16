#QUESTION:Given an array of non-negative integers.
# Your task is to rearrange the array elements alternatively i.e. first element should be the max value, the second should be the min value, the third should be the second max, the fourth should be the second min, and so on.
arr=list(map(int,input().split()))
arr.sort()

n = len(arr)

result = []

left = 0
right = n - 1

while left <= right:
    result.append(arr[right])
    right -= 1

    if left <= right:
        result.append(arr[left])
        left += 1
for i in range(n):
    arr[i] = result[i]
print(*result)