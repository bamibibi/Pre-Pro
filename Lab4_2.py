from Lab3 import ArrayStacks
def copyStack(stack1, stack2):
    copystack = ArrayStacks()
    while True:
        if stack1.is_empty():
            break
        else:
            data = stack1.pop()
            copystack.push(data)
    while True:
        if stack2.is_empty():
            break
        else:
            data = stack2.pop()
    while True:
        if copystack.is_empty():
            break
        else:
            data = copystack.pop()
            stack1.push(data)
            stack2.push(data)
s1 = ArrayStacks()
s1.push(10); s1.push(20); s1.push(30)
s2 = ArrayStacks()
s2.push(15)
copyStack(s1, s2)
s1.printStack()
s2.printStack()