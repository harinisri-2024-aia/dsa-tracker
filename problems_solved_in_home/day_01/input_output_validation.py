# 1. Basic input and output
n = int(input())
print(n)

# 2. Multiple integers in one line
a, b = map(int, input().split())
print(a + b)

# 3. Array input
arr = list(map(int, input().split()))
print(arr)

# 4. Array input with size validation
n = int(input())
arr = list(map(int, input().split()))

if len(arr) == n:
    print("Valid")
else:
    print("Invalid")

# 5. Output formatting
print(a, b)
print(a, b, sep="-")
print(a, end=" ")
print(f"Sum: {a + b}")
print(*arr)

# 6. Positive, negative or zero validation
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# 7. Array range validation (1 to 100)
if all(1 <= x <= 100 for x in arr):
    print("Valid")
else:
    print("Invalid")

# 8. Safe input type validation
try:
    num = int(input())
    print(num)
except ValueError:
    print("Invalid input")

# 9. Multiple test cases
t = int(input())
for _ in range(t):
    num = int(input())
    print(num * 2)

# 10. Multiple test cases with arrays
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if len(arr) == n and all(1 <= x <= 100 for x in arr):
        print(sum(arr))
    else:
        print("Invalid")