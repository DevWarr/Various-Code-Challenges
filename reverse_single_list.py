class Node:
    def __init__(self, value, nex):
        self.value = value
        self.next = nex

n1 = Node(5, None)
n2 = Node(4, n1)
n3 = Node(3, n2)
n4 = Node(2, n3)
n5 = Node(1, n4)
n6 = Node(0, None)

n6.next = n5


def reverse_list(head):
    prev = None
    curr = head
    while curr is not None:
        nex = curr.next
        curr.next = prev

        prev = curr
        curr = nex


def checker(head):
    node = head
    while node is not None:
        print(node.value)
        node = node.next

checker(n6)
print("\n")
reverse_list(n6)

checker(n1)