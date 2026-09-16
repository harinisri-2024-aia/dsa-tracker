arr=list(map(int,input().split()))
frequency={}
for x in arr:
    frequency[x]=frequency.get(x, 0) + 1
print(frequency)