class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        
class binarytree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while(True):
                if value < currentNode.value:
                    if not currentNode.left:
                        currentNode.left = newNode
                        return self
                    currentNode = currentNode.left
                    
                else:
                    if value > currentNode.value:
                        if not currentNode.right:
                            currentNode.right = newNode
                            return self
                        currentNode = currentNode.right
                        
                        
    def lookup(self,value):
        if not self.root:
            return False
        currentNode = self.root
        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            elif value == currentNode.value:
                return currentNode
        return False    
    
tree = binarytree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)