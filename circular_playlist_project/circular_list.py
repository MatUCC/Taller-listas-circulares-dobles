from node import Node


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def is_empty(self):
        return self.head is None

    def append(self, title, artist, duration):
        new_node = Node(title, artist, duration)

        if self.head is None:
            # Link the first node to itself in both directions.
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.current = new_node
            return new_node

        tail = self.head.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

        if self.current is None:
            self.current = new_node

        return new_node

    def delete_current(self):
        # Handle an empty playlist.
        if self.current is None:
            return None

        deleted = self.current

        if deleted.next is deleted:
            self.head = None
            self.current = None
        else:
            previous_node = deleted.prev
            next_node = deleted.next
            previous_node.next = next_node
            next_node.prev = previous_node

            if self.head is deleted:
                self.head = next_node

            self.current = next_node

        deleted.next = None
        deleted.prev = None
        return deleted

    def next_track(self):
        if self.current is not None:
            self.current = self.current.next
        return self.current

    def prev_track(self):
        if self.current is not None:
            self.current = self.current.prev
        return self.current

    def find_by_id(self, node_id):
        # Search by node identity without copying the linked list.
        if self.head is None:
            return None

        curr = self.head
        while True:
            if str(id(curr)) == str(node_id):
                return curr
            curr = curr.next
            if curr is self.head:
                break

        return None

    def set_current(self, node):
        if node is None:
            return False

        if self.head is None:
            return False

        curr = self.head
        while True:
            if curr is node:
                self.current = curr
                return True
            curr = curr.next
            if curr is self.head:
                break

        return False

    def iter_nodes(self):
        if self.head is None:
            return

        curr = self.head
        while True:
            yield curr
            curr = curr.next
            if curr is self.head:
                break

    def count(self):
        if self.head is None:
            return 0

        total = 0
        curr = self.head
        while True:
            total += 1
            curr = curr.next
            if curr is self.head:
                break

        return total
