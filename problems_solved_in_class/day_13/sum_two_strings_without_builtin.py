s = input()

if "+" in s:
    i = s.index("+")
    a = s[:i]
    b = s[i+1:]
    print(int(a) + int(b))

elif "-" in s:
    i = s.index("-")
    a = s[:i]
    b = s[i+1:]
    print(int(a) - int(b))

elif "*" in s:
    i = s.index("*")
    a = s[:i]
    b = s[i+1:]
    print(int(a) * int(b))

elif "/" in s:
    i = s.index("/")
    a = s[:i]
    b = s[i+1:]
    print(int(a) / int(b))

else:
    print("Invalid Input")