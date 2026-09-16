#QUESTION:Given an array arr[] with indices ranging from 0 to arr.size() - 1, rearrange the elements so that the value at each index i becomes i. If the value i is not present in the array, place -1 at index i.
n=int(input())
arr=list(map(int,input().split()))
result=[-1]*n
for num in arr:
    if num!=-1:
        result[num]=num 
print(*result)