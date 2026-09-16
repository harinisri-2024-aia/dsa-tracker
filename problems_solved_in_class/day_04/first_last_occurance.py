arr = [1, 2, 2, 2, 3, 4, 5]
x = 2

left = 0
right = len(arr) - 1

first = -1
last = -1

while left <= right:

    if arr[left] == x and first == -1:
        first = left

    if arr[right] == x and last == -1:
        last = right

    if first != -1 and last != -1:
        break

    left += 1
    right -= 1

print("First occurrence:", first)
print("Last occurrence:", last)