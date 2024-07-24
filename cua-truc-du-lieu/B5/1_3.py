class Stack:
    def __init__(self):
        self.stack = []
    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def remove(self):
        if len(self.stack) <= 0:
            return ('No elements in Stack')
        else:
            return self.stack.pop()
        
AStack = Stack()
print(AStack.add ('data science'))
print(AStack.add('big data'))
print(AStack.add('IoT'))
print(AStack.add('deep learning'))
print(AStack.add('machine learning'))
print(AStack.remove())