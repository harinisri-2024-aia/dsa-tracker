s=input()
frequency={}
for ch in s:
    frequency[ch]=frequency.get(ch,0)+1

    if frequency[ch]==2:
        print(ch)
        break
else:
    print(-1)
