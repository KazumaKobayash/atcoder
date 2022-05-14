s = input()
if len(s) == 1:
    print("".join([s for _ in range(6)]))
elif len(s) == 2:
    print("".join([s for _ in range(3)]))
else:
    print("".join([s for _ in range(2)]))