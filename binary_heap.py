class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class MaxHeap:
    def __init__(self):
        self.root = None
        self.nodes = []  # Keep track of nodes level-order (for easy insertion)

    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
            self.nodes.append(newNode)
            return self

        # Insert in level order (complete binary tree)
        for node in self.nodes:
            if not node.left:
                node.left = newNode
                self.nodes.append(newNode)
                self._heapify_up(newNode)
                return self
            elif not node.right:
                node.right = newNode
                self.nodes.append(newNode)
                self._heapify_up(newNode)
                return self

    def extract_max(self):
        if not self.root:
            return None

        maxValue = self.root.value

        if len(self.nodes) == 1:  # Only root exists
            self.root = None
            self.nodes.pop()
            return maxValue

        # Replace root with last node
        lastNode = self.nodes.pop()
        self.root.value = lastNode.value

        # Disconnect lastNode from its parent
        for node in self.nodes:
            if node.left == lastNode:
                node.left = None
                break
            if node.right == lastNode:
                node.right = None
                break

        self._heapify_down(self.root)
        return maxValue

    def _heapify_up(self, node):
        # Bubble up: swap values until heap property satisfied
        while node != self.root:
            parent = self._find_parent(node)
            if parent and node.value > parent.value:
                node.value, parent.value = parent.value, node.value
                node = parent
            else:
                break

    def _heapify_down(self, node):
        # Push down: swap with larger child if needed
        while node:
            largest = node
            if node.left and node.left.value > largest.value:
                largest = node.left
            if node.right and node.right.value > largest.value:
                largest = node.right

            if largest != node:
                node.value, largest.value = largest.value, node.value
                node = largest
            else:
                break

    def _find_parent(self, child):
        for node in self.nodes:
            if node.left == child or node.right == child:
                return node
        return None


class MinHeap:
    def __init__(self):
        self.root = None
        self.nodes = []  # Keep track of nodes level-order (for easy insertion)

    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
            self.nodes.append(newNode)
            return self

        # Insert in level order (complete binary tree)
        for node in self.nodes:
            if not node.left:
                node.left = newNode
                self.nodes.append(newNode)
                self._heapify_up(newNode)
                return self
            elif not node.right:
                node.right = newNode
                self.nodes.append(newNode)
                self._heapify_up(newNode)
                return self

    def extract_min(self):
        if not self.root:
            return None

        minValue = self.root.value

        if len(self.nodes) == 1:  # Only root exists
            self.root = None
            self.nodes.pop()
            return minValue

        # Replace root with last node
        lastNode = self.nodes.pop()
        self.root.value = lastNode.value

        # Disconnect lastNode from its parent
        for node in self.nodes:
            if node.left == lastNode:
                node.left = None
                break
            if node.right == lastNode:
                node.right = None
                break

        self._heapify_down(self.root)
        return minValue

    def _heapify_up(self, node):
        # Bubble up: swap values until heap property satisfied
        while node != self.root:
            parent = self._find_parent(node)
            if parent and node.value < parent.value:
                node.value, parent.value = parent.value, node.value
                node = parent
            else:
                break

    def _heapify_down(self, node):
        # Push down: swap with smaller child if needed
        while node:
            smallest = node
            if node.left and node.left.value < smallest.value:
                smallest = node.left
            if node.right and node.right.value < smallest.value:
                smallest = node.right

            if smallest != node:
                node.value, smallest.value = smallest.value, node.value
                node = smallest
            else:
                break

    def _find_parent(self, child):
        for node in self.nodes:
            if node.left == child or node.right == child:
                return node
        return None


# Example usage
print("=== Max Heap ===")
max_heap = MaxHeap()
max_heap.insert(10).insert(5).insert(20).insert(1)
print("Extract Max:", max_heap.extract_max())  # 20
print("Extract Max:", max_heap.extract_max())  # 10

print("\n=== Min Heap ===")
min_heap = MinHeap()
min_heap.insert(10).insert(5).insert(20).insert(1)
print("Extract Min:", min_heap.extract_min())  # 1
print("Extract Min:", min_heap.extract_min())  # 5