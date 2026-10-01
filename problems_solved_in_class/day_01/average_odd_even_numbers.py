#Average of Odd numbers and Even numbers

#Different levels of difficulties:
#- Input Validation
#- Output round off to 2 decimal places



arr = [1, 2, 3, 4, 5, 6]

odd_sum = 0
odd_count = 0

even_sum = 0
even_count = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even_sum += arr[i]
        even_count += 1
    else:
        odd_sum += arr[i]
        odd_count += 1

print("Average of odd numbers:", odd_sum / odd_count)
print("Average of even numbers:", even_sum / even_count)