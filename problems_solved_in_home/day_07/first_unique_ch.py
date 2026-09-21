s=(list(map(str,input().split())))
frequency={}
for ch in s:
    frequency[ch]=frequency.get(ch,0)+1
for i,ch in enumerate(s):
    if frequency[ch]==1:
        print(i)
        break
else:
    print(-1)