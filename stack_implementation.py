def push(stack, ele):
    stack.append(ele)
    print(ele,"inserted into stack successfully")
    print(stack)
def pop(stack):
    if len(stack) == 0:
        print("stack is empty")
        return
    print(stack[-1],"deleted successfully")
    stack.pop()
    print(stack)
stack = []
push(stack, 17)
push(stack, 29)
push(stack, 35)
push(stack, 40)
push(stack, 51)

pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)