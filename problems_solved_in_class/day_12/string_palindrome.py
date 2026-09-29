str=input()
left=0
right=len(str)-1
while left<right:
    if str[left]!=str[right]:
        print("Not Palindrome")
        break
    left+=1
    right-=1
else:
    print("Palindrome")