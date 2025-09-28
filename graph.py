class Graph:
    def __init__ (self):
        self.numberofNodes = 0
        self.adjacentLists = {}
        
    def addVertex(self,node):
        if node not in self.adjacentLists:
            self.adjacentLists[node] = []
            self.numberofNodes +=1
    
    def addEdges(self,node1,node2):
        if node1 in self.adjacentLists and node2 in self.adjacentLists:
            self.adjacentLists[node1].append(node2)
            self.adjacentLists[node2].append(node1)
        else:
            print("One or both of the nodes do not exist.")
            
    def showGraph(self):
        for node in self.adjacentLists:
            print(f"{node} --> {self.adjacentLists[node]}")
        
        
    def showConnection(self):
        """
        Shows the connections (edges) of the graph.
        """
        print("\nDisplaying all connections:")
        for node in self.adjacentLists:
            for neighbor in self.adjacentLists[node]:
                # To avoid printing each edge twice (e.g., 1-2 and 2-1)
                # a more robust implementation would use a set of visited edges,
                # but for simplicity, we'll just print all connections.
                print(f"Connection from {node} to {neighbor}")
    
    
g = Graph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)

g.addEdges(1, 2)
g.addEdges(2, 3)
g.addEdges(1, 3)

g.showGraph()