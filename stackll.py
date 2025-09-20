class Node:
    def __init__(self,value):
        self.value = value 
        self.next_val = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def push(self, value):
        newNode = Node(value)
        if self.length == 0:  
            self.top = newNode
            self.bottom = newNode
            self.length += 1
        else:
            exist_val = self.top
            self.top = newNode
            self.top.next_val = exist_val
        self.length += 1

        return self    
    
              
    def pop(self):
        if not self.top:
            return None
        exist_val = self.top
        self.top = self.top.next_val
        self.length -=1
        return exist_val


    def peek(self):
        if self.top:
            return self.top
        else:
            return None
        
    # def print_stack(self):
    #     """Prints the stack from top to bottom."""
    #     temp = self.top
    #     stack_str = "Top -> "
    #     while temp:
    #         stack_str += str(temp.value) + " -> "
    #         temp = temp.next_val
    #     print(stack_str + "None")
    
    
    def __str__(self):
        """Return a string representation of the stack."""
        return f"Stack (Top: {self.top.value if self.top else None}, Bottom: {self.bottom.value if self.bottom else None}, Length: {self.length})"

# ✅ Testing the stack
    
stack = Stack()
stack.push("Google")
stack.push("Udemy")
stack.push("YouTube")

# print("Stack after pushes:")
# stack.print_stack()  

print("\nTop element (peek):", stack.peek())

# print("\nPopped element:", stack.pop())
# stack.print_stack()

print("\nFinal stack details:", stack)