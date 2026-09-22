arr = list(map(int, input().split()))
k = int(input())
left = 0
right = k - 1
max_sum = 0
while right < len(arr):
    current_sum = sum(arr[left:right + 1])
    max_sum = max(max_sum, current_sum)
    left += 1
    right += 1
print(max_sum)