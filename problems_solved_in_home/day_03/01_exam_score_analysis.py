import math

n = int(input())
arr = list(map(int, input().split()))

# 1. Display scores 4 per row
print("Scores:")

for i in range(n):
    print(arr[i], end=" ")

    if (i + 1) % 4 == 0:
        print()

# 2. Average
total = 0

for i in range(n):
    total += arr[i]

average = total / n

# 3. Lowest score
lowest = arr[0]

for i in range(1, n):
    if arr[i] < lowest:
        lowest = arr[i]

# 4. Highest score
highest = arr[0]

for i in range(1, n):
    if arr[i] > highest:
        highest = arr[i]

print(f"Average: {average:.2f}")
print(f"Lowest Score: {lowest}")
print(f"Highest Score: {highest}")

# 5. Deviations
print("Score  Deviation")

for i in range(n):
    deviation = arr[i] - average
    print(f"{arr[i]}     {deviation:.2f}")

# 6. Standard deviation
sum_squared = 0

for i in range(n):
    deviation = arr[i] - average
    sum_squared += deviation * deviation

sd = math.sqrt(sum_squared / n)

print(f"Standard Deviation: {sd:.2f}")

# 7. Count scores within one standard deviation
count = 0

lower = average - sd
upper = average + sd

for i in range(n):
    if lower <= arr[i] <= upper:
        count += 1

print(f"Scores within one standard deviation: {count}")