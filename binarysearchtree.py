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
    
    def delete(self, value):
        if not self.root:
            return False

        currentNode = self.root
        parentNode = None

        # Step 1: Find the node to delete and its parent
        while currentNode and currentNode.value != value:
            parentNode = currentNode
            if value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        # If the value is not found, return False
        if not currentNode:
            return False

        # Case 1: Node to be deleted is a leaf node (no children)
        if currentNode.left is None and currentNode.right is None:
            if parentNode is None:  # Deleting the root node
                self.root = None
            elif parentNode.left == currentNode:
                parentNode.left = None
            else:
                parentNode.right = None
            return True

        # Case 2: Node with one child
        elif currentNode.left is None or currentNode.right is None:
            childNode = currentNode.left if currentNode.left else currentNode.right
            if parentNode is None:  # Deleting the root node with one child
                self.root = childNode
            elif parentNode.left == currentNode:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
            return True

        # Case 3: Node with two children
        else:
            # Find the in-order successor (the smallest node in the right subtree)
            successorParent = currentNode
            successor = currentNode.right
            while successor.left:
                successorParent = successor
                successor = successor.left

            # Replace the currentNode's value with the successor's value
            currentNode.value = successor.value

            # Now, delete the successor node from its original position
            # This is essentially handling Case 1 or 2 on the successor
            if successorParent.left == successor:
                successorParent.left = successor.right
            else:
                successorParent.right = successor.right
            return True

    
tree = binarytree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)