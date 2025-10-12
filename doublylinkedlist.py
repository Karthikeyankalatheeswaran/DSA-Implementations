"""

A Linked lists contains head and tail with
a value of [value , next].

Operations :
-> prepend - done
-> append - done
-> lookup or search
-> insert
-> delete

"""

class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinked_list :
    def __init__(self,value):
        self.head = {
            "value" : value,
            "next"  : None,
            "prev"  : None
            }
        self.tail = self.head
        self.length = 1
        
    def append(self,value): 
        # newNode = Node(value)  ->This is an alt way of declaring a class Node as a New node
        newNode = {
            "value" : value,
            "next"  : None,
            "prev"  : None
        }
        newNode["prev"] = self.tail
        self.tail["next"] = newNode #refers to the first linkedlist's next ->
        self.tail = newNode #refers to Base tail value
        self.length +=1
        return self
    
    def prepend(self,value):
        newNode = {
            "value" : value,
            "next"  : None,
            "prev"  : None
        }
        newNode["next"] = self.head
        self.head["prev"] = newNode 
        self.head = newNode
        self.length+=1
        return self
    
    def insert(self,index,value):
        if index >= self.length:
            return self.append(value)
        
        newNode = {
            "value" : value,
            "next"  : None,
            "prev"  : None
        }
        leader = self.traverseindex(index-1)
        follower = leader["next"]
        leader["next"] = newNode
        newNode["prev"] = leader
        newNode["next"] = follower
        follower["prev"] = newNode
        self.length+=1
        return self.printlist()
        
    def traverseindex(self,index):
        counter = 0
        currentNode = self.head
        while counter!=index:
            currentNode = currentNode["next"]
            counter+=1
        return currentNode
    
    def printlist(self):
        values_in_list = []
        currentNode = self.head
        while currentNode!=None : 
            values_in_list.append(currentNode["value"])
            currentNode =currentNode["next"]
        return values_in_list
    
    def remove(self,index):
        leader = self.traverseindex(index-1)
        unwantedNode = leader["next"]
        leader["next"] = unwantedNode["next"]
        self.length -+1
        return self.printlist()
        
    def __str__(self):
        return f"DoublyLinkedList\n\t(Head: {self.head}, Tail: {self.tail}, Length: {self.length})"    
        
    
my_linked_list = DoublyLinked_list(10)
my_linked_list.append(29)
my_linked_list.prepend(999)
# print(my_linked_list.remove(2))
# print(my_linked_list.printlist())
print(my_linked_list)
