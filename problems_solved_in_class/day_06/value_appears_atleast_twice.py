arr=list(map(int,input().split()))
frequency={}
for x in arr:
    frequency[x]=frequency.get(x,0)+1
for x in frequency:
    if frequency[x]==2:
        print(x)