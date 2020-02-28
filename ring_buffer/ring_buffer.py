from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Start things off by changing current to 0 if it is None...
        if self.current is None:
            self.current = 0

        # If storage is full
        if self.storage.length == self.capacity:

            # Get Head
            node = self.storage.head

            if self.current > 0:

                # Navigate index we're replacing
                for _ in range(0, self.current):
                    node = node.next

            # Replace value
            node.value = item

            # If our overflow is at the end of capacity
            if self.current == self.capacity - 1:
                # Set back to None which'll be set to 0 on next append call
                self.current = None
            else:
                # Otherwise, increment it up wards
                self.current += 1

            # Return out as to not continue with method
            return

        # Add to tail
        self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # Get the head
        head = self.storage.head

        # While head is not none
        while head:
            # Add to list
            list_buffer_contents.append(head.value)
            # navigate to next
            head = head.next

        # Return
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
