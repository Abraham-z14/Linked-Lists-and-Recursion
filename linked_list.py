class Node:
    """
    A node stores integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that uses recursion for sum, search, and reverse.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node at the beginning of the list.

        Time complexity: O(1)
        """
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.

        Time complexity: O(n)
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """
        Return the sum of all node values using recursion.
        """

        def sum_nodes(node):
            # Base case:
            # Reaching None means there are no more values to add.
            if node is None:
                return 0

            # Recursive case:
            # Add this node's data to the sum of the remaining nodes.
            return node.data + sum_nodes(node.next)

        return sum_nodes(self.head)

    def recursive_reverse(self):
        """
        Reverse the linked list in-place using recursion.
        """

        def reverse_nodes(previous, current):
            # Base case:
            # Once current becomes None, previous is the new head.
            if current is None:
                return previous

            # Save the next node before changing the pointer.
            next_node = current.next

            # Reverse the current node's pointer.
            current.next = previous

            # Continue through the rest of the list.
            return reverse_nodes(current, next_node)

        self.head = reverse_nodes(None, self.head)

    def recursive_search(self, target):
        """
        Return True if target exists in the list, otherwise False.
        """

        def search_nodes(node):
            # Base case:
            # Reaching None means the target was not found.
            if node is None:
                return False

            # Base case:
            # We found the target.
            if node.data == target:
                return True

            # Recursive case:
            # Search the remainder of the list.
            return search_nodes(node.next)

        return search_nodes(self.head)

    def display(self):
        """
        Print the linked list in a readable format.
        """
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.data))
            current = current.next

        values.append("None")

        print(" -> ".join(values))