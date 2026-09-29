s=input()
result=""
for ch in s:
    if not result or ch!=result[-1]:
        result+=ch
print(result)