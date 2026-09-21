nums = [2, 7, 13, 14, 9, 21]
target = 20

arr = []

for i, num in enumerate(nums):
    arr.append((num, i))

arr.sort()

left = 0
right = len(arr) - 1

while left < right:
    total = arr[left][0] + arr[right][0]

    if total == target:
        print([arr[left][1], arr[right][1]])
        break

    elif total < target:
        left += 1

    else:
        right -= 1