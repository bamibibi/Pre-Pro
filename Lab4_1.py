from Lab3 import ArrayStacks
def is_parentese_matching(expression):
    myStack = ArrayStacks()
    for i in expression:
        if i == "(":
            myStack.push(i)
        elif i == ")":
            if myStack.is_empty():
                return False
            myStack.pop()
        if myStack.is_empty:
            return True
        else:
            return False
result = is_parentese_matching("((A+B)*C)")
print(result)