class ArrayStack:

    def __init__(self):
        self.data = []
    
    def size(self):
        return len(self.data)

    def is_empty(self):
        if self.data == []:
            return True
        else:
            return False

    def push(self, data):
        self.data.append(data)
        return self.data

    def pop(self):
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            return self.data.pop()

    def stackTop(self):
        if self.data == []:
            return None
        else:
            return self.data[-1]

    def printStack(self):
        print(self.data)
    
    def is_parentheses_matching(self, expression):
        for i in expression:
            if i == '(':
                checker = False
                self.push(i)
            elif i == ')':
                if self.data == []:
                    return False
                self.pop()
        if self.data == []:
            return True
        else:
            return False

    def copyStack(self, Stack1, Stack2):
        for _ in range(len(s2.data)):
            s2.pop()
        for i in s1.data:
            s2.push(i)
    
    def infixToPostfix(self, expression):
        lv_of_op = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = ArrayStack()
        postfix = ""
        for i in expression:
            if i.isalnum():
                postfix += i
            elif i == '(':
                stack.push(i)
            elif i == ')':
                while not stack.is_empty() and stack.stackTop() != '(':
                    postfix += stack.pop()
                if not stack.is_empty() and stack.stackTop() == '(':
                    stack.pop()
            else:
                while not stack.is_empty() and stack.stackTop() != '(' and \
                        lv_of_op[i] <= lv_of_op[stack.stackTop()]:
                    postfix += stack.pop()
                stack.push(i)
        while not stack.is_empty():
            postfix += stack.pop()

        return postfix


exp = "A+B*C-D/E"
postfix = ArrayStack().infixToPostfix(exp)
print("Postfix of", exp, "is", postfix)
