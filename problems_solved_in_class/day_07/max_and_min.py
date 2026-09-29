n = int(input())

arr = list(map(int, input().split()))

maximum = arr[0]
minimum = arr[0]

for num in arr:

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

    running_range = maximum - minimum

    print(running_range, end=" ")