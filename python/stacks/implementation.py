class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)

monika=Stack()
monika.push('physics')
monika.push('chemistry')
monika.push('maths')

print(monika.stack)
print(monika.pop())
print(monika.peek())
print(monika.isEmpty())
print(monika.size())

rajesh=Stack()
rajesh.push('python')
rajesh.push('AI')
rajesh.push('ML')

print(rajesh.stack)
print(rajesh.pop())
print(rajesh.peek())
print(rajesh.isEmpty())
print(rajesh.size())

