sales = list(map(int, input().split()))
n=len(sales)
cumulative = []
current_sum = 0
for i in range(n):
    current_sum += sales[i]
    cumulative.append(current_sum)
print(*cumulative)