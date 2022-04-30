class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def get_value(self):
        return self.value

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size  # the maximum capacity of the queue if entered
        self.size = 0  # current size of the queue

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            return "There isn't any data"

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0

    def enqueue(self, new_value):
        if self.has_space() == True:
            new_item = Node(new_value)
            print(f"{new_item} has been added to queue")
            if self.is_empty():
                self.head = new_item
                self.tail = new_item
            else:
                self.tail.set_next_node(new_item)
                self.tail = new_item
            self.size += 1
        else:
            print("There's not enough of space")

    def dequeue(self):
        if self.get_size() > 0:
            removed_value = self.head
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return removed_value.get_value()
        else:
            print(f"Can't be {self.size - 1}, queue underflow")


kuyruk = Queue()
print(kuyruk.size)

kuyruk.enqueue(15)
kuyruk.enqueue('Kahraman')
kuyruk.enqueue('Merhaba')
kuyruk.enqueue(8)

print(kuyruk.size)

kuyruk.dequeue()
kuyruk.dequeue()

print(kuyruk.size)

kuyruk.dequeue()
kuyruk.dequeue()
print(kuyruk.size)

kuyruk.dequeue()
