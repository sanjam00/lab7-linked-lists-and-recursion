class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data      # stores value
        self.next = None      # pointer to next node


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None  # start with empty list

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head  # point to current head
        self.head = new_node       # update head

    def insert_at_end(self, data):
        new_node = Node(data)

        # if list is empty
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:   # traverse until last node
            current = current.next

        current.next = new_node  # attach at end

    def recursive_sum(self):
        def helper(node):
            if node is None:
                return 0
            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        def helper(prev, current):
            if current is None:
                return prev

            next_node = current.next 
            current.next = prev       # reverse pointer

            return helper(current, next_node)

        self.head = helper(None, self.head)

    def recursive_search(self, target):
        def helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return helper(node.next)

        return helper(self.head)

    def display(self):
        current = self.head
        result = ""

        while current:
            result += str(current.data) + " -> "
            current = current.next

        result += "None"
        print(result)