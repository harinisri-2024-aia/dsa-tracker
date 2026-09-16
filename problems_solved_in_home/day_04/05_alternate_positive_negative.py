#QUESTION:Given an unsorted array arr containing both positive and negative numbers. 
#Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.
arr=list(map(int,input().split()))
positive=[]
negative=[]
for x in arr:
    if x>=0:
        positive.append(x)
    else:
        negative.append(x)
    result=[]
    i=0
    j=0
    while i<len(positive) and j<len(negative):
        result.append(positive[i])
        result.append(negative[j])
        i+=1
        j+=1
    while i<len(positive):
        result.append(positive[i])
        i+=1
    while j<len(negative):
        result.append(negative[j])
        j+=1
print(*result)