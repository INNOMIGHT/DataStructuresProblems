import time


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.next_node = None
        self.last = None

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
            self.last = self.head
        else:
            self.last.next_node = Node(val)
            self.last = self.last.next_node

    def nth_to_last_node(self, n):
        left_pointer = self.head
        right_pointer = self.head

        for i in range(n-1):
            if not right_pointer.next_node:
                print("Error! Size Not Suitable")

            right_pointer = right_pointer.next_node

        while right_pointer.next_node:
            left_pointer = left_pointer.next_node
            right_pointer = right_pointer.next_node

        return left_pointer.value


def measure_time(n, fn):
    start_millis = int(round(time.time() * 1000))
    fn(n)
    print("Total Time Taken = " + str((int(round(time.time() * 1000)) - start_millis)) + "ms")


linked_list = LinkedList()


def add_numbers(limit):
    for num in range(limit):
        linked_list.add(num)


print("Adding numbers...")
print(measure_time(10000000, add_numbers))
print("Searching for nth term...")
print(measure_time(500, linked_list.nth_to_last_node))
