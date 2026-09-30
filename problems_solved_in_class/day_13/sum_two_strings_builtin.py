s = input()

if "+" in s:
    a, b = s.split("+")
    print(int(a) + int(b))

elif "-" in s:
    a, b = s.split("-")
    print(int(a) - int(b))

elif "*" in s:
    a, b = s.split("*")
    print(int(a) * int(b))

elif "/" in s:
    a, b = s.split("/")
    print(int(a) / int(b))

else:
    print("Invalid Input")