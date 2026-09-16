arr = [10, 5, 20, 8, 15]

largest = float('-inf')
second_largest = float('-inf')

for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("Largest:", largest)
print("Second largest:", second_largest)