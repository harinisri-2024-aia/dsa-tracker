n = 5
k = 2
arr = [1, 2, 3, 4, 5]

k = k % n

arr = arr[n-k:] + arr[:n-k]

print(arr)