class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    # Getter for the value
    @property
    def value(self):
        return self._value

    # Getter for the next node
    @property
    def next(self):
        return self._next

    # Setter for the next node
    @next.setter
    def next(self, new_next):
        self._next = new_next


"""
LinkedList stores a sequence of nodes by maintaining a reference to the head node.
Disadvantages of LinkedList:
- It uses more memory due to storing references for each node.
- Elements must be accessed sequentially as there is no direct indexing.
"""


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node into the beginning

    def insert_node(self, value):
        new_node = Node(value)

        # Case-1: If the LinkedList is empty
        if self.head is None:
            self.head = new_node


        # Case-2: Insert head at the beginning if the value is smaller than or equal to head
        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node

        # Case-3: Insert in the middle or the end:
        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next

            new_node.next = runner
            previous.next = new_node


    # Traverse the linked list and print each value
    def print_list_items(self):
        # If Linked List is empty
        if self.head is None:
            print("Linked List is empty")

        else:
            runner = self.head

            while runner is not None:
                print(runner.value)
                runner = runner.next
            print()

    # Counts and print the total number of nodes in the linked list
    def count_nodes(self):
        runner = self.head
        nodes_array = []

        if not runner:
            print("Linked List is empty")
            return
        while runner:
            nodes_array.append(runner)
            runner = runner.next
        print(f"Total number of nodes: {len(nodes_array)}")


    # Searches for a target value in the list and prints its index
    def find_nodes(self, target_value):
        self.head = None

        if self.head is None:
            print("Linked List is empty")
            return

        runner = self.head
        index = 0

        while runner is not None:
            if runner.value == target_value:
                print(f"Target value found at index: {index}")
                return
            runner = runner.next
            index += 1

        print(f"{target_value} is not present in the linked list.")

    # Deletes a node from the list
    def delete_node(self, target_value):
        self.head = None

        # Case-1: If the list is empty
        if self.head is None:
            print("Nothing to delete. List is empty")

        # Case-2: If the list has only one node
        elif self.head.value == target_value:
            self.head = self.head.next
            return

        # Case-3: If the node to be deleted is in the middle or the end
        previous = self.head
        runner = self.head.next

        while runner is not None:
            if runner == target_value:
                previous.next = runner.next
                return None
            previous = runner
            runner = runner.next

        # Case-4: Target value not found in the list
        print(f"{target_value} is not present in the linked list.")

# Creating a linked list instance
my_linked_list = LinkedList()

# Insert a node at the beginning of the list
my_linked_list.insert_node(5)
my_linked_list.insert_node(3)
my_linked_list.insert_node(1)
my_linked_list.insert_node(4)

# Accessing values for verification
print(my_linked_list.head.next.value)
print(my_linked_list.head.value)
print(my_linked_list.head.next.next.next.value)

# Traversing the list and printing elements
print("\n================Traversing the list=====================")
my_linked_list.print_list_items()






