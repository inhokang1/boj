words = input()
stack = []


for i in words:
    stack.append(i)


    if stack[-4:] == ['P','P','A','P']:
        for j in range(4):
            stack.pop()
        stack.append("P")


if stack == ['P','P','A','P'] or stack == ["P"]:
    print("PPAP")
else:
    print("NP")