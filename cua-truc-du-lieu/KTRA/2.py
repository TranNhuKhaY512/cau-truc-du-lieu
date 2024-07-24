
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    #Insert to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    #find value to compare the value
    def findval(self, inval):
        if (inval < self.data):
            if self.left is None:
                return (str(inval)+" Not Found")
            return (self.left.findval(inval))
        if (inval > self.data):
            if self.right is None:
                return (str(inval)+" Not Found")
            return self.right.findval(inval)
        else:
            print(str(self.data) + 'is found')
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
            print( self.data)
        if self.right:
            self.right.PrintTree()
            print( self.data)

root = Node(53)
root.insert(36)
root.insert(65)
root.insert(30)
root.insert(44)
root.insert(58)
root.insert(69)
root.insert(8)
root.insert(31)
root.insert(34)
root.insert(51)
print(root.findval(49))


